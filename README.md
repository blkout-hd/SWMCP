# SWMCP - High-Performance MCP Server

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Rust 1.70+](https://img.shields.io/badge/rust-1.70+-orange.svg)](https://www.rust-lang.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A production-grade fastmcp 3.2 port of [DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) with enterprise security, CUDA acceleration, and multiagent orchestration.

## Features

### 🚀 Performance
- **Rust Extensions**: 7-21x speedup for CPU-intensive operations via PyO3
- **CUDA Green Contexts**: Parallel GPU acceleration for file processing
- **Intel MKL**: Optimized numerical operations for data pipelines
- **Work-Stealing Scheduler**: Efficient parallel task execution

### 🔒 Security
- **Post-Quantum Cryptography**: ML-KEM/ML-DSA algorithms
- **TPM 2.0 Integration**: Hardware-backed authentication (default)
- **RSA-512 + HMAC**: Fallback authentication mode
- **OAuth 2.1**: Multiple provider support (GitHub, Google, Azure, AWS)
- **Encrypted Storage**: Fernet encryption for all persistent data

### 🤖 Multiagent Orchestration
- **LangGraph**: Graph-based agent coordination
- **StateGraph**: Persistent context across agent invocations
- **Conditional Routing**: Dynamic workflow adaptation
- **Fault Tolerance**: Replay and recovery capabilities

### 📊 Observability
- **MCP Apps GUI**: Browser-based monitoring dashboard
- **OpenTelemetry**: Comprehensive instrumentation
- **Real-time Metrics**: Resource utilization tracking
- **Process Monitoring**: Terminal session replay

### 🛠️ Core Capabilities
- Terminal operations (SSH, REPL, interactive shells)
- File editing with surgical diff/patch operations
- Process management and monitoring
- Cross-platform file system operations
- Binary file processing and format detection

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    FastMCP Server                        │
│  (Python 3.10+ with async/await, decorators)           │
└────────────────┬────────────────────────────────────────┘
                 │
    ┌────────────┴────────────┬──────────────┬────────────┐
    │                         │              │            │
┌───▼────┐              ┌────▼─────┐   ┌───▼────┐  ┌───▼─────┐
│  Rust  │              │ LangGraph│   │  CUDA  │  │ Storage │
│Extension│             │   Agent  │   │ Green  │  │ (Redis) │
│ (PyO3) │              │Orchestr. │   │Context │  │Encrypted│
└────────┘              └──────────┘   └────────┘  └─────────┘
    │                         │              │            │
    │                         │              │            │
┌───▼────────────────────────▼──────────────▼────────────▼───┐
│  Diff/SSH/Terminal    Workflow Coord    Parallel Ops  State│
└─────────────────────────────────────────────────────────────┘
```

## Quick Start

### Prerequisites

- Python 3.10 or higher
- Rust 1.70 or higher (for building extensions)
- CUDA 13.2+ (optional, for GPU acceleration)
- Redis (optional, for distributed deployment)
- TPM 2.0 hardware or tpm2-simulator (for TPM auth)

### Installation

```bash
# Clone the repository
git clone https://github.com/blkout-hd/SWMCP.git
cd SWMCP

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"

# Build Rust extension
maturin develop --release

# Run tests
pytest
```

### Configuration

Create `.env` file:

```env
# Authentication (choose one)
AUTH_MODE=tpm  # or 'rsa-hmac'

# OAuth (if using OAuth instead)
GITHUB_CLIENT_ID=your_client_id
GITHUB_CLIENT_SECRET=your_client_secret
JWT_SIGNING_KEY=your_jwt_key

# Storage
STORAGE_ENCRYPTION_KEY=your_fernet_key
REDIS_URL=redis://localhost:6379

# CUDA (optional)
CUDA_VISIBLE_DEVICES=0
CUDA_GREEN_CONTEXT_SMS=16

# Intel MKL (optional)
MKL_NUM_THREADS=8
```

### Running the Server

```bash
# Start MCP server
python -m swmcp.server

# With debug logging
PYTHONDEVMODE=1 python -m swmcp.server --debug

# Open observability GUI
python -m swmcp.gui
```

## Project Structure

```
SWMCP/
├── swmcp/
│   ├── server/           # FastMCP server implementation
│   ├── agents/           # LangGraph agent definitions
│   ├── tools/            # MCP tool implementations
│   ├── auth/             # Authentication providers
│   ├── storage/          # Database backends
│   └── gui/              # Observability dashboard
├── swmcp_rs/             # Rust extension module
│   ├── src/
│   │   ├── diff.rs       # Fast diff algorithms
│   │   ├── ssh.rs        # SSH client implementation
│   │   ├── terminal.rs   # Terminal emulation
│   │   └── lib.rs        # PyO3 bindings
│   └── Cargo.toml
├── tests/                # Integration tests
├── docs/                 # Documentation
├── pyproject.toml        # Python project config
├── Cargo.toml            # Rust workspace config
└── README.md
```

## Development

### Building Rust Extension

```bash
# Development build (faster compilation)
maturin develop

# Release build (optimized)
maturin develop --release

# Build wheel for distribution
maturin build --release
```

### Running Tests

```bash
# Python tests
pytest tests/

# Rust tests
cd swmcp_rs && cargo test

# Integration tests
pytest tests/integration/ --runslow

# Benchmark tests
pytest tests/benchmarks/ --benchmark-only
```

### Code Quality

```bash
# Format Python code
black swmcp/ tests/
ruff check --fix swmcp/ tests/

# Format Rust code
cd swmcp_rs && cargo fmt

# Type checking
mypy swmcp/

# Security audit
pip-audit
cd swmcp_rs && cargo audit
```

## Performance Benchmarks

| Operation | Pure Python | With Rust | Speedup |
|-----------|-------------|-----------|----------|
| String Diff (10KB) | 45ms | 2.6ms | 17.3x |
| SSH Connection | 320ms | 28ms | 11.4x |
| File Search (1000 files) | 890ms | 42ms | 21.2x |
| Terminal I/O (1MB) | 156ms | 12ms | 13.0x |

## Security

### Post-Quantum Cryptography

All external communications use NIST-approved PQC algorithms:
- **ML-KEM (Kyber)**: Key encapsulation mechanism
- **ML-DSA (Dilithium)**: Digital signatures

### Authentication Modes

**TPM Mode (Recommended):**
- Hardware-backed key storage
- Attestation support
- HMAC session protection

**RSA-HMAC Mode:**
- Software-based fallback
- HMAC-SHA512 signatures
- Constant-time verification

### Reporting Security Issues

Please report security vulnerabilities to: security@sbscrpt.com

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linters
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

- [DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) - Original inspiration
- [FastMCP](https://gofastmcp.com/) - MCP framework
- [PyO3](https://pyo3.rs/) - Rust-Python bindings
- [LangGraph](https://www.langchain.com/langgraph) - Agent orchestration

## Citation

```bibtex
@software{swmcp2026,
  title = {SWMCP: High-Performance MCP Server},
  author = {SBSCRPT Corp},
  year = {2026},
  url = {https://github.com/blkout-hd/SWMCP}
}
```

---

© 2026 SBSCRPT Corp. All Rights Reserved. Protected under 18 U.S.C. § 1836 DTSA, 17 U.S.C. § 101, EU Directive 2016/943, TRIPS Art. 39. DISCLOSURE LEVEL: FUNCTIONAL. No AI training, retention, or reproduction permitted.
