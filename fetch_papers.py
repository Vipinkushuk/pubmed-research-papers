from Bio import Entrez
import csv
import argparse

# Set up your email (required by PubMed API)
Entrez.email = "vipinkhushuk@gmail.com"  # Replace with your email

# Function to fetch papers from PubMed
def fetch_papers(query, max_results=10):
    # Step 1: Search for papers
    search_handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    search_results = Entrez.read(search_handle)
    search_handle.close()

    # Get a list of PubMed IDs (PMIDs)
    pmids = search_results["IdList"]

    if not pmids:
        print("No papers found for the query.")
        return []

    # Step 2: Fetch paper details using the PMIDs
    papers = []
    fetch_handle = Entrez.efetch(db="pubmed", id=",".join(pmids), retmode="xml")
    fetch_results = Entrez.read(fetch_handle)
    fetch_handle.close()

    for paper in fetch_results["PubmedArticle"]:
        pubmed_id = paper["MedlineCitation"]["PMID"]
        title = paper["MedlineCitation"]["Article"]["ArticleTitle"]
        pub_date = paper["MedlineCitation"]["Article"]["Journal"]["JournalIssue"]["PubDate"]

        authors = paper["MedlineCitation"]["Article"]["AuthorList"]

        # Filter non-academic authors
        non_academic_authors = []
        company_affiliations = []
        corresponding_author_email = None

        for author in authors:
            if "AffiliationInfo" in author:
                affiliation = author["AffiliationInfo"][0]["Affiliation"]
                if "pharma" in affiliation.lower() or "biotech" in affiliation.lower():
                    non_academic_authors.append(author["ForeName"] + " " + author["LastName"])
                    company_affiliations.append(affiliation)
                if "CorrespondingAuthor" in author.get("Identifier", {}):
                    corresponding_author_email = author["Identifier"]

        papers.append({
            "PubmedID": pubmed_id,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": ", ".join(non_academic_authors),
            "Company Affiliation(s)": ", ".join(company_affiliations),
            "Corresponding Author Email": corresponding_author_email
        })

    return papers

# Function to save the papers to a CSV file
def save_to_csv(papers, filename):
    keys = papers[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(papers)

if __name__ == "__main__":
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", help="The query to search for papers.")
    parser.add_argument("-f", "--file", help="The output CSV file to save the results.", default=None)
    args = parser.parse_args()

    # Fetch papers using the provided query
    papers = fetch_papers(args.query)

    if papers:
        if args.file:
            save_to_csv(papers, args.file)
            print(f"Papers saved to {args.file}")
        else:
            # Print results if no file provided
            for paper in papers:
                print(paper)
    else:
        print("No papers found or no non-academic authors detected.")
