# Header

Heading elements are used to define headings in HTML. They range from` <h1>` to` <h6>`, with `<h1> `representing the highest (or most important) level and `<h6>` the lowest (or least important) level.

## Diagram

The following diagram displays the set of possible sub-elements of the component.

```mermaid
classDiagram
    class Heading {
        +Enum level
        +String content
    }
    class Enum {
        +1
        +2
        +3
        +4
        +5
        +6
    }
    Heading --> Enum

```

## Example markdown

The following markdown is an example of the artifact in a file.

```md
# Heading
```

## JSON parsed object

The following JSON represents the attributes of a parsed artifact.

```json
{
    "type": "header",
    "id": "guid",
    "attributes": [
        {   "level": "1"
        },
        {
            "markdown": "# Title text for the header"
        },
        {
            "text": "Title text for the header"
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
            "enum": ["header"]
        },
        "id": {
            "type": "string",
            "pattern": "^[a-zA-Z0-9-]+$"
        },
        "attributes": {
            "type": "array",
            "minItems": 3,
            "maxItems": 3,
            "items": [
                {
                    "type": "object",
                    "required": ["level"],
                    "properties": {
                        "level": {
                            "type": "string",
                            "enum": ["1", "2", "3", "4", "5", "6"]
                        }
                    },
                    "additionalProperties": false
                },
                {
                    "type": "object",
                    "required": ["markdown"],
                    "properties": {
                        "markdown": {
                            "type": "string",
                            "pattern": "^(#{1,6}) .*$"
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

## h1

Heading level 1 (# heading 1).

## h2

Heading level 2 (# heading 2).

## h3

Heading level 3 (# heading 3).

## h4

Heading level 4 (# heading 4).

## h5

Heading level 5 (# heading 5).

## h6

Heading level 6 (# heading 6).

## More components

[Library of components](document-object-model.md#library-of-defined-components-in-the-ca-object-model)