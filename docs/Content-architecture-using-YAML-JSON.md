# Content Architecture using YAML and JSON with a Common Rules Engine

## Objective
Develop a simplified rule writing process for content architecture using a combination of JSON, YAML, and a common rules engine.

## Requirements

1. **Document Representation**:
	- Each document will contain:
		- Metadata: Defined as a YAML document. This can be converted to JSON. The address would be structured as `document/metadata/<attribute>`.
		- Body: Represents the core content of the document.

2. **Conversion**:
	- The content should be converted from Markdown to JSON/YAML. Current practices include converting from Markdown to XHTML, then to JSON.

3. **Content Patterns**:
	- The content architecture should be organized hierarchically as follows:
		1. Patterns are contained within patterns.
		2. A hub pattern contains TOC patterns.
		3. A TOC pattern contains guide patterns.
		4. A guide pattern contains article patterns.
		5. An article pattern contains unit patterns.
		6. A unit pattern contains component patterns.

4. **Validation**:
	- The proposed structure should be validated using JSON schemas.

5. **Queries & Content Generation**:
	- Given the predictable structure, it would be possible to query specific sections for declarative assessments. This could aid in programmatic content generation routines.

6. **Document Structure Sample**:
	```yaml
	document:
	  - attribute: value
	metadata:
	  - attribute: value
	body:
	  - unit:
	      Type: "Type Value"
	      Content: "Content Value"
	```

7. **Feedback on Document Representation**:
	- Use JSON to represent the document, JSON schema for schemas, and JSON query for declarative rules.
	- Consideration for JSON-LD:
		- Works well with RDF.
		- Compatible with Schema.org which is based on RDFa.

8. **Markdown Conversion Challenges**:
	- Rendering currently strips out all the markdown/HTML, thus needing a revision.
	- Some content might need to be written twice; once for SEO and once for display.
	- Relying solely on a parser for markdown might not be reliable for content reidentification, thus creating a publish-out system.
	- Concerns on the support of authoring tools and the reidentification of content chunks.

9. **Development Challenges**:
	- Precise markdown writing aligned with patterns.
	- Heavy engineering work for the conversion and validation processes.
	- Schema validation should also be incorporated for better accuracy.

## Feedback
Feedback from stakeholders, including Louis Spinelli and Mimi Sasouvanh, should be integrated into the final process, especially in terms of JSON usage, content development, and engineering requirements.