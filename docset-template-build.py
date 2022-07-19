import os
import yaml
import pystache as ST
import common_utilities as CU

def get_yaml(filepath):
    '''With a yaml file, return a dictionary.'''
    with open (filepath, "r") as stream:
        outdict = yaml.load(stream, Loader=yaml.CLoader)
    return outdict

def main():
    '''Main generator logic.'''
    template_defs = CU.get_files("./patterns-v2-doc/", ".yml")

    for i in template_defs:
        if i.find("!") < 0:
            t = get_yaml(i)
            outpath = "./gentemplates/{}{}.md".format(t["Name"], t["Version"])
            print("Creating... {}".format(outpath))
            outfile = ""

            comp = t["Components"]
            for j in comp:
                try:
                    comp_path = "./patterns-v2-components/" + j["Component"]
                    c = get_yaml(comp_path)
                    outfile += c["Boilerplate"] + "\n"
                    try:
                        outfile += "<-- " + c["Instructions"] + j["Help"] + " -->\n"
                    except:
                        pass
                except:
                    pass
            CU.write_text(outfile, outpath)

if __name__ == "__main__":

    main()