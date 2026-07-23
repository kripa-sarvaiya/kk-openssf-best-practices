[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/13761/badge)](https://www.bestpractices.dev/projects/13761)

# semver-bump

A tiny, dependency-free command-line tool for bumping
[semantic version](https://semver.org/) numbers.

`semver-bump` takes a version string and prints the next version after
incrementing the major, minor, or patch component, following SemVer rules
(bumping a higher-order component resets the lower ones).

## Installation

```bash
pip install .
```

Or install in editable mode for development:

```bash
pip install -e ".[dev]"
```

## Usage

```bash
$ semverbump 1.4.2 --patch
1.4.3

$ semverbump 1.4.2 --minor
1.5.0

$ semverbump 1.4.2 --major
2.0.0
```

Prerelease tags are recognized on input and dropped when bumping:

```bash
$ semverbump 2.0.0-rc.1 --patch
2.0.1
```

## Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## Contributing

Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). By
participating you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## Security

To report a vulnerability, please follow the process in [SECURITY.md](SECURITY.md).

## License

Released under the [MIT License](LICENSE).
