import json
from jinja2 import  Environment, FileSystemLoader

def clean_authors_name(authors):
    authors = authors.split('and')
    print(authors)
    cleaned_authors=[" ".join(author.strip().split(',')[::-1]) for author in authors] 
    return ",".join(cleaned_authors)

# Define input and output file paths
input_json_file = 'merged_publications.json'
output_html_file = 'publications.html'

# Load JSON data
with open(input_json_file, 'r') as json_file:
    entries = json.load(json_file)
    
for entry in entries:
    authors = entry['author'] 
    cleaned_authors = clean_authors_name(authors)
    entry['author']   =cleaned_authors
    

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('chicago_template.jinja2')

# Render the template with the entries
output = template.render(entries=entries)

# Save the rendered template to a new HTML file
with open(output_html_file, 'w') as html_file:
    html_file.write(output)

print(f"HTML file generated: {output_html_file}")
