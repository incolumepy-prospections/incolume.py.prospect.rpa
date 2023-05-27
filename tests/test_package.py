"""Module test for principal package."""
import re

import pytest

from incolume.py.prospect.rpa import __version__, configfile, load, versionfile

__author__ = "@britodfbr"  # pragma: no cover


class TestCase:
    """Test case class."""
    @pytest.mark.parametrize(
        "entrance",
        (
            configfile,
            versionfile,
        ),
    )
    def test_exists(self, entrance):
        """Test if exists files."""
        assert entrance.exists(), f"{entrance=}"

    @pytest.mark.parametrize(
        "entrance",
        (
            configfile,
            versionfile,
        ),
    )
    def test_is_file(self, entrance):
        """Test if are files."""
        assert entrance.is_file(), f"{entrance=}"

    @pytest.mark.parametrize(
        "entrance",
        (
            configfile,
            versionfile,
        ),
    )
    def test_same_version(self, entrance):
        """Test same version."""
        try:
            with entrance.open("rb") as stream:
                version = load(stream)["tool"]["poetry"]["version"]
        except ValueError:
            version = entrance.read_text().strip()
        assert version == __version__

    @pytest.mark.parametrize(
        ["entrance", "expected"],
        (
            (__version__, True),
            ("1", False),
            ("1.0", False),
            ("0.1", False),
            ("1.1.1-rc0", False),
            ("1.1.1-rc-0", False),
            ("1.0.1-dev0", False),
            ("1.1.1-a0", False),
            ("1.1.1-a.0", True),
            ("0.0.1", True),
            ("0.1.0", True),
            ("1.0.0", True),
            ("1.0.1", True),
            ("1.1.1", True),
            ("1.1.1-rc.0", True),
            ("1.0.1-dev.0", True),
            ("1.0.1-dev.1", True),
            ("1.0.1-dev.2", True),
            ("1.0.1-alpha.0", True),
            ("1.0.1-alpha.266", True),
            ("1.0.1-dev.0", True),
            ("1.0.1-beta.0", True),
            ("1.1.1-alpha.99999", True),
            ("11111.1.1-rc.99999", True),
            ("1.1.99999", True),
            ("1.999999.1", True),
        ),
    )
    def test_semantic_version(self, entrance, expected):
        """Test semantic version asserts."""
        assert (
            bool(
                re.fullmatch(
                    r"^\d+(\.\d+){2}((-\w+\.\d+)|(\w+\d+))?$",
                    entrance,
                    flags=re.I,
                )
            )
            == expected
        )
