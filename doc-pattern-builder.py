import os
import yaml
import markdown
import graphviz
import pystache as ST
import common_utilities as CU

def get_yaml(filepath):
    '''With a yaml file, return a dictionary.'''
    with open (filepath, "r") as stream:
        outdict = yaml.load(stream, Loader=yaml.CLoader)
    return outdict

def main():
    '''Main generator logic.'''
    patterns = {}
    pattern_files = CU.get_files("./pattern-definitions", ".yml")
    for i in pattern_files:
        temp = i.split("\\")[-1].replace(".yml", "")
        temp_text = get_yaml(i)
        patterns[temp] = temp_text
    pat_names = patterns.keys()
    for i in pat_names:
        sk = patterns[i].keys()
        filename = "./pattern-definitions-help/" + "{}.html".format(i)
        print("Creating {}".format(filename))
        outfile = ""
        for s in sk:
            if s == "Title":
                outfile += "# {}: {}\n".format(s, patterns[i][s])
            elif s == "Diagram":
                try:
                    graphname = i + ".svg"
                    dotname = i + ".gv"
                    CU.write_text(patterns[i][s], './pattern-definitions/media/' + dotname)
                    graphplink = '![{}]({})'.format(i, './pattern-definitions/media/' + graphname)

                    graphviz.render('dot', 'svg', graphplink).replace('\\', '/')
                    './pattern-definitions/media/' + graphname

                    outfile += "# {}: \n{}\n".format(s, graphplink)
                except:
                    outfile += "# {}: \n{}\n".format(s, patterns[i][s])

            else:
                outfile += "## {}:\n{}\n".format(s, patterns[i][s])
        html =  html = markdown.markdown(outfile)
        CU.write_text(html, filename)


if __name__ == "__main__":


    main()