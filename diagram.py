import graphviz

diagram = '''digraph { A -> B A -> C A -> D A -> E A -> F

A [label="MVC"] B [label = "Overview"] C [label = "Quickstarts"] D [label = "Tutorials"] E [label = "Samples"] F [label = "Concepts"] }'''

src = graphviz.Source(diagram)

graphviz.render(src, 'png', './pattern-definitions/media/' + "test.png")