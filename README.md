# Cosmic Cupid CLI 🌹✨

An AI-powered cosmic Valentine card generator for the terminal. Generate personalized astrological compatibility readings and beautiful Valentine cards for you and your cosmic soulmate.

## Features

✨ **Astrological Compatibility** - Generate detailed cosmic compatibility readings between two people based on their birth charts

💖 **Beautiful Terminal UI** - Rich, colorful, and interactive command-line interface with animations

📸 **Card Generation** - Export your cosmic destiny cards as beautiful PNG images

🔐 **GitHub OAuth** - Secure authentication with GitHub for personalized experiences

🎨 **Customizable Output** - Control card styling and formatting

## Installation

### Quick Start with pip

```bash
pip install cosmic-cupid
```

### From GitHub (development)

```bash
git clone https://github.com/Milcah03/cosmic-cupid-cli.git
cd cosmic-cupid-cli
pip install -e .
```

## Usage

### Running Cosmic Cupid

```bash
cosmic-cupid
```

The application will:
1. Prompt you to authenticate with GitHub (type `/login`)
2. Ask for you and your partner's names and birthdates
3. Generate a cosmic compatibility reading
4. Create and save a beautiful Valentine card image

### Setting up GitHub OAuth

1. Create a GitHub OAuth App (see [AUTH_SETUP.md](AUTH_SETUP.md) for detailed steps)
2. Set environment variables:
   ```bash
   export GITHUB_OAUTH_CLIENT_ID="your_client_id"
   export GITHUB_OAUTH_CLIENT_SECRET="your_client_secret"
   ```
3. Run `cosmic-cupid`

**Note:** On your first run, type `/login` at the authentication prompt to begin the OAuth flow.

## Requirements

- Python 3.8 or higher
- Internet connection (for GitHub OAuth)
- Modern terminal with Unicode support (for best visual experience)

## Dependencies

- **rich** - Beautiful terminal formatting
- **kerykeion** - Astrological calculations
- **Pillow** - Image generation
- **requests** - HTTP communication

## Documentation

- [AUTH_SETUP.md](AUTH_SETUP.md) - GitHub OAuth configuration guide
- [CHANGELOG.md](CHANGELOG.md) - Version history and changes

## Examples

### Generate a Compatibility Reading

```
$ cosmic-cupid
🌹 COSMIC CUPID 2026 🌹
A partner ritual for the fated.

❤ YOUR DETAILS
Your Name: Alice
Birthdate: Dec 03 1990

❤ PARTNER DETAILS
Partner Name: Bob
Birthdate: May 20 1992

✨ Destiny Card Saved ✨
~/cosmic-destiny/Alice_Bob.png
```

## Development

### Setup Development Environment

```bash
git clone https://github.com/Milcah03/cosmic-cupid-cli.git
cd cosmic-cupid-cli
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Code Style

This project uses black for code formatting:

```bash
black src/
```

## Architecture

- `src/main.py` - Application entry point and main flow
- `src/auth.py` - GitHub OAuth authentication
- `src/engine.py` - Astrological calculations
- `src/ui.py` - Terminal UI components
- `src/exporter.py` - Image generation and export

## Security

- Tokens are stored locally in `~/.cosmic-cupid/github_token.json`
- OAuth credentials should be set via environment variables
- No credentials are committed to version control
- See [AUTH_SETUP.md](AUTH_SETUP.md) for security best practices

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

- Powered by [Kerykeion](https://github.com/g-battaglia/kerykeion) for astrological calculations
- Beautiful terminal UI with [Rich](https://github.com/Textualize/rich)
- GitHub OAuth integration for secure authentication

## Support

For issues, questions, or suggestions, please open an issue on [GitHub Issues](https://github.com/Milcah03/cosmic-cupid-cli/issues).

---

Made with 💖 and ✨ cosmic energy
