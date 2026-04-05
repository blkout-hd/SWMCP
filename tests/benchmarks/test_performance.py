"""Performance benchmarks."""

import pytest


@pytest.mark.benchmark
def test_diff_performance(benchmark):
    """Benchmark diff calculation."""
    try:
        from swmcp._swmcp_rs import calculate_diff
        
        old = "\n".join([f"line {i}" for i in range(1000)])
        new = "\n".join([f"line {i if i != 500 else 'modified'}" for i in range(1000)])
        
        result = benchmark(calculate_diff, old, new)
        assert result is not None
    except ImportError:
        pytest.skip("Rust extension not built")
