# Paragraph

Content blocks that contains text elements are natural language parts that can be understood by a person reading the text. Text elements are not structured using purely prescriptive models, however they can be parsed into programmatic representations using a variety of techniques. NLP processing creates a syntactical model that contains attributes such a part of speech, entity recognition, sentence recognition, and so on. Vector representations convert text, sentences, and so on into a numeric coordinates. The purpose of text is to communicate information to a human reader. Textual superstructures such as modality organize text chunks with specific purposes to accomplish more complex information tasks such as teaching a reader skill or presenting information for a reader to accomplish a task.

Text refers to the primary content in any written communication. In digital media, it's the sequence of words, sentences, and paragraphs that convey information or a message to the reader.

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

## More components

[Library of components](document-object-model.md#library-of-defined-components-in-the-ca-object-model)