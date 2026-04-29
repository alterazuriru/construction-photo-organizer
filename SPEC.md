# SPEC

## Purpose

This is a small CLI tool for organizing image files by modified date.

It is built as a personal learning project for Python, file operations, CSV output, testing, and GitHub publishing.

This project does not use real construction site photos, company data, internal documents, or confidential information.

## Scope

### Input

- A local input directory
- Image files with the following extensions:
  - .jpg
  - .jpeg
  - .png

### Output

- A separate output directory
- Copied image files renamed by modified date
- A CSV file containing the rename mapping

### Sort rule

Files are sorted by:

1. Modified time
2. Original file name

### Rename rule

New file name format:

YYYYMMDD_001.jpg
YYYYMMDD_002.jpg

Numbering resets by date.

### CSV columns

- original_name
- new_name
- modified_time
- output_path

## CLI

photo-organizer INPUT_DIR OUTPUT_DIR
photo-organizer INPUT_DIR OUTPUT_DIR --dry-run

## Safety rules

- Original files are never modified.
- Files are copied to the output directory.
- Real work data, construction site photos, company documents, and confidential files must not be used.
- This is a personal learning project.

## Out of scope for v1

- EXIF support
- GUI
- Web app
- AI image recognition
- OCR
- Excel photo ledger generation
- Cloud sync
- User accounts
