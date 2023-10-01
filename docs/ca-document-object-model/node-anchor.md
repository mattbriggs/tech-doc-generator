# Anchor

Anchor (Hyperlink). Defines a hyperlink.

**HTML**: `<a href="URL">text</a>`  
Markdown `[text](URL)`

A link can be categorized into the following types:

| Type | Example | Description |
| --- | --- | --- |
|    |    |     |
|    |    |     |
|    |    |     |

    "type": "name",
## JSON parsed object

A component may have children and the data is stored in attributes in nodes.

```json
{
    "type": "anchor",
    "id": "guid",
    "attributes": [
        {
            "markdown": "[text](URL)"
        },
        {
            "text": "text"
        },
        {
            "href": "URL"
        },
        {
            "category": "type-of-link"
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
            "enum": ["anchor"]
        },
        "id": {
            "type": "string",
            "pattern": "^[a-zA-Z0-9-]+$"
        },
        "attributes": {
            "type": "array",
            "minItems": 4,
            "maxItems": 4,
            "items": [
                {
                    "type": "object",
                    "required": ["markdown"],
                    "properties": {
                        "markdown": {
                            "type": "string",
                            "pattern": "^\\[.*\\]\\(.*\\)$"
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
                    "required": ["href"],
                    "properties": {
                        "href": {
                            "type": "string",
                            "format": "uri"
                        }
                    },
                    "additionalProperties": false
                },
                {
                    "type": "object",
                    "required": ["category"],
                    "properties": {
                        "category": {
                            "type": "string",
                            "enum": ["type-of-link", "type1", "type2", "type3"]
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
