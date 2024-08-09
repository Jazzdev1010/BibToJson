## Working of programs.

### 1. bib2json.py:

#### BibTeX is a standard format for bibliographic references. The code would parse a BibTeX file, extracting information like author, title, year, and publication details.

### 2. clean_json_pub.py;

#### The extracted bibliographic data from json file generated from bib2json.py. THis code cleans null values and generate a new Json file.

### 3. generate_newchicago.py:

#### It takes cleaned json file as input and use jinja2 to design the template for the Chicago format. After a new chicago format is generated a HTML file to display the publications.
