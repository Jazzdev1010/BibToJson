import json

# File paths
publications_file = 'all_merged_publications.json'
output_file = 'cleaned_merged_publications.json'

# Function to clean and format author names
def clean_authors_name(authors):
    # Split authors string by 'and'
    authors_list = [author.strip() for author in authors.split('and') if author.strip()]
    
    # Reverse the author names for each split section
    cleaned_authors = [" ".join(author.strip().split(',')[::-1]) for author in authors_list]
    
    # Join authors with ', ' and add 'and' before the last author
    if len(cleaned_authors) > 1:
        formatted_authors = ', '.join(cleaned_authors[:-1]) + ' and ' + cleaned_authors[-1]
    else:
        formatted_authors = cleaned_authors[0] if cleaned_authors else ''
    
    return formatted_authors

# Function to clean individual entries by removing keys with null or empty values
def clean_entry(entry):
    return {k: v for k, v in entry.items() if v not in [None, '', [], {}, ()]}

# Function to remove entries where all values are null or empty
def filter_non_empty_entries(entries):
    return [clean_entry(entry) for entry in entries if any(entry.values())]

# Load JSON data
with open(publications_file, 'r') as json_file:
    entries = json.load(json_file)

# Clean author names and remove null or empty fields
for entry in entries:
    if 'author' in entry and entry['author']:
        entry['author'] = clean_authors_name(entry['author'])

# Remove entries with null or empty values and keys with null values
entries = filter_non_empty_entries(entries)

# Write the cleaned data to a new JSON file
with open(output_file, 'w') as json_file:
    json.dump(entries, json_file, indent=2)

print(f"Clean JSON file generated: {output_file}")
