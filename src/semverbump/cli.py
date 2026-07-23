"""Command-line interface for semver-bump."""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass

_SEMVER_RE = re.compile(
    r"^(?P<major>0|[1-9]\d*)\."
    r"(?P<minor>0|[1-9]\d*)\."
    r"(?P<patch>0|[1-9]\d*)"
    r"(?:-(?P<prerelease>[0-9A-Za-z.-]+))?$"
)


@dataclass(frozen=True)
class Version:
    """A parsed semantic version."""

    major: int
    minor: int
    patch: int
    prerelease: str | None = None

    def __str__(self) -> str:
        base = f"{self.major}.{self.minor}.{self.patch}"
        return f"{base}-{self.prerelease}" if self.prerelease else base


def parse(text: str) -> Version:
    """Parse a semantic version string into a :class:`Version`."""
    match = _SEMVER_RE.match(text.strip())
    if not match:
        raise ValueError(f"not a valid semantic version: {text!r}")
    return Version(
        major=int(match["major"]),
        minor=int(match["minor"]),
        patch=int(match["patch"]),
        prerelease=match["prerelease"],
    )


def bump(version: Version, part: str) -> Version:
    """Return a new :class:`Version` with the requested part incremented.

    Bumping a higher-order part resets the lower ones, per SemVer rules.
    Any prerelease tag is dropped on a bump.
    """
    if part == "major":
        return Version(version.major + 1, 0, 0)
    if part == "minor":
        return Version(version.major, version.minor + 1, 0)
    if part == "patch":
        return Version(version.major, version.minor, version.patch + 1)
    raise ValueError(f"unknown part: {part!r}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="semverbump",
        description="Bump a semantic version string.",
    )
    parser.add_argument("version", help="current version, e.g. 1.4.2")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--major", action="store_const", const="major", dest="part")
    group.add_argument("--minor", action="store_const", const="minor", dest="part")
    group.add_argument("--patch", action="store_const", const="patch", dest="part")
    args = parser.parse_args(argv)

    try:
        current = parse(args.version)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    print(bump(current, args.part))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
