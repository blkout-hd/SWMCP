"""Tests for Rust extension module."""

import pytest


def test_rust_module_import():
    """Test Rust module can be imported."""
    try:
        import swmcp._swmcp_rs as rust_ext
        assert rust_ext.__version__ is not None
    except ImportError:
        pytest.skip("Rust extension not built")


def test_calculate_diff():
    """Test diff calculation."""
    try:
        from swmcp._swmcp_rs import calculate_diff
        
        old = "line 1\nline 2\nline 3"
        new = "line 1\nmodified\nline 3"
        
        diff = calculate_diff(old, new)
        assert "-line 2" in diff
        assert "+modified" in diff
    except ImportError:
        pytest.skip("Rust extension not built")
