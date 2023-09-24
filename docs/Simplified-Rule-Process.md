# Simplified Rule Process for CA Object Model Representation

## Objective
To establish a common standard for representing the CA object model to facilitate easy querying and rule writing.
## JSON Parsing Challenges
Metadata tags are individual objects.
Serialized .Net places metadata objects in a variable order.
To query effectively, multiple rules might be necessary.
## Suggested Model for Simplified Access
```
Document
<attributes for the document>
Metadata
  <metadata>
Body
  <body attributes>
```
   - Potential path for JSON queries: `document/metadata/<metadata attribute>`

## Transition to YAML
A shift from the current model to YAML will simplify the entire process.
With this, a direct transition from YAML to JSON will be possible facilitating easier querying with JSON Query.
## Common Information Model (CIM)
The idea is to move towards a standardized model much like the CIM, which enables a common querying method across platforms.
Partnering with the Data I&I team who has experience with CIM could provide insights and methods to create a more robust model.
## Integration and Development
The Linter Engine can serve as a testbed for developing and refining the CIM.
The focus should be on the Linter and DocuTune tools as they are both on the same engineering team, making collaboration easier.
## Scope
The end goal is a rules engine that operates on common standards, ensuring interoperability.
The Linter is currently at the forefront of driving this story of interoperability.
## Considerations
Potential political hurdles from other teams might arise.
There's a need for collaborative efforts, especially with LPP, to ensure the success of this initiative.
## Next Steps
Delve deeper into understanding the structure and benefits of CIM.
Begin discussions with relevant teams and stakeholders to move forward with this idea.
Update the software specification based on evolving insights and feedback.

# Content Architecture Standards, Explanations, and Discussion Points

**1. BNF Approach:**
   - **Explanation:** BNF (Backus–Naur form) is a metasyntax notation for context-free grammars. It's used to describe the syntax of languages in computing.
   - **Discussion:**
	 - Louis identified it as best for capturing the "whole pattern".
	 - Concerns about its need and alternative flows (e.g., markdown body -\> xhtml -\> json).
	 - Issues determining if content matches a pattern with it.
	 - The Tech Design document explained how BNF is used in their system, emphasizing its clarity.

**2. Markdown and YAML:**
   - **Explanation:** Markdown is a lightweight markup language, while YAML is a human-readable data serialization standard.
   - **Discussion:**
	 - Debates about the workload required for compliant markdown vs. YAML.
	 - The possible introduction of authoring tools to guide "structured" markdown writing.
	 - YAML to JSON conversion and its benefits.
	 - YAML might be the initial level, but the main intent is to use JSON/JSON schema.

**3. BNF vs. Regex:**
   - **Explanation:** While BNF provides a structured representation, Regex (Regular Expressions) defines search patterns for strings.
   - **Discussion:**
	 - Scaling issues with Regex.
	 - Challenges with BNF when mapping entire templates/articles.
	 - Using BNF for parsing at the chunk level and Regex for rule-writing.

**4. Content Structure:**
   - **Explanation:** Structuring content to have patterns and rules for consistent representation.
   - **Discussion:**
	 - Louis suggests YAML/JSON would save everyone trouble in the long term.
	 - Benefits of structuring content, especially when dealing with AI and automated processes.
	 - Issues with writers intermingling presentation with content/data.
	 - Stripping out Markdown and HTML from chunks for rendering/integration.
	 - Moving towards content as data for repurposing based on audience and context.

**5. Mermaid for Diagramming:**
   - **Explanation:** Mermaid is a tool for generating diagrams and flowcharts from text in a similar manner as markdown.
   - **Discussion:**
	 - Mermaid's potential as a diagramming standard.
	 - The need to address the "source of truth" issue with current diagrams.

**6. Structured vs. Unstructured Content:**
   - **Explanation:** Unstructured content lacks a predefined data model or is not organized in a pre-defined manner. Structured content has a clear, consistent data model.
   - **Discussion:**
	 - Questions about the long-term viability of unstructured content for their use cases.
	 - The perception that unstructured content may be suitable for blogs and marketing but not for other specific use cases.

**7. Tooling and Collaboration:**
   - **Explanation:** Tools that can assist in the structuring and presentation of content.
   - **Discussion:**
	 - The need for authoring tools that abstract the format efficiently.
	 - Challenges with multiple teams having varied standards.
	 - The importance of simplifying to achieve abstraction.

**8. AI and LLMs (Likely Large Language Models):**
   - **Explanation:** LLMs, such as the one from OpenAI, are capable of processing vast amounts of data but still depend on the quality of input.
	 

# Chunking in Learn-Linter System
The document details the requirements and design considerations for implementing a new chunking and content validation system in the Learn-Linter platform.

## Background
Mimi’s engineering team has undertaken the task to replace the previously unsuccessful learn-validation extension with the improved learn-linter tool, which will assist authors by providing real-time feedback and quick fixes.

## System Requirements

*1. Validation Features:*
- Integration of build validations and single-file parsing capabilities.
- The system should be able to present quick fixes to users for broken links and other detected issues. 
- Record user decisions related to quick fixes to improve the recommendation system.

*2. Telemetry:*
- Capture how users interact with validations: their fixes, undos, and whether they choose to ignore them.
- Utilize feedback for continuous improvement.

*3. Integration with Strong Model:*
- The system will include a C# library, removing the need to write and read JSON via docFX.
- It should provide an interface to a full Markdown Abstract Syntax Tree (AST). Compatibility with other models like markdig should be evaluated.

*4. Supported Elements:*
- Initially, the system will not support elements like Links, Xref, and Snippets due to the complexity of loading the whole repository. Existing code can handle these.

*5. Collaboration with the Engineering Team:*
- The engineering team will primarily provide services through the learn-linter. How it will integrate with the existing rules engine is yet to be determined.

## System Design Considerations

*1. Rules Engine Overhaul:*
- The system should prioritize the design for chunking, optimizing for performance.
- The integration with docFX should consider future updates to the rules engine.
- It should potentially accommodate Article Sets natively. The implications on re-linting files within the Guide must be addressed.
- The system needs testing with elements like ZonePivots, and suitable solutions need to be devised to handle any anomalies.

*2. User Interface and Integrations:*
- Post-integration, the focus should shift towards enhancing the UI, adding quick fixes, and ensuring seamless integration with other tools.
- Exploring options like integrating AI for pattern recognition can also be looked into.
- A hybrid approach of Yaml to Markdown is recommended, although a shift to Yaml requires a significant change in the authoring environment.
	  
*3. Acrolinx Decoupling:*
- The start date for this process is undetermined, but the project aims to achieve savings and consolidate rulesets across platforms.

## Conclusion
The goal is to build a robust model that facilitates content validation and assists authors in real-time. With these specifications, the collaboration between all stakeholders should result in an improved tool that enhances the authoring process.