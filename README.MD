# DLIS File Processing Suite

## Overview
The DLIS File Processing Suite is a Python-based tool designed for the efficient handling and analysis of Digital Log Interchange Standard (DLIS) files, commonly used in the oil and gas industry for well log data. This suite provides a set of tools for extracting metadata, processing frames, and summarizing the contents of .dlis files.

## Features
- BeloFastFrame: Represents and processes individual frames in a DLIS file, extracting channel and index information.
- BeloDlisFast: Aggregates multiple BeloFastFrame instances, facilitating batch processing of frames from DLIS files.
- DlisFileWrapper: Wraps a DLIS file, storing metadata and error details for easy access and analysis.
- SingleBeloProcessor: Provides static methods for loading DLIS files into DlisFileWrapper objects and generating BeloDlisFast objects for comprehensive file analysis.
- General File Information Extraction: A utility function to extract general information from all .dlis files in a directory and save it as a JSON file.

## Installation
To install the DLIS File Processing Suite, clone the repository and install the required dependencies:

```bash
git clone 
cd DLIS-File-Processing-Suite
pip install -r requirements.txt
```

## Usage

### Processing DLIS Files
Load a DLIS file into a wrapper:

```python	
dlis_wrapper = SingleBeloProcessor.load_dlis_wrapper('path/to/file.dlis')
```

### Generate a report from the DLIS file:

```python	
report = SingleBeloProcessor.create_fast_report(dlis_wrapper)
```