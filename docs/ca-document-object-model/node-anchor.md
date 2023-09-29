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
    "category" : "type-of-link",
    "markdown": "[text](URL)",
    "text": "text",
    "href": "URL"
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
    "category": {
      "type": "string"
    },
    "markdown": {
      "type": "string"
    },
    "text": {
      "type": "string"
    },
    "href": {
      "type": "string"
    }
  },
  "required": [
    "type",
    "category",
    "markdown",
    "text",
    "href"
  ]
}
```

## More nodes

[Library of attribute nodes](document-object-model.md#library-of-attribute-nodes)
