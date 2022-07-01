import yaml
import common_utilities as CU

def main():
    '''Main generator logic.'''
    
    with open ("config.yml", "r") as stream:
        config = yaml.load(stream, Loader=yaml.CLoader)

    with open (config["docdesign"], "r") as stream:
        design = yaml.load(stream, Loader=yaml.CLoader)
    
    print(design)

    documents = {}
    templates = CU.get_files("./patterns-doc", "md")
    for i in templates:
        temp = i.split("\\")[-1].split(".")[0]
        temp_text = CU.get_text_from_file(i)
        documents[temp] = temp_text


if __name__ == "__main__":

    main()