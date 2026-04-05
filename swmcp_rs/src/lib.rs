//! SWMCP Rust Extension Module
//!
//! High-performance operations implemented in Rust:
//! - String diffing algorithms
//! - SSH client operations
//! - Terminal emulation
//! - Memory-safe mutex operations

use pyo3::prelude::*;

mod diff;
mod ssh;
mod terminal;

/// Calculate unified diff between two strings.
///
/// Args:
///     old: Original string
///     new: Modified string
///     context_lines: Number of context lines (default 3)
///
/// Returns:
///     Unified diff as string
#[pyfunction]
fn calculate_diff(
    old: &str,
    new: &str,
    context_lines: Option<usize>,
) -> PyResult<String> {
    let context = context_lines.unwrap_or(3);
    Ok(diff::calculate_diff(old, new, context))
}

/// Apply unified diff to string.
///
/// Args:
///     original: Original string
///     diff: Unified diff to apply
///
/// Returns:
///     Modified string after applying diff
#[pyfunction]
fn apply_diff(original: &str, diff: &str) -> PyResult<String> {
    diff::apply_diff(original, diff)
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(e.to_string()))
}

/// Python module initialization.
#[pymodule]
fn _swmcp_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(calculate_diff, m)?)?;
    m.add_function(wrap_pyfunction!(apply_diff, m)?)?;
    
    // Add version
    m.add("__version__", env!("CARGO_PKG_VERSION"))?;
    
    Ok(())
}
