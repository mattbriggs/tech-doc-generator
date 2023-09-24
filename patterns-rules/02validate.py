import jsonschema
import json

# Step 1: Obtain the JSON schema
json_schema_string = '''{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "tagName": { "type": "string" },
    "attributes": {
      "type": "object",
      "additionalProperties": { "type": "string" }
    },
    "children": {
      "type": "array",
      "items": { "$ref": "#" }
    },
    "textContent": { "type": "string" }
  },
  "required": ["tagName"],
  "additionalProperties": false
}'''

json_schema = json.loads(json_schema_string)

# Step 2: Load the JSON document
json_document_string = '''{ "content": "<p>title: string\ndescription: string
\nauthor: string\nms-author: string\nms-service: string\nms-topic:
string\nms-date: string\nms-custom:
string</p>\n<h1>[H1 heading here]</h1>\n<p>[add your introductory paragraph]</p>\n<h2>[Section 1 heading]</h2>\n<h2>[Section 2 heading]</h2>\n<h2>[Section n heading]</h2>\n<h2>Next
steps</h2>\n<ul>\n<li><a href=\"article-concept.md\">Write
concepts</a></li>\n<li><a  
href=\"../contribute/links-how-to.md\">Links</a></li>\n</ul>"
}'''

json_document = json.loads(json_document_string)

# Step 3: Validate the JSON document against the JSON schema
try:
    jsonschema.validate(json_document, json_schema)
    print("JSON document is valid.")
except jsonschema.ValidationError as e:
    print("JSON document is not valid.")
    print(e.message)  # Validation error message