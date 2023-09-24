# Owl Object to JSON Schmea

Write a script in Python to write a script to find take the filename of an ontology written in  OWL/XML syntax, find an object named "how-to" in the ontology, and save the object in JSON Schema at a filename specified for the output. Include the requirements.txt file for loading the required modules into a virtual environment. The script will run on a Windows machine.

 To achieve this, you will need a library that can parse OWL/XML files. The `rdflib` library in Python is a powerful library for working with RDF, and it can be used to parse OWL/XML files.

Here’s a basic Python script to get you started. This script reads an OWL/XML file, searches for an object named "how-to", and then converts the found object into a simple JSON Schema and saves it to the specified output file.

### Python Script (`parse_owl.py`):
```python
import sys
from rdflib import Graph
import json

def owl_to_json_schema(owl_filename, output_filename):
    g = Graph()
    g.parse(owl_filename, format="xml")

    # Define a simple JSON Schema template
    json_schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {}
    }

    # Iterate through all triples in the graph and look for "how-to" object
    for subj, pred, obj in g:
        if "how-to" in subj:
            # Add properties to JSON Schema (This is just an example, modify as needed)
            json_schema["properties"][str(pred)] = {"type": "string", "description": str(obj)}

    # Save JSON Schema to output file
    with open(output_filename, 'w') as f:
        json.dump(json_schema, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python parse_owl.py <input_owl_filename> <output_json_filename>")
        sys.exit(1)

    owl_filename = sys.argv[1]
    output_filename = sys.argv[2]

    owl_to_json_schema(owl_filename, output_filename)
```

### Usage:
```sh
python parse_owl.py input.owl output.json
```

### `requirements.txt`:
```
rdflib==6.0.1
```

### Instructions:

1. Create a virtual environment:
   ```sh
   python -m venv venv
   ```

2. Activate the virtual environment:
   ```sh
   .\venv\Scripts\activate
   ```

3. Install the requirements:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the script with the input OWL file and the desired output JSON file:
   ```sh
   python parse_owl.py input.owl output.json
   ```

### Note:
This is a very basic example. The conversion from OWL to JSON Schema can be complex, depending on the OWL constructs used, and you might need to adjust the script accordingly to fit the actual structure and requirements of your ontology and desired JSON Schema.