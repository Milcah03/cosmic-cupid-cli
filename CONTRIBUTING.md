# Contributing to Cosmic Cupid

Thank you for your interest in contributing to Cosmic Cupid! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please be respectful, inclusive, and constructive in all interactions.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Git
- GitHub account

### Development Setup

1. **Fork the repository** on GitHub

2. **Clone your fork**
   ```bash
   git clone https://github.com/your-username/cosmic-cupid-cli.git
   cd cosmic-cupid-cli
   ```

3. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install in development mode**
   ```bash
   pip install -e ".[dev]"
   ```

5. **Set up GitHub OAuth** (for testing auth features)
   - See [AUTH_SETUP.md](AUTH_SETUP.md)
   - Set environment variables for OAuth credentials

## Making Changes

### Branch Naming
- Feature: `feature/description`
- Bug fix: `fix/description`
- Documentation: `docs/description`

Example: `feature/add-dark-mode`

### Code Style

We use **Black** for code formatting and **flake8** for linting.

```bash
# Format code
black src/

# Check linting
flake8 src/
```

### Commit Messages

Write clear, descriptive commit messages:
- Use imperative mood ("Add feature" not "Added feature")
- Keep first line under 50 characters
- Explain why, not just what

Example:
```
Add customizable card colors

Allow users to specify RGB values for card styling
to personalize their cosmic cards.
```

### Testing

Run tests before submitting:
```bash
pytest
```

For testing with multiple Python versions:
```bash
# Install tox
pip install tox

# Run tests for all supported versions
tox
```

## Submitting Changes

### Pull Request Process

1. **Update your fork** with latest changes
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Push your changes**
   ```bash
   git push origin your-branch-name
   ```

3. **Create a Pull Request** on GitHub
   - Use a clear, descriptive title
   - Reference any related issues (#123)
   - Describe the changes and their purpose
   - Include before/after examples if applicable

4. **Address feedback** from reviewers
   - Make requested changes
   - Push new commits
   - Don't force-push (keeps discussion history)

## Types of Contributions

### Bug Reports
- Clear, reproducible steps
- Expected vs. actual behavior
- Python version and OS
- Error messages/logs

### Feature Requests
- Use case and motivation
- Example usage
- Any alternatives considered

### Documentation
- README updates
- Code comments for complex logic
- Examples and tutorials
- API documentation

### Code
- New features
- Bug fixes
- Performance improvements
- Code refactoring

## Style Guidelines

### Python
- Follow PEP 8 (enforced by Black and flake8)
- Use type hints where helpful
- Comment complex logic
- Keep functions focused and small

### Naming
- Variables/functions: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`

### Documentation
- Docstrings for all public functions/classes
- Include parameter types and return types
- Add usage examples for complex functions

## Project Structure

```
cosmic-cupid-cli/
├── src/
│   ├── main.py          # Application entry point
│   ├── auth.py          # GitHub OAuth
│   ├── engine.py        # Astrological calculations
│   ├── ui.py            # Terminal UI
│   └── exporter.py      # Image generation
├── .github/workflows/   # CI/CD pipelines
├── README.md            # Project documentation
├── AUTH_SETUP.md        # OAuth setup guide
├── CHANGELOG.md         # Version history
├── LICENSE              # MIT License
└── pyproject.toml       # Package configuration
```

## Common Tasks

### Add a New Feature
1. Create feature branch
2. Make changes with tests
3. Update CHANGELOG.md
4. Submit PR with description

### Fix a Bug
1. Create issue describing the bug
2. Create fix branch
3. Add test case that reproduces bug
4. Fix the bug (test should pass)
5. Submit PR linking to issue

### Update Documentation
1. Create docs branch
2. Make documentation changes
3. Test that links work
4. Submit PR

## Release Process

Releases are handled by maintainers:
1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Create git tag (`v0.1.0`)
4. Push tag to trigger GitHub Actions
5. CI/CD automatically publishes to PyPI
6. Binaries are built and attached to release

## Questions?

- **Issues**: Use GitHub Issues for bugs and feature requests
- **Discussions**: Use GitHub Discussions for questions
- **Security**: Email security concerns privately

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Cosmic Cupid! Your help makes this project better. ✨💖
