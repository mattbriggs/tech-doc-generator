---
title: Reference for {{implementation-name}}
description:  Reference for {{implementation-name}}.
author: mattbriggs
ms.author: mabrigg
ms.date: 09/24/2022
ms.topic: contributor-guide
ms.prod: non-product-specific
ms.custom: internal-contributor-guide
---

# Reference for {{implementation-name}}

This document contains views of the {{implementation-name}} that can be used to:
- Check a document for consistency.
- Help an author quickly write a document.
- Identify {{implementation-name}} in the content.

## Schema for {{implementation-name}}

The document contains the following schema.

```yaml
name: Quickstart - General
version: 0.0.0
description: 
units:
  - unit: "metadata"
    position: 0
    contains:
    - title: "string"
      text-has: "quickstart"
      required: yes
    - description: "string"
      text-has: "quickstart"
      required: yes
    - author: "string"
      required: yes
    - ms.author: "string"
      required: yes
    - ms.date: "string"
      required: yes
    - ms.topic: "string"
      text-is: "quickstart"
    - customer-intent: "string"
  - unit: "h1"
    position: 1
    text-begins: "Quickstart: "
    required: yes
    contains:
    - comp: introduction
      text-start: ""In this quickstart, you'll"
      required: yes
  - unit: "h2"
    position: 2
    text-is: "Prerequisites"
    required: no
  - unit: "h2"
    repeat: yes
    required: yes
  - unit: "h2"
    text-is: "Clean up resources"
    position: -2
  - unit: "Next Steps"
    position: -1
    required: yes "required": [ "productId", "productName" ]
}
```

## Criteria for {{implementation-name}}

The following table contains the criteria for the {{implementation-name}}.

| Name | Level | Criteria | Guidance | Quickfix |
| --- | --- | --- | --- | --- |
| Heading 1 | Definition | Contains 1 H1. | Has a H1 header. | # Heading 1 |
| Introduction | Definition | Rule | A paragraph follows the H1. | An introduction paragraph answers what the reader can find in the document and why they would want to use the document to get this information. |
| Steps checklist | Recommended | Rule | A checklist helps orient the reader to the material in the document. It's made of checkmarks. Add a bullet list of short version of the Headings 2. | - item<br>- item<br>-item<br> |

## Template details

This template is a specific solution to the [{{pattern}}](../library/pattern-library-intro.md).

The template is supported by the following:
- [Template](../library/pattern-library-intro.md)
- [Template schema and criteria](../library/pattern-library-intro.md)