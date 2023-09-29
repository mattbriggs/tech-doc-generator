# Image

Image.

**HTML**: `<img src="URL" alt = "alt-text">  
**Markdown**: `![alt-text](URL)`

## JSON parsed object

A component may have children and the data is stored in attributes in nodes.

```json
{
    "type": "image",
    "markdown": "![alt-text](URL)",
    "text": "alt-text",
    "source": "URL"
}
```

## JSON Schema for a parsed object

A JSON Schema provides a contract for the JSON data required by a given application and how that JSON data should be structured. It describes the structure of the JSON data, specifying what properties are required, the types of values, and more.

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "type": {
      "type": "string"
    },
    "markdown": {
      "type": "string"
    },
    "text": {
      "type": "string"
    },
    "source": {
      "type": "string"
    }
  },
  "required": [
    "type",
    "markdown",
    "text",
    "source"
  ]
}
```

## More nodes

[Library of attribute nodes](document-object-model.md#library-of-attribute-nodes)