# construction-photo-organizer

A small Python CLI tool for organizing image files by modified date.

## Purpose

This project is a personal learning project for Python, CLI development, file operations, CSV output, testing, and GitHub publishing.

## Features

- Organize .jpg, .jpeg, and .png files
- Sort files by modified time
- Copy files to an output directory without modifying originals
- Rename files using YYYYMMDD_001.jpg format
- Output a CSV rename mapping
- Support --dry-run

## Usage

Install the project in editable mode:

```powershell
python -m pip install -e .
```

Run the command:

```powershell
photo-organizer INPUT_DIR OUTPUT_DIR
photo-organizer INPUT_DIR OUTPUT_DIR --dry-run
```

Example:

```powershell
photo-organizer data\sample_input output
photo-organizer data\sample_input output --dry-run
```

## Development setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the project in editable mode:

```powershell
python -m pip install -e .
```

Install test dependencies:

```powershell
python -m pip install pytest
```

Run tests:

```powershell
python -m pytest
```

## Notice / Disclaimer

- This repository is a personal learning project.
- This project is not related to the developer's employer, workplace, projects, or internal data.
- This repository does not use real construction site photos, company documents, client information, or internal project files.
- Use only dummy files or generated test images.
- If you use this tool in your own environment, you are responsible for testing and operation.
- The developer is not responsible for any damage caused by using this tool.
- License: MIT License.

## License

MIT License.
