# CSV Health Inspector

A small Python project built to learn object-oriented programming and understand how files, classes, and functions connect. This repo inspects CSV data, reports dataset health, and exposes a simple FastAPI endpoint to analyze uploaded files.

## Project Overview

CSV Health Inspector is designed as a learning project for OOP and file interaction. It loads dataset files, inspects structure and missing values, and generates a report that helps verify data quality quickly.

## Motivation

The primary goal of this project is to practice OOP concepts and understand the relationship between modules:

- how a loader loads data,
- how an analyzer class encapsulates inspection logic,
- how a FastAPI app ties everything together,
- and how a script can generate a report artifact.

This was built to learn how classes and functions interconnect across files and to build a working data inspection flow.

## Architecture and File Map

- `app.py`
  - FastAPI application with endpoints:
    - `GET /` for a health message
    - `POST /analyze` for file analysis
  - Uses `load_data()` and `CSVInspector`

- `loader.py`
  - Contains `load_data(file_path)`
  - Loads CSV and XLSX files from a FastAPI `UploadFile`

- `analyzer.py`
  - Contains `CSVInspector` class
  - Provides methods for dataset health checks and report generation

- `inspector.py`
  - Script entry point for local report generation
  - Loads `IPL_Matches_2008_2022.csv`
  - Writes `report.txt`

- `IPL_Matches_2008_2022.csv`
  - Example dataset used by the script

- `report.txt`
  - Generated output artifact created by `inspector.py`

## OOP Design

The main object-oriented element is the `CSVInspector` class in `analyzer.py`.

### `CSVInspector`

Responsibilities:
- store dataset state (`self.data`, `self.rows`, `self.cols`)
- inspect dataset shape
- identify missing values
- count duplicate rows
- classify column data types
- detect suspicious columns with a large number of nulls
- generate a combined text report

### Why this structure works

- `loader.py` handles input and file loading concerns.
- `analyzer.py` handles inspection logic and report assembly.
- `app.py` handles API request/response flow.
- `inspector.py` handles command-line/script execution and artifact creation.

This separation keeps responsibilities clear and makes the project easier to expand.

## Installation

1. Install Python 3.9+.
2. Install dependencies:

```bash
pip install pandas fastapi uvicorn openpyxl
```

3. Place `IPL_Matches_2008_2022.csv` in the project folder.

## Usage

### Run the API

```bash
uvicorn app:app --reload
```

Then visit:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/docs` for interactive Swagger UI

### Analyze a file via API

Send a `POST` request to `/analyze` with a file upload.

#### Example using `curl`

```bash
curl -X POST "http://127.0.0.1:8000/analyze" \
  -F "file=@IPL_Matches_2008_2022.csv"
```

#### Example response

```json
{
  "filename": "IPL_Matches_2008_2022.csv",
  "shape": "✓ Shape: 1234 rows, 20 columns",
  "missing": "✓ Missing values: column1(2.345%), column2(0.123%)",
  "duplicates": "✓ Duplicates: 5 rows",
  "dtypes": "✓ Dtypes: 12 numeric, 8 categorical",
  "suspicious": "✓ Suspicious values: important_column(315 rows are null)"
}
```

### Generate a local report

Run the inspector script:

```bash
python inspector.py
```

This reads `IPL_Matches_2008_2022.csv`, inspects the dataset, and writes the summary to `report.txt`.

## Generated Artifacts

- `report.txt`
  - Contains the combined inspection results from `CSVInspector.generate_report()`
- API response JSON
  - Provides dataset health details for uploaded files

## Supported File Formats

The loader supports:

- `.csv`
- `.xlsx`

If a different file type is provided, a `ValueError` is raised.

## Notes and Extension Ideas

This project is a good foundation for further OOP and data pipeline learning. Possible extensions:

- add column-level summary statistics
- include categorical value distributions
- support more file formats like JSON and Parquet
- add validation rules for specific datasets
- implement a web UI for file uploads
- improve error handling and response messages

## Summary

`CSV Health Inspector` is a beginner-friendly OOP project that demonstrates how loading, analysis, and reporting can be organized into separate modules. It is useful for learning modular design, clean separation of concerns, and how classes and functions work together in Python.
