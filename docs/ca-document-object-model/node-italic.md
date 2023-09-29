# Italic

Italic text.

**HTML**: `<i>text</i>`  
**Markdown**: `*text*` or `_text_`

## JSON parsed object

A component may have children and the data is stored in attributes in nodes.

```json
{
    "type": "italic",
    "markdown": "*text*",
    "text": "text"
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
    }
  },
  "required": [
    "type",
    "markdown",
    "text"
  ]
}
```

## More nodes

[Library of attribute nodes](document-object-model.md#library-of-attribute-nodes)