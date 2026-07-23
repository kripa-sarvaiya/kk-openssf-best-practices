import pytest

from semverbump import bump, parse


def test_parse_basic():
    v = parse("1.4.2")
    assert (v.major, v.minor, v.patch) == (1, 4, 2)
    assert v.prerelease is None


def test_parse_prerelease():
    v = parse("2.0.0-rc.1")
    assert v.prerelease == "rc.1"


@pytest.mark.parametrize(
    "current,part,expected",
    [
        ("1.4.2", "major", "2.0.0"),
        ("1.4.2", "minor", "1.5.0"),
        ("1.4.2", "patch", "1.4.3"),
        ("2.0.0-rc.1", "patch", "2.0.1"),
    ],
)
def test_bump(current, part, expected):
    assert str(bump(parse(current), part)) == expected


def test_invalid_version():
    with pytest.raises(ValueError):
        parse("not.a.version")
