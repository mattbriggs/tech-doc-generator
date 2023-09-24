import sys
from rdflib import Graph
import json

def owl_to_json_schema(owl_filename, output_filename):
    g = Graph()
    g.parse(owl_filename, format="xml")

    # Define a simple JSON Schema template
    json_schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "content-object",
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

    print("Done!")