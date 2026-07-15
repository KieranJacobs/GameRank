# Multi-Stage Game Data Pipeline

A lightweight, three-stage production data engineering pipeline built in Python. This project automates the process of extracting raw gaming data from an external REST API, sanitizing anomalous records, and executing structural data analysis using Pandas.

##  Architecture Overview

The pipeline is split into three decoupled operational stages:
1. **Data Ingestion (`extract.py`):** Securely connects to the RAWG API using environment configurations, handles pagination, and extracts the top 50 highest-rated games into a raw local JSON payload.
2. **Data Cleaning (`clean.py`):** Implements defensive key retrieval to parse the raw data, strips out entries with missing release dates or low Metacritic scores ($\le 75$), and exports a clean data subset.
3. **Data Analysis (`analyze.py`):** Ingests the pristine dataset into a two-dimensional Pandas DataFrame to run descriptive statistical analysis, reporting dataset volume, average ratings, and slicing top-performing records.

##  Tech Stack & Dependencies

* **Language:** Python 3.x
* **Libraries:** Pandas, Requests, Python-Dotenv
* **Environment Management:** Miniconda / Anaconda

##  Quick Start & Verification

### 1. Environment Configuration
Clone the repository and install the mandatory dependencies:
\`\`\`bash
conda install pandas requests
pip install python-dotenv
\`\`\`

Create a `.env` file in the root directory and add your secret API token:
\`\`\`text
RAWG_API_KEY=your_secret_api_key_here
\`\`\`

### 2. Execution Sequence
Run the pipeline stages sequentially from your terminal:
\`\`\`bash
python extract.py  # Generates raw_games.json (git-ignored)
python clean.py    # Generates clean_games.json (git-ignored)
python analyze.py  # Spits out summary analytics to the console
\`\`\`