# Text node

Plain text content.

**HTML**: `<p>This is paragraph text.</p>`
**Markdown**: `This is paragraph text.`

## JSON parsed object

A component may have children and the data is stored in attributes in nodes.

```json
{
    "type": "p",
    "id": "guid",
    "attributes": [
        {
            "markdown": "markdown"
        },
        {
            "text": "text-only"
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
            "enum": ["p"]
        },
        "id": {
            "type": "string",
            "pattern": "^[a-zA-Z0-9-]+$"
        },
        "attributes": {
            "type": "array",
            "items": {
                "type": "object",
                "minProperties": 1,
                "properties": {
                    "markdown": {
                        "type": "string"
                    },
                    "text": {
                        "type": "string"
                    }
                },
                "additionalProperties": false
            }
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

