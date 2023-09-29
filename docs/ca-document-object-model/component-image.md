# image

In Markdown syntax, an HTML image is described using an exclamation mark `!` followed by square brackets `[]` containing the alt text, and immediately after, parentheses () containing the URL of the image. Optionally, a title can be included within double quotes inside the parentheses. For example: `![Alt Text](url "Title")`. This syntax embeds an image within the Markdown document, rendering it visible when the Markdown is converted to HTML or viewed on a platform supporting Markdown rendering.

## Diagram

The following diagram displays the set of possible sub-elements of the component.

```mermaid
classDiagram
    class ImageComponent {
        +String type
        +String markdown
        +String text
        +String href
    }
```

## Example markdown: markdown image

The following markdown is an example of the artifact in a file.

```md
![alt-text.](media/my-cool-graphic.png)
```
## Example markdown: image extension

```md
:::image type="content" source="<folderPath>" alt-text="<alt text>" link="<https://link.com>":::
```

## JSON parsed object

The following JSON represents the attributes of a parsed artifact.

```json
{
    "type": "image",
    "markdown": "![alt-text.](media\/my-cool-graphic.png)",
    "text": "Alt text",
    "source": "media/my-cool-graphic.png"
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
    "href": {
      "type": "string"
    }
  },
  "required": [
    "type",
    "markdown",
    "text",
    "href"
  ]
}

```

## diagram

Definition


## editorial

Definition

## screenshot

Definition

## wayfinder

Definition
## large-image

Definition

## More components

[Library of components](document-object-model.md#library-of-defined-components-in-the-ca-object-model)