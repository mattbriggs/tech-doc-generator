import os
import yaml
import markdown
import pydot
import pystache as ST
import common_utilities as CU

def get_yaml(filepath):
    '''With a yaml file, return a dictionary.'''
    with open (filepath, "r") as stream:
        outdict = yaml.load(stream, Loader=yaml.CLoader)
    return outdict

def build_index(inlist, filename):
    '''With a list of touples and a filename create and save the index.'''
    indexfile = "# Skilling patterns draft\n"
    for i in inlist:
        indexfile += "[{}]({})\n\n".format(i[0],i[1])
    indexfile += "<hr>[Microsoft content pattern library](https://review.docs.microsoft.com/en-us/help/patterns/?branch=patterns)"
    html =  html = markdown.markdown(indexfile)
    CU.write_text(html, filename)
    print("Creating {}".format(filename))

def main():
    '''Main generator logic.'''
    patterns = {}
    pattern_files = CU.get_files("./pattern-definitions", ".yml")
    for i in pattern_files:
        temp = i.split("\\")[-1].replace(".yml", "")
        temp_text = get_yaml(i)
        patterns[temp] = temp_text
    pat_names = patterns.keys()
    index_files = []
    for i in pat_names:
        sk = patterns[i].keys()
        filename = "./pattern-definitions-help/" + "{}.html".format(i)
        shortfilename = "{}.html".format(i)
        print("Creating {}".format(filename))
        outfile = ""
        for s in sk:
            if s == "Title":
                outfile += "# {}: {}\n".format(s, patterns[i][s])
            elif s == "Diagram":
                if patterns[i][s][:7] == "digraph":
                    graphname = i + ".svg"
                    graphpath_write = "./pattern-definitions-help/media/" + graphname
                    graphath_ref = "./media/" + graphname
                    graphplink = '![{}]({})'.format(i, graphath_ref)
                    graph = pydot.graph_from_dot_data(patterns[i][s])
                    output_graphviz_svg = graph[0].create_svg().decode()
                    CU.write_text(output_graphviz_svg, graphpath_write )
                    outfile += "## {}: \n{}\n".format(s, graphplink)
                else:
                    outfile += "## {}: \n{}\n".format(s, patterns[i][s])
            else:
                outfile += "## {}:\n{}\n".format(s, patterns[i][s])
        index_files.append((i, shortfilename))
        outfile += "<hr>[Top](index.html) | [Microsoft content pattern library](https://review.docs.microsoft.com/en-us/help/patterns/?branch=patterns)"
        html =  html = markdown.markdown(outfile)
        CU.write_text(html, filename)
    build_index(index_files, "./pattern-definitions-help/index.html")


if __name__ == "__main__":


    main()