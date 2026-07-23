# Contributing

Thanks for your interest in improving semver-bump! Contributions of all kinds
are welcome — bug reports, documentation, and code.

## Getting started

1. Fork and clone the repository.
2. Create a virtual environment and install in editable mode:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -e ".[dev]"
   ```
3. Run the tests:
   ```bash
   pytest
   ```

## Making changes

- Keep changes focused and add tests for new behavior.
- Follow the existing code style (PEP 8).
- Update `CHANGELOG.md` under the "Unreleased" heading.

## Submitting

Open a pull request describing what changed and why. A maintainer will review
it as soon as possible.
