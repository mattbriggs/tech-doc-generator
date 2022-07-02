import os
import yaml
import common_utilities as CU


def create_toc_yaml(path, toc_list):
    '''With a list created a toc yaml'''
    out_toc = {}
    out_toc["items"] = toc_list
    toc_yaml = yaml.dump(out_toc)
    CU.write_text(str(toc_yaml), path)

def create_doc(documents, pathname, meta_dict):
    '''with the filename stem and metadata create the file'''
    a = meta_dict["Name"]
    b = meta_dict["Author"]
    c = meta_dict["Author"]
    d = "7/1/2022"
    e = meta_dict["Name"]
    file_text = documents[meta_dict["Type"]].format(a, b, c, d, e)
    CU.write_text(file_text, pathname)

def main():
    '''Main generator logic.'''
    
    with open ("config.yml", "r") as stream:
        config = yaml.load(stream, Loader=yaml.CLoader)

    with open (config["docdesign"], "r") as stream:
        design = yaml.load(stream, Loader=yaml.CLoader)

    documents = {}
    templates = CU.get_files("./patterns-doc", "md")
    for i in templates:
        temp = i.split("\\")[-1].split(".")[0]
        temp_text = CU.get_text_from_file(i)
        documents[temp] = temp_text

    pathstem = config["target"]

    top_toc = []
    top_pair = {}
    top_pair["name"] = design["Name"]
    top_pair["href"] = "index.yml"
    top_toc.append(top_pair)

    for pat in design["Patterns"].keys():
        print("Creating {}".format(pat))

        top_pat_pair = {}
        top_pat_pair["name"] = pat
        top_pat_pair["href"] = "/{}/toc.yml".format(pat).lower()
        top_toc.append(top_pat_pair)

        guide_toc = []
        for i in design["Patterns"][pat]:
            section = {}
            section["name"] = i["Name"]
            section["href"] = "{}.md".format(i["Filename"])
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