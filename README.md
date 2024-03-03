# XML Sitemap Post Name Extractor

This script is designed to extract post names from XML sitemaps. It provides an option to download the sitemap directly from a URL or use a locally available sitemap file. The extracted post names are then saved to a text file.

## Purpose

The script is useful for SEO analysts, webmasters, or developers who need to quickly extract post names from a sitemap without manually parsing the XML. It can be used to audit, analyze, or troubleshoot the contents of a website's sitemap.

## How to Use

### Prerequisites

- Python 3.x installed on your system.
- `requests` library installed. If not already installed, you can install it using pip:

```bash
pip install requests
```

## Running the Script

### Clone the repository or download the script

First, you need to have the script on your local machine. If it's hosted on a repository, you can clone it using git or simply download the script file.

### Navigate to the script directory

Open a terminal (Linux) or command prompt/PowerShell (Windows) and navigate to the directory where the script is located.

```bash
cd path/to/script
```

### Run the script

Execute the script using Python.
On Linux:

```bash
python3 sitemap_extractor.py
```

On Windows:

```bash
python sitemap_extractor.py
```

### Follow the prompts

The script will ask if you want to download a sitemap. Type yes (or y) and provide the URL to download and process the sitemap. If you type no (or n), the script will list all the XML files in the current directory for you to choose from for processing.

## Output
The script will save the extracted post names to a file named _heist.txt_ in the same directory as the script.

## Compilation
No compilation is needed as this is a Python script. You just need to ensure Python is installed and run the script as mentioned above.
