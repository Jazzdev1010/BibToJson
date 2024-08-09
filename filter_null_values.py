import json

def clean_entry(entry):
    """
    Remove keys with null, empty, or whitespace-only values from a dictionary.
    """
    return {k: v for k, v in entry.items() if v not in [None, '', ' ', [], {}, ()]}

def filter_non_empty_entries(entries):
    """
    Remove entries from a list of dictionaries where all values are null or empty.
    """
    return [clean_entry(entry) for entry in entries if any(entry.values())]

def process_json(input_file, output_file):
    """
    Read JSON from input_file, clean entries, and write the result to output_file.
    """
    # Load JSON data
    with open(input_file, 'r') as json_file:
        data = json.load(json_file)
    
    # Check if the data is a list of entries
    if isinstance(data, list):
        # Clean entries and filter out empty ones
        cleaned_data = filter_non_empty_entries(data)
    else:
        raise ValueError("The input JSON file does not contain a list of entries.")
    
    # Write cleaned JSON data to the output file
    with open(output_file, 'w') as json_file:
        json.dump(cleaned_data, json_file, indent=4)
    
    print(f"Cleaned JSON file generated: {output_file}")

# Example usage
input_file = 'merged_publications.json'  # Replace with your input file path
output_file = 'Filtered_publications.json'  # Replace with your output file path

process_json(input_file, output_file)
