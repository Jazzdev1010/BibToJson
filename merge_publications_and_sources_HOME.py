import json

# File paths
publications_file = 'type4_publications.json'
sources_file = 'type4_urls.json'
output_file = 'type4_merged_publications.json'

# Load JSON data from publications.json
with open(publications_file, 'r') as file:
    publications = json.load(file)

# Load JSON data from sources.json
with open(sources_file, 'r') as file:
    sources = json.load(file)

# Create a dictionary for sources with ID as the key
sources_dict = {entry['ID']: entry for entry in sources}

# Merge publications with sources
for publication in publications:
    publication['topic']="type4" ## get_topic_type(filename) "type1.json" type2.json
    publication_id = publication['ID']
    if publication_id in sources_dict:
        # Add all fields from sources.json to the publication
        publication.update(sources_dict[publication_id])

# Write the merged data to a new JSON file
with open(output_file, 'w') as file:
    json.dump(publications, file, indent=2)

print(f"Merged JSON file generated: {output_file}")
