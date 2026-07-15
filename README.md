# Multi-Stage Game Data Pipeline

A beginner-friendly Python project that demonstrates a simple ETL/data pipeline. It pulls game data from the RAWG API, stores the raw results locally as JSON, filters the data by basic quality rules, and performs simple analysis with Pandas.

## Architecture Overview

This project was built as a small solo learning exercise to practice working with real data from start to finish. The workflow is split into three simple stages:

1. **Data Ingestion (`extract.py`):** Connects to the RAWG API using environment variables, requests the top 50 highest-rated games, and saves the raw results to a local JSON file.
2. **Data Cleaning (`clean.py`):** Reads the raw JSON data and keeps only records with a release date and a Metacritic score of 75 or higher.
3. **Data Analysis (`analyze.py`):** Loads the cleaned data into a Pandas DataFrame and prints summary information such as record count, average Metacritic score, and the highest-rated game.

## Tech Stack & Dependencies

* **Language:** Python 3.x
* **Libraries:** Pandas, Requests, Python-Dotenv
* **Environment Management:** Miniconda / Anaconda

## Quick Start & Verification

### 1. Environment Configuration
Clone the repository and install the required dependencies:

`\`\`bash
conda install pandas requests
pip install python-dotenv
`\`\`

Create a `.env` file in the root directory and add your RAWG API key:
`\`\`text
RAWG_API_KEY=your_api_key_here
\`\`\`

### 2. Execution Sequence
Run the pipeline steps from your terminal:
\`\`\`bash
python extract.py # Generates raw_games.json
python clean.py # Generates clean_games.json
python analyze.py # Prints summary analytics to the console
\`\`\`