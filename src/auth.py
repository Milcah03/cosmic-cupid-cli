import os
import json
import webbrowser
import requests
from pathlib import Path
from urllib.parse import urlencode
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align

console = Console()

# GitHub OAuth Configuration
GITHUB_CLIENT_ID = os.getenv("GITHUB_OAUTH_CLIENT_ID", "your_client_id_here")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_OAUTH_CLIENT_SECRET", "your_client_secret_here")
GITHUB_AUTH_URL = "https://github.com/login/oauth/authorize"
GITHUB_TOKEN_URL = "https://github.com/login/oauth/access_token"
GITHUB_USER_URL = "https://api.github.com/user"

# Token storage
TOKEN_DIR = Path.home() / ".cosmic-cupid"
TOKEN_FILE = TOKEN_DIR / "github_token.json"


class GitHubOAuthHandler(BaseHTTPRequestHandler):
    """Handles OAuth callback from GitHub"""
    auth_code = None

    def do_GET(self):
        if "code=" in self.path:
            self.auth_code = self.path.split("code=")[1].split("&")[0]
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                b"<html><body><h1>Authentication successful!</h1>"
                b"<p>You can close this window and return to your terminal.</p></body></html>"
            )
        else:
            self.send_response(400)
            self.end_headers()

    def log_message(self, format, *args):
        pass


class GitHubOAuth:
    def __init__(self):
        self.access_token = None
        self.user_info = None
        self.redirect_uri = "http://localhost:8888/callback"

    def initiate_login(self):
        """Start GitHub OAuth flow"""
        TOKEN_DIR.mkdir(parents=True, exist_ok=True)

        params = {
            "client_id": GITHUB_CLIENT_ID,
            "redirect_uri": self.redirect_uri,
            "scope": "user:email",
            "state": "cosmic-cupid-auth",
        }
        auth_url = f"{GITHUB_AUTH_URL}?{urlencode(params)}"

        server = HTTPServer(("localhost", 8888), GitHubOAuthHandler)
        server_thread = Thread(target=server.handle_request, daemon=True)
        server_thread.start()

        console.print(
            Align.center(
                Panel(
                    Text.assemble(
                        ("Opening GitHub authorization...\n", "bold cyan"),
                        ("If browser doesn't open, visit:\n", "dim"),
                        (auth_url, "bright_blue underline"),
                    ),
                    border_style="cyan",
                    padding=(1, 2),
                )
            )
        )

        webbrowser.open(auth_url)
        server_thread.join(timeout=120)

        if not GitHubOAuthHandler.auth_code:
            raise Exception("Authentication timed out or was cancelled")

        return self._exchange_code_for_token(GitHubOAuthHandler.auth_code)

    def _exchange_code_for_token(self, code):
        """Exchange authorization code for access token"""
        data = {
            "client_id": GITHUB_CLIENT_ID,
            "client_secret": GITHUB_CLIENT_SECRET,
            "code": code,
            "redirect_uri": self.redirect_uri,
        }
        headers = {"Accept": "application/json"}

        try:
            response = requests.post(GITHUB_TOKEN_URL, data=data, headers=headers, timeout=10)
            response.raise_for_status()
            result = response.json()

            if "error" in result:
                raise Exception(f"OAuth error: {result.get('error_description', result['error'])}")

            self.access_token = result.get("access_token")
            self._fetch_user_info()
            self._save_token()

            return True

        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to exchange code for token: {str(e)}")

    def _fetch_user_info(self):
        """Fetch user info from GitHub"""
        headers = {"Authorization": f"token {self.access_token}"}
        try:
            response = requests.get(GITHUB_USER_URL, headers=headers, timeout=10)
            response.raise_for_status()
            self.user_info = response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch user info: {str(e)}")

    def _save_token(self):
        """Save token to local file"""
        token_data = {
            "access_token": self.access_token,
            "username": self.user_info.get("login"),
        }
        with open(TOKEN_FILE, "w") as f:
            json.dump(token_data, f)

    def get_username(self):
        """Return authenticated username"""
        return self.user_info.get("login") if self.user_info else None

    @staticmethod
    def is_authenticated():
        """Check if user has valid saved token"""
        return TOKEN_FILE.exists()

    @staticmethod
    def clear_token():
        """Clear saved token"""
        if TOKEN_FILE.exists():
            TOKEN_FILE.unlink()
