''' In this script, we read the contents of the markdown file, convert it to
HTML using the markdown library, and then store it in a JSON object with a key
of 'content'. You can modify the json_object dictionary to include any other
metadata or properties that you need in your JSON output. Finally, we use
json.dumps() to convert the Python dictionary into a JSON string with
indentation for better readability. '''

import markdown
import json

def convert_md_to_json(md_file_path):
    ''' Convert the markdown file to JSON. '''
    with open(md_file_path, 'r') as f:
        md_content = f.read()
        html_content = markdown.markdown(md_content)
        json_object = {'content': html_content}
        return json_object

def save_json(json_object, json_file_path):
    ''' Save the JSON object to a file.'''
    with open(json_file_path, 'w') as f:
        json.dump(json_object, f, indent=4)

# Example usage:
md_file_path = r'C:\git\mb\tech-doc-generator\patterns-rules\concept-markdown.md'
json_object = convert_md_to_json(md_file_path)
print(json.dumps(json_object, indent=4))
json_file_path = "C:\\git\\mb\\tech-doc-generator\\patterns-rules\\concept-markdown.json"
save_json(json_object, json_file_path)
