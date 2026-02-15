# GitHub OAuth Setup for Cosmic Cupid

This guide explains how to set up GitHub OAuth authentication for the Cosmic Cupid CLI.

## Prerequisites

- A GitHub account
- Access to create OAuth apps in your GitHub account settings

## Step 1: Create a GitHub OAuth Application

1. Go to [GitHub Settings > Developer settings > OAuth Apps](https://github.com/settings/developers)
2. Click "New OAuth App"
3. Fill in the application details:
   - **Application name**: Cosmic Cupid
   - **Homepage URL**: `http://localhost`
   - **Authorization callback URL**: `http://localhost:8888/callback`
4. Click "Register application"
5. You'll be taken to your app's settings page

## Step 2: Get Your Credentials

On your OAuth app settings page, you'll see:
- **Client ID**
- **Client Secret** (click "Generate a new client secret" if needed)

## Step 3: Set Environment Variables

Set the following environment variables before running Cosmic Cupid:

```bash
export GITHUB_OAUTH_CLIENT_ID="your_client_id_here"
export GITHUB_OAUTH_CLIENT_SECRET="your_client_secret_here"
```

### On Windows (Command Prompt):
```cmd
set GITHUB_OAUTH_CLIENT_ID=your_client_id_here
set GITHUB_OAUTH_CLIENT_SECRET=your_client_secret_here
```

### On Windows (PowerShell):
```powershell
$env:GITHUB_OAUTH_CLIENT_ID="your_client_id_here"
$env:GITHUB_OAUTH_CLIENT_SECRET="your_client_secret_here"
```

## Step 4: Run Cosmic Cupid

```bash
cosmic-cupid
```

When prompted, type `/login` to authenticate with GitHub.

## Authentication Flow

1. App starts and displays login prompt
2. Type `/login` to initiate authentication
3. Your default browser opens with GitHub authorization page
4. Authorize the application
5. You're automatically logged in and the app continues to card generation

## Token Storage

- Authentication tokens are stored in `~/.cosmic-cupid/github_token.json`
- To logout, delete this file or clear it via the app

## Troubleshooting

### "Authentication timed out"
- Ensure your browser can reach `http://localhost:8888`
- Check that no firewall is blocking the callback
- Try again and complete authorization within 2 minutes

### "OAuth error"
- Verify your Client ID and Client Secret are correct
- Ensure environment variables are set
- Check that the OAuth app is properly registered on GitHub

### Port 8888 already in use
- Close any other applications using port 8888
- Or modify the `redirect_uri` in `src/auth.py` and update your OAuth app settings

## Security Notes

- Never commit your `GITHUB_OAUTH_CLIENT_SECRET` to version control
- Keep your `.cosmic-cupid/` directory private (contains sensitive tokens)
- Consider using a `.env` file with environment variable loading in production
