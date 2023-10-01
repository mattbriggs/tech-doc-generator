# Italic

Italic text.

**HTML**: `<i>text</i>`  
**Markdown**: `*text*` or `_text_`

## JSON parsed object

A component may have children and the data is stored in attributes in nodes.

```json
{
    "type": "italic",
    "id": "guid",
    "attributes": [
        {
            "markdown": "*text*"
        },
        {
            "text": "text"
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
            "enum": ["span"]
        },
        "id": {
            "type": "string",
            "pattern": "^[a-zA-Z0-9-]+$"
        },
        "attributes": {
            "type": "array",
            "minItems": 2,
            "items": [
                {
                    "type": "object",
                    "required": ["markdown"],
                    "properties": {
                        "markdown": {
                            "type": "string",
                            "pattern": "^:::.*:::$"
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