
# YAML Style Guide for Technical Writers

YAML (YAML Ain't Markup Language) is a human-readable data format, primarily used for configuration files and data serialization. This guide aims to ensure consistency, clarity, and interoperability when writing YAML documents for both human and machine readers.

## General Principles

- **Readability is Key**: YAML is designed to be readable by humans. Ensure that your structure and naming conventions are intuitive.
- **Consistency**: Stick to a consistent style throughout the document. It reduces confusion for both human readers and machine parsers.

## Indentation and Spacing

- Use **two spaces** for indentation. Never use tabs.
- Separate entries with a single blank line for clarity.
- Avoid trailing whitespace.

## Naming Conventions

- Use **snake\_case** for multi-word keys.
- Keys should be descriptive but concise.
	  
	```yaml
	user_name: John Doe
	email_address: john.doe@example.com
	```

## Scalars (Single Values)

- Use plain, unquoted scalars whenever possible. 
- Use double quotes for scalars that may be misinterpreted.

	```yaml
	name: John Doe
	note: "True isn't a confirmation here."
	```

## Collections

- Use block sequences (dashes) for lists:

	```yaml
	fruits:
	  - apple
	  - banana
	  - cherry
	```

- Use block mappings for key-value pairs:

	```yaml
	user:
	  name: John Doe
	  age: 30
	```

## Comments

- Start comments with a space for readability.
- Place comments on a new line above the code they refer to, not at the end of the line.

	```yaml
	# This is the user's age in years
	age: 30
	```

## Multi-Line Strings

- Use the literal block scalar (`|`) for multi-line strings where newlines need preservation.
- Use the folded block scalar (`>`) for multi-line strings where newlines should be converted to spaces.

	```yaml
	description: |
	  This is a longer description
	  that spans multiple lines.
	```

## Booleans and Nulls

- Use lowercase for boolean values: `true` and `false`.
- Use `null` for null values.

## Anchors and Aliases

- Use anchors (`&`) and aliases (`*`) sparingly for reusing content, ensuring they improve readability rather than confuse.

	```yaml
	default_address: &address
	  street: 123 Main St
	  city: Springfield

	billing_address: *address
	```

## Keep It Simple

- Avoid excessive nesting. If a document is too deeply nested, consider if there's a simpler representation or if some data can be abstracted.

## *Validation

- Always validate your YAML documents using online tools or libraries to ensure they're syntactically correct and machine-readable.

## Notes on using Markdown with YAML

Combining Markdown within YAML can be useful, especially for configuration files of static site generators or other systems that require rich text configuration. However, there are some considerations to keep in mind:

1. **Quoting and Escaping**: 
	- Strings containing special characters or those that could be interpreted as native YAML data types (e.g., `true`, `false`, numbers) should be enclosed in quotes.
	- If the Markdown content has characters like `"`, `:`, or `-` which have special meanings in YAML, ensure they're properly escaped or enclosed in quotes.

2. **Multiline Strings**:
	- For longer Markdown content, use YAML's block scalar options, `|` for literal style and `>` for folded style.
	- Literal style (`|`) keeps newlines as they are, making it suitable for Markdown content.
	- Folded style (`>`) turns newlines into spaces, except for double newlines.

3. **Indentation Matters**: 
	- Remember that YAML is sensitive to indentation. If you're writing multiline Markdown, ensure that every line of content is indented appropriately relative to its key.

4. **Avoid Ambiguity**:
	- Since both Markdown and YAML use characters like `-` and `#` for special purposes, be clear in your context. For instance, a list in Markdown should be clearly distinguishable from a list in YAML.

5. **Comments**:
	- If you're commenting within the YAML portion, use `#`. However, if you need to comment within the Markdown content, use the appropriate Markdown syntax for comments.

6. **Validation**: 
	- After writing, it's a good idea to validate your YAML file to ensure there are no syntax errors. Some online tools or local libraries can parse YAML to check its validity.

7. **Preview Your Markdown**:
	- Since Markdown is for rendering to HTML, ensure you preview the rendered content to check that it displays as expected, especially when embedded in YAML.

8. **Consider Human Readability**:
	- Even though you're embedding Markdown in YAML, the file should still be easily readable. Use spacing and comments judiciously to guide the reader.

9. **Use with Purpose**: 
	- Embedding Markdown in YAML is unconventional and can be confusing to some developers. Ensure there's a clear reason for doing so, such as specific tools or systems that require it.

10. **Document**: 
	- If your project heavily relies on embedding Markdown in YAML, consider providing documentation or comments to guide other developers or collaborators.

By being cautious and thorough in merging the syntaxes of Markdown and YAML, you can maintain files that are both human-readable and machine-interpretable.

## Tables in Markdown In YAML

Writing Markdown tables within a YAML file requires special care, given the nature of both YAML's whitespace sensitivity and Markdown's table syntax. Here are some tips to make the process smoother:

1. **Use Quotation Marks**:
   2. Enclose the entire table in double quotes to ensure YAML treats it as a single string.
   3. Inside the table, escape any double quotes with a backslash (`\"`).

2. **Multiline Strings**:
   2. Use the `|` (literal block scalar) before starting the table. This tells YAML to interpret the following lines as a multi-line string.
   3. Ensure the table content is indented correctly according to the YAML structure.

3. **Markdown Table Syntax**:
   2. Begin with the header row, followed by a delimiter row, and then the data rows.
```markdown
| Header1 | Header2 |
|---------|---------|
| data1   | data2   |
```

4. **Spacing**:
   2. Maintain consistent spacing within your table columns to enhance readability in raw form.

5. **Avoid Extra Characters**:
   2. Ensure no extraneous characters are present, especially YAML-specific ones like `:`, `-`, and `#`, within your table unless they're part of the table data.

6. **Embedding YAML in Tables**:
   2. If you need to embed YAML content within a table cell, consider linking to the YAML content or providing a brief description instead of trying to fit it all inside a table cell.

7. **Indentation**:
   2. Make sure every line of the table, including separators, is indented the same amount relative to the key indicating the table.

8. **Validation and Preview**:
   2. Use a YAML validator to ensure your combined Markdown and YAML syntax is correct.
   3. Preview the rendered Markdown to verify the table displays correctly.

9. **Limit Table Complexity**:
   2. Given the complexities of managing indentation and ensuring valid syntax, it's advisable to keep tables relatively simple when embedding them within YAML.

10. **Provide Context**:
   2. Consider adding a comment above the table to explain its purpose, especially if its inclusion in the YAML might be confusing to other collaborators.

Here's a small example of how it could look:
```yaml
description: |
  Here's a table:

  | Header1 | Header2 |
  |---------|---------|
  | data1   | data2   |
```

Remember, the combination of Markdown tables within YAML files is unconventional, so always ensure the context demands it and that the end result is both readable for humans and parsable for machines.

## Closing

Remember, the primary goal of YAML is readability and simplicity. Keep human readers in mind first, ensuring they can understand your document's structure and intent. Machines come second; they're quite good at adapting as long as the syntax is correct.

