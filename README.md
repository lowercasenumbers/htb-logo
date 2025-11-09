# HTB Logo Fetcher

A simple command-line tool to fetch logo URLs for HackTheBox machines.

## Features

- Fetch machine logo URLs by machine name
- Simple command-line interface
- Handles relative and absolute URLs automatically

## Requirements

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended)

## Installation

### Using uv (recommended)

Install directly from the repository:

```bash
uv tool install git+https://github.com/lowercasenumbers/htb-logo.git
```

Or install from a local clone:

```bash
git clone git@github.com:lowercasenumbers/htb-logo.git
cd htb-logo
uv tool install .
```

Or install in development mode:

```bash
uv pip install -e .
```

### Traditional pip installation

```bash
pip install -r requirements.txt
```

## Usage

**Note:** The Python module file is named `htb_logo.py` (with underscore), but the installed command-line tool is named `htb-logo` (with hyphen). This follows Python naming conventions.

After installation with `uv tool install`, you can run:

```bash
htb-logo <machine_name>
```

Or run directly without installation:

```bash
uv run htb_logo.py <machine_name>
```

Or with Python:

```bash
python3 htb_logo.py <machine_name>
```

### Examples

```bash
# Fetch logo URL for "Lame" machine
htb-logo Lame

# Fetch logo URL for "Bashed" machine
htb-logo Bashed
```

The tool will output the logo URL to stdout if found, or an error message to stderr if not found.

## Development

### Setup development environment

```bash
# Create virtual environment and install dependencies
uv venv
uv pip install -e .
```

### Running tests

```bash
uv run python3 htb_logo.py Lame
```

## Dependencies

- `requests>=2.31.0` - HTTP library for fetching web pages
- `beautifulsoup4>=4.12.0` - HTML parsing library

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Author
lowercasenumbers
