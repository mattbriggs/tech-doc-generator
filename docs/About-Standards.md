# Standards

Structured content depends on the coordination of multiple groups both internally and externally to the platform team. Learn content is the content that appears on the website. This content is by and large unstructured content, but in order to meet the challenges of integration with third party systems and to provide the framework for generative AI, the content needs to move toward a structured content.

## Who is concerned with standards

The primary groups are:
- Platform
	- The platform team. Within the platform team there are several squads. These include:
		- Authoring
		- Validation
		- Rendering
		- Metadata
		- Discovery
	- The product team. The product team has a stake in the third party integration of Learn content.
	- Information Architecture. They design the site experience and interaction of users with site structures.
- Content Teams
	- Skilling. Publishes Azure content, Power Platform Content, and Azure Architecture Center content.
	- Magic. Publishes M360 Content (Office)
	- BAP (Windows Dynamics). Published Windows Dynamics Content.
- Learn support from Skilling. Within the Skilling organization several teams provide broad support to the Learn platform.
	- Customer Experience (Skilling)
		- Content Architecture. Content architecture is responsible of the design and management of content structures. Content structured contain content; Content is in turn contained by the site experience structures created by the Information Architecture.
	- Tools Team (BC&S)

## Standards

To coordinate these groups we use several shared models and standards.

### Standards

#### Loose coupling

By requiring OData/REST interfaces, combined with the robust documentation of OpenAI/Swagger endpoints, we ensure not only transparency in our service interactions but also promote a loosely coupled architecture. This commitment facilitates effortless adaptability, streamlined updates, and fosters a future-ready system that effortlessly interacts with diverse platforms.

#### Single-concern

We should follow a principle of "single concern" or "single responsibility" refers to the idea that each service to tool should have only one reason to change. This is an extension of the Single Responsibility Principle (SRP) from object-oriented programming. In terms of our services, it means:

1. **Focused Functionality**: Each service/tool should be responsible for a specific business capability or functionality. This ensures that the service remains small, focused, and easy to maintain.
	  
2. **Isolation**: By ensuring that a service/tool  has a single concern, you also ensure that changes in one service have minimal impact on other services. This enhances the resilience and flexibility of the system.
	  
3. **Independence**: Single-concern service/tool  can be developed, deployed, scaled, and maintained independently. This is especially useful in larger teams or organizations where different teams can work on different services without stepping on each other's toes.

4. **Easier Scaling**: When service/tool have single responsibilities, it's easier to identify which services need scaling based on specific demands. For instance, if one part of your system experiences heavy traffic, you can scale just that specific service/tool without affecting others.

### Yet another markup language (YAML)

By choosing YAML for human-written and machine-readable files, we prioritize simplicity and comprehension. This ensures seamless collaboration between teams and systems, bridging human insight with machine efficiency for a streamlined experience. For a YAML style guide see: XXX.

### JSON Schema

By integrating JSON and its accompanying JSON Schema, we enhance the accuracy and ease of authoring YAML-based workloads. This interaction not only ensures consistent data structures and validation but also broadens interoperability, allowing for smoother integration across diverse systems and streamlined workflows.

### Models

#### Site architecture: United Content Model
**Information Architecture**
The entire website uses the United Content Model for site interaction documented and managed by the Information Architecture team. This is currently two pages in the contributor guide. This may need to be revisited to account for the CA's approach. What would a common standard for a site wide content architecture?

#### Content architecture: Object Model for Learn Content
**Content Architecture**
The content structure uses design patterns for content documented and managed by the Content Architecture team. This structure is managed using the Content Patterns program. The structure uses an object model that is described in JSON schemas and validated using an extended version of JSON Schema. this is being developed.

#### Validation: Validation Standard
**LLP: Validation**
Validation uses a validation object standard that is rendered in an extended version of JSON Schema.

#### Quick fixes and content generation standards
**LLP/CX/CA**
Content generation includes in-line quick fixes to the methods used to generate content. What do we mean by standards and what is a content generation standard?

#### Governance
**Governance Team** who is this?
Data and content governance uses a standard that is managed by the governance squad.

## Notes on validation and governance
The rules engine uses validation standards which are the implementation of requirements form the Governance team. The validation standard perform three tasks: 1) validation of structure 2) data validation 3) style validation.

Standard for content exist in several domains.

- Business Domain
- 

We are conflating in the validation story right now three things: 1) enforce consistency and accuracy 2) provide author assistance 3) content generation.
