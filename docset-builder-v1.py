'''
Docset Builder
The docset builder script assembled a document set by using the doc-design.yml
and the patterns definitions to create the documentation at a target location.

The script expects to find a config.yml file in the same folder as the builder
script.

Version 1 uses the patterns-v1-* folders.

7.15.2022
Matt Briggs
'''

import os
import yaml
import pystache as ST
import common_utilities as CU


def create_toc_yaml(path, toc_list):
    '''With a list created a toc yaml'''
    out_toc = {}
    out_toc["items"] = toc_list
    toc_yaml = yaml.dump(out_toc)
    CU.write_text(str(toc_yaml), path)

def create_doc(documents, pathname, meta_dict):
    '''with the filename stem and metadata create the file'''
    meta_dict["Date"] = "7/1/2022"
    try:
        file_text = ST.render(documents[meta_dict["Type"]], meta_dict)
        CU.write_text(file_text, pathname)
    except:
        print("Problem creating: {}".format(pathname))

def main():
    '''Main generator logic.'''
    
    with open ("config.yml", "r") as stream:
        config = yaml.load(stream, Loader=yaml.CLoader)

    with open (config["docdesign"], "r") as stream:
        design = yaml.load(stream, Loader=yaml.CLoader)

    documents = {}
    templates = CU.get_files("./patterns-v1-doc", "md")
    for i in templates:
        temp = i.split("\\")[-1].split(".")[0]
        temp_text = CU.get_text_from_file(i)
        documents[temp] = temp_text

    pathstem = config["target"]

    top_toc = []
    top_pair = {}
    top_pair["name"] = design["Title"]
    top_pair["href"] = "index.yml"
    top_toc.append(top_pair)

    for pat in design["Patterns"].keys():
        print("Creating {}".format(pat))

        top_pat_pair = {}
        top_pat_pair["name"] = pat
        top_pat_pair["href"] = "{}/toc.yml".format(pat)
        top_toc.append(top_pat_pair)

        guide_toc = []
        for i in design["Patterns"][pat]:
            section = {}
            section["name"] = i["Title"]
            section["href"] = "{}".format(i["Filename"])
            guide_toc.append(section)
            try:
                os.mkdir(pathstem + "{}\\".format(pat))
            except FileExistsError:
                print("Exists: {}".format(pathstem + "{}\\".format(pat)))
            pathname = pathstem + "{}\\".format(pat) + i["Filename"]
            print("Creating {}".format(pathname))
            create_doc(documents, pathname, i)
        toc_path = pathstem + "{}\\".format(pat) + "toc.yml"

        print("Creating {}".format(toc_path))
        create_toc_yaml(toc_path, guide_toc)

    top_path = pathstem + "toc.yml"
    create_toc_yaml(top_path, top_toc)

if __name__ == "__main__":

    main()