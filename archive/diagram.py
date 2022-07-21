import pydot
import common_utilities as CU

dotstring = '''  digraph {
  A -> B 
  A -> C
  A -> D
  A -> E
  A -> F 
  
  A [label="MVC"]
  B [label = "Overview"]
  C [label = "Quickstarts"]
  D [label = "Tutorials"]
  E [label = "Samples"]
  F [label = "Concepts"]
  }'''

graph = pydot.graph_from_dot_data(dotstring)
output_graphviz_svg = graph[0].create_svg().decode()
CU.write_text(output_graphviz_svg, "diagram.svg")