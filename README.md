# PubMed Research Papers Fetcher

## Description

This Python program fetches research papers from the PubMed API based on a user-specified query. It filters the papers to identify those with at least one author affiliated with pharmaceutical or biotech companies and outputs the results as a CSV file.

## How the Code is Organized

The code is structured as follows:

1. **`main.py`**: The main entry point of the program, which handles user input, API requests, and output generation.
2. **`fetch_papers.py`**: Contains functions to interact with the PubMed API and fetch the relevant data.
3. **`output.py`**: Contains functions to handle the CSV file creation and writing results.
4. **`requirements.txt`**: Lists all the dependencies required to run the project.

## Tools and Libraries Used

- **`requests`**: For making HTTP requests to the PubMed API.
  - [requests documentation](https://docs.python-requests.org/en/master/)
- **`csv`**: For handling CSV file operations to save the fetched data.
- **`argparse`**: For command-line argument parsing.
- **`Poetry`**: For dependency management and packaging.
  - [Poetry documentation](https://python-poetry.org/)
  
Additionally, any heuristics like email addresses and domain names (e.g., words like "university", "lab") are used to filter non-academic authors.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Vipinkushuk/pubmed-research-papers.git
   cd pubmed-research-papers

2. **Install Dependencies using Poetry**:
   Make sure you have Poetry installed. Then, install the dependencies:
   ```bash
   poetry install

3. **Usage**:
   To fetch research papers, run the following command in your terminal:
   ```bash
   poetry run get-papers-list -q "<your-query>" -f "<output-file.csv>"

4. **Example**
   This will search for papers related to "cancer therapy" and save the results in cancer_papers.csv.
   ```bash
   poetry run get-papers-list -q "cancer therapy" -f "cancer_papers.csv"

   
