# Text node

Plain text content.

**HTML**: `<p>This is paragraph text.</p>`
**Markdown**: `This is paragraph text.`

## JSON parsed object

A component may have children and the data is stored in attributes in nodes.

```json
{
    "type": "p",
    "child" : []
    "markdown": "This is paragraph text.",
    "text": "This is paragraph text.",
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
    "child": {
      "type": "array",
      "items": {}
    },
    "markdown": {
      "type": "string"
    },
    "text": {
      "type": "string"
    }
  },
  "required": [
    "type",
    "child",
    "markdown",
    "text"
  ]
}
```

