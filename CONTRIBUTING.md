# Contributing to SWMCP

Thank you for your interest in contributing to SWMCP! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and collaborative environment.

## Getting Started

### Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/SWMCP.git
   cd SWMCP
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -e ".[dev]"
   ```

4. **Build Rust Extension**
   ```bash
   maturin develop --release
   ```

5. **Run Tests**
   ```bash
   pytest
   ```

## Development Workflow

### Branching Strategy

- `main` - Stable release branch
- `develop` - Development branch for integration
- `feature/*` - New features
- `bugfix/*` - Bug fixes
- `perf/*` - Performance improvements

### Making Changes

1. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Your Changes**
   - Write clear, concise code
   - Follow existing code style
   - Add tests for new functionality
   - Update documentation as needed

3. **Run Tests and Linters**
   ```bash
   # Format code
   black swmcp/ tests/
   ruff check --fix swmcp/ tests/
   
   # Type checking
   mypy swmcp/
   
   # Run tests
   pytest
   
   # Rust formatting
   cd swmcp_rs && cargo fmt && cargo clippy
   ```

4. **Commit Changes**
   ```bash
   git add .
   git commit -m "feat: add new feature"
   ```
   
   Use conventional commit format:
   - `feat:` - New feature
   - `fix:` - Bug fix
   - `docs:` - Documentation changes
   - `perf:` - Performance improvements
   - `refactor:` - Code refactoring
   - `test:` - Test additions/changes
   - `chore:` - Maintenance tasks

5. **Push and Create PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   
   Then create a Pull Request on GitHub.

## Code Style

### Python

- Follow PEP 8 guidelines
- Use Black for formatting (line length 100)
- Use type hints for all functions
- Write docstrings for all public APIs

**Example:**
```python
from typing import Optional

async def process_file(
    path: str,
    encoding: str = "utf-8",
    timeout: Optional[int] = None
) -> dict:
    """Process a file and return results.
    
    Args:
        path: File path to process
        encoding: Text encoding to use
        timeout: Optional timeout in seconds
        
    Returns:
        Dictionary with processing results
        
    Raises:
        FileNotFoundError: If file doesn't exist
        TimeoutError: If processing exceeds timeout
    """
    # Implementation
    pass
```

### Rust

- Follow Rust standard style (rustfmt)
- Use clippy for linting
- Document public APIs with doc comments
- Prefer safe Rust; unsafe blocks require justification

**Example:**
```rust
/// Calculate diff between two strings.
///
/// # Arguments
///
/// * `old` - Original string
/// * `new` - Modified string
/// * `context_lines` - Number of context lines
///
/// # Returns
///
/// Unified diff as string
pub fn calculate_diff(old: &str, new: &str, context_lines: usize) -> String {
    // Implementation
}
```

## Testing

### Test Structure

- Unit tests in same directory as code
- Integration tests in `tests/integration/`
- Benchmarks in `tests/benchmarks/`

### Writing Tests

```python
import pytest
from swmcp.tools import process_file

@pytest.mark.asyncio
async def test_process_file(temp_file):
    """Test file processing."""
    result = await process_file(str(temp_file))
    assert result["status"] == "success"

@pytest.mark.slow
async def test_large_file_processing():
    """Test processing of large files."""
    # Slow test implementation
    pass
```

### Running Tests

```bash
# All tests
pytest

# Specific test file
pytest tests/test_server.py

# With coverage
pytest --cov=swmcp --cov-report=html

# Skip slow tests
pytest -m "not slow"

# Benchmarks only
pytest tests/benchmarks/ --benchmark-only
```

## Documentation

### Updating README

- Keep README concise and up-to-date
- Add examples for new features
- Update performance benchmarks if applicable

### API Documentation

- Document all public APIs
- Include usage examples
- Specify parameter types and return values
- Note any exceptions that may be raised

## Performance Considerations

### When to Use Rust

- CPU-intensive operations (parsing, diffing, encoding)
- Hot paths in critical code
- Operations requiring memory safety guarantees

### When to Use Python

- I/O-bound operations
- Orchestration and coordination
- Rapid prototyping

### Benchmarking

Always benchmark performance-critical changes:

```bash
pytest tests/benchmarks/ --benchmark-only --benchmark-compare
```

## Security

### Reporting Vulnerabilities

**DO NOT** create public issues for security vulnerabilities.

Email: security@sbscrpt.com

### Security Best Practices

- Never commit secrets or credentials
- Use secure defaults
- Validate all inputs
- Prefer memory-safe operations
- Use constant-time comparison for sensitive data

## Pull Request Process

1. **Ensure All Tests Pass**
   - All existing tests must pass
   - New code must have test coverage
   - No linting errors

2. **Update Documentation**
   - Update README if needed
   - Add docstrings for new APIs
   - Update CHANGELOG.md

3. **PR Description**
   - Describe what changes you made
   - Explain why the changes are needed
   - Reference any related issues

4. **Review Process**
   - Address reviewer feedback promptly
   - Keep PR scope focused
   - Squash commits before merge if requested

## Release Process

(For maintainers)

1. Update version in `pyproject.toml` and `Cargo.toml`
2. Update `CHANGELOG.md`
3. Create release tag: `git tag -a v0.1.0 -m "Release 0.1.0"`
4. Push tag: `git push origin v0.1.0`
5. GitHub Actions will build and publish release

## Questions?

Feel free to:
- Open an issue for bugs or feature requests
- Start a discussion for questions
- Join our community chat (link TBD)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
