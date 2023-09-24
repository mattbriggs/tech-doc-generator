# Notes on content

## Content lifecycle

Content has a lifecycle. Content has two main sources: data flows into the site and is generated using a data-to-text content generation process. For example, much of the API content is reference content is built using an automated process from the code. A variety of methods are used to collect data about code and then produce reference content. A smaller portion of content published to the site is manually authored by contributors and maintained by content teams.

Once content is written and published, it is maintained by the content teams who respond to customer feedback, updates from product teams, and data collected about user interaction with the content. Content teams regularly check their content to make sure that the content is current and accurate. Much of our content references software that has features being removed and added at a continual rate.

When content is no longer required, it is archived.

Much of the content on the web site is 'unstructured content'. This means that the content cannot be 
## Content construction

Content is contained in articles. Learn uses a topic-based architecture. This means that each article is considered an atomic part of content. You might think of an article as a page in a book. A sequence of pages makes up a book. A sequence of articles makes up a manual for the technical documentation. In training, the atomic unit is called a module. A sequence of modules makes up a learning path (or lesson).

To guide this concept, articles have an intent statement. That is each article has an audience, a task that would to be accomplished, and this task leads to an outcome. To document complex scenarios, a sequence of tasks would require require a sequence of articles.

### Collections of articles

Articles are collected in tables of contents, and a landing page for the table of context provides hyperlinks and a common abstraction of the set of articles that are connected to the table of contents. A table of contents is both a navigation affordance and an inventory of the articles.

In turn tables of contents and landing pages are collected into hub pages. Hub pages use a “hub and spoke” model. Each hub page is organized around a defined area and links to the tables of contents and hub pages that support this area. For example, a hub page for a product may have as spokes tables of contents that present the information for different users of the product.

### Composition of an article

An article with an intent is in turn made of parts. Unlike the article, these parts are not “stand alone” articles in the same that that the parts a biological cell cannot survive outside of a cell. The nucleus, organelles, and cytoplasm would just be blobs of matter outside of a cell.

An article is made of units. It has is compose of three categories of units: the metadata block, the introduction block, and the heading two blocks.
In turn each unit is made of components. A components may be thought of a content block. Components include introductory paragraphs, images, tables, ordered and unordered list, and so on.
## Structured vs Unstructured Content

Content architecture is concerned with content, but what is content? To understand this question, I turned to the book _Content_ (MIT Press) and found that content itself is an open definition. Content is the contents of a container on the web. Socks in a drawer are as much content as the words in a novel.

Kate Eichorn notes:
> Content isn’t necessarily data, even if the two terms are frequently used interchangeably. Some argue that this is because content is contextualized information and data is not. Others argue that while content conveys a message (in words or images or sound), data does not. But as suggested earlier in this chapter, some content—for example, the Instagram egg—seems to exist simply for the sake of circulation alone and not to convey a message. Given such vexing problems, attempts to define content seem to lead to only the most imperfect operational definitions—for example, “all the stuff that circulates online”—but this too isn’t quite right. Does a classic film streamed online rather than projected in a movie theater become content simply because of the context? It seems that content isn’t just context specific but also subject to the eye of the beholder. — Eichhorn, Kate. Content (The MIT Press Essential Knowledge series) (p. 21). MIT Press. Kindle Edition. 

This definition is useful in our context in so far as it points to several challenges Learn has in offering content to our readers. And it points to several technical solutions to the problem of “unstructured content.”

Before we get into that, we will look address the solution of structured content compared to unstructured content. In our list of the parts of content, we alluded to two different types of language. We had natural language which are contained in text blocks. And we had constructed language which are contained in code blocks. The constructed language of computer code is a structured language and represents a flavor of structured content. C# for example is difficult to write because it is structured. It must be structured because the compiler cannot resolve ambiguity. Instead each character that appears in C# must get interpreted into executable code that can then be fed to the processor and result a workload. To write workable C# requires practice and validation with code linters and debugging tools and then finally testing. The result is a strange piece of language in that this language is somewhat hard for a human reader to understand, but this piece of language can also do work.

In Learn content, a common practice for our readers is to fine and return to a code snippet and the reader will cut and pate the code snippet into a command line interface at their workstation and in their environment and run it. When the code is formatted correctly and any environmental specific modification are made clear in the documentation, This code just runs and does work. Our documentation then functions because it contains pieces of structured content.

Structured content is not limited to code snippets. Structured content can include any documentation format that can be programmatically consumed. Common formats of pragmatically consumed information include XML, JSON, and YAML. These are documents formats exist midway between code and natural language text. They include a schema and markers that allow them to be understood by computer code. For example, a JSON file that contains a list of URLs for a whitelist can be ingested and loaded into a firewall application. Our reader in this case is both the system administrator for the network using the firewall application but also this administrators toolchain.

Structured content is consumed by agents downstream from our content including third party systems integrating with our content. You might call this type of content, content as data. Perhaps the most critical of these third party systems is Google Knowledge Graph that creates a representation of our content based on structured content and where it can’t find deliberately structured content, it asserts its best guess on what the structure might be.
Unless Google can’t really make a good guess. And in this case the agent regards the content as a kind of blob, a fat burg in the flow of data from the source to the target. The target is the audience of readers on the web with their desktops, laptops, and mobile devices interacting with Google knowledge graph.

With structured content defined, we have another category, which is unstructured content. This is not to say that it is completely unstructured but rather the structure is organic to human language. While natural language processors can parse and create structured representations, these are translation or best guesses of what the language. A human reader can deal with gaps in logic, leaps of logic, implied context, recursive statements, typos, the repetition of words and sentences, and other expressions of what you might call “the infinite”. Computers cannot really deal with ambiguity. Ambiguity is not a bug in natural language but a feature. While it may create miscommunication, natural language is an efficient way to record and transmit information. The precise, exact, and definitive can also be recorded in natural language as well as the ephermal qualities such as context, connotation, and empathy.
The challenge then is to find an architecture and technical solutions that supports programmatic processing, supports both human and agent-based readers, and allows for empathetic human written content to be offered alongside data vital to the work and learning of our audience.

To consider content then as the contents of a structure, for example socks in a drawer, is a step toward this solution. A sentence and a paragraph can be the sock in a drawer. The structure can be the chest of drawers. In some drawers, the writer may place paragraphs of text. In other drawers they may place tables of data. A reader can be presented the contents as an article and read it as an article. An agent can interrogate the contents and know to access the table of data, where to find it and how to access the columns and rows so that data can be incorporated into the agent’s workflow.