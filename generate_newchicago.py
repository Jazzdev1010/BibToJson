import json
from jinja2 import Environment, FileSystemLoader

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

def clean_entry(entry):
    # Remove keys with null, empty, or whitespace-only values
    return {k: v for k, v in entry.items() if v not in [None, '', ' ', [], {}, ()]}

# Remove entries where all values are null or empty
def filter_non_empty_entries(entries):
    return [clean_entry(entry) for entry in entries if any(entry.values())]

# Define input and output file paths
input_json_file = 'merged_publications.json'
output_html_file = 'modified_publications.html'

# Load JSON data
with open(input_json_file, 'r') as json_file:
    entries = json.load(json_file)

# Clean author names and remove null or empty fields
for entry in entries:
    if 'author' in entry and entry['author']:
        entry['author'] = clean_authors_name(entry['author'])

# Remove entries with null or empty values and keys with null values
entries = filter_non_empty_entries(entries)

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('new_jinja_chicago.jinja2')

# Render the template with the entries
output = template.render(entries=entries)

# Save the rendered template to a new HTML file
with open(output_html_file, 'w') as html_file:
    html_file.write(output)

print(f"HTML file generated: {output_html_file}")
