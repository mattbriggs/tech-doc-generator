# Technical documentation generator

This repo builds on the *Specification for a Grammar for a Combinatorial System* to create the logic, scripts, and data structures to generate a complete technical doc set following our content architecture specifications and a pattern language for technical documentation and training. The intent of the project is to check requirements for the language grammar and underlying data structures to make the system entire easier to use for content authors.
## Before you start

You will need the following parts installed:
 - Install Python: https://www.python.org/downloads/.  
     Be sure to choose the option to add Python to your environment variables. Re-run setup if this option does not appear.
 - Install [virtualenv](https://medium.com/co-learning-lounge/create-virtual-environment-python-windows-2021-d947c3a3ca78): `Pip install virtualenv`

    **Note**: Run pip outside of the Python prompt.

### Steps to set up your environment

1. Clone a copy of this repo your local machine.
2. Open the repository. 
3. In the directory, open a PowerShell prompt and then your virtualenv (virtual environment) by typing:  
    `virtualenv ENV`
4. Activate the environment by typing:  
    `ENV/Scripts/activate`
5. Install your dependences in the virtual environment:  
    `pip install -r requirements.txt`

    **Note**: Run pip from inside the virtual environment, but outside of the Python prompt.

6. Copy the `config-example.yml` and rename to `config.yml`.
7. Open the fil.
    ```yml
    ---
    target: "<path-to-target-repo>"
    docdesign: "<path-to-doc-design>\\doc-design.yml"
    ```
8.  Update `target` to the target directory.  Be sure to escape the virgules. That is \\ rather than \.
9. Update `docdesign` to the full path and filename to your design document.
10. Run the script:` python docset-builder.py`.
11. Open your target directory and review the output in Visual Studio Code. You can create a branch, commit the changed, and create a PR to generate an OPS preview of the content.

## Notes on the code

The document level templates are based on the proof of concept document templates. I use the [Mustache](https://mustache.github.io/) template system with the [Pystache](https://github.com/sarnold/pystache) implementation.

## If you have issues, file a GitHub issue

[Create a GitHub Issue](https://github.com/mattbriggs/tech-doc-generator/issues/new/choose)