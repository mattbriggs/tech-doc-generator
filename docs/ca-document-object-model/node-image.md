# Image

Image.

**HTML**: `<img src="URL" alt = "alt-text">  
**Markdown**: `![alt-text](URL)`

For more information about HTML Images Syntax [see W3](https://www.w3schools.com/html/html_images.asp).

## JSON parsed object

A component may have children and the data is stored in attributes in nodes.

```json
{
    "type": "image",
    "id": "guid",
    "attributes": [
        {
            "markdown": "![alt-text](URL)"
        },
        {
            "text": "alt-text"
        },
        {
            "source": "URL"
        }
    ],
    "child": []
}
```

## JSON Schema for a parsed object

A JSON Schema provides a contract for the JSON data required by a given application and how that JSON data should be structured. It describes the structure of the JSON data, specifying what properties are required, the types of values, and more.

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": ["type", "id", "attributes", "child"],
    "properties": {
        "type": {
            "type": "string",
            "enum": ["image"]
        },
        "id": {
            "type": "string",
            "pattern": "^[a-zA-Z0-9-]+$"
        },
        "attributes": {
            "type": "array",
            "minItems": 3,
            "items": [
                {
                    "type": "object",
                    "required": ["markdown"],
                    "properties": {
                        "markdown": {
                            "type": "string",
                            "pattern": "^!\\[.*\\]\\(.*\\)$"
                        }
                    },
                    "additionalProperties": false
                },
                {
                    "type": "object",
                    "required": ["text"],
                    "properties": {
                        "text": {
                            "type": "string"
                        }
                    },
                    "additionalProperties": false
                },
                {
                    "type": "object",
                    "required": ["source"],
                    "properties": {
                        "source": {
                            "type": "string",
                            "format": "uri"
                        }
                    },
                    "additionalProperties": false
                }
            ]
        },
        "child": {
            "type": "array",
            "items": {
                "type": "object"
            }
        }
    },
    "additionalProperties": false
}

```

## More nodes

[Library of attribute nodes](document-object-model.md#library-of-attribute-nodes)