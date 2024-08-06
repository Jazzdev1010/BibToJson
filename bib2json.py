import json
import bibtexparser

# Define input and output file paths
input_bib_file = 'type4_bib.bib'
output_json_file = 'type4_publications.json'

# Read the BibTeX file
with open(input_bib_file, 'r') as bib_file:
    bibtex_str = bib_file.read()

# Parse the BibTeX entries
bib_database = bibtexparser.loads(bibtex_str)

# Extract the entries
bib_entries = bib_database.entries

# Convert to JSON
bib_json = json.dumps(bib_entries, indent=2)

# Write to JSON file
with open(output_json_file, 'w') as json_file:
    json_file.write(bib_json)

print(f"JSON file generated: {output_json_file}")
