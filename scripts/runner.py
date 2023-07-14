import os
import re

class Script:
    def __init__(self, scriptname, author='', docstring='', options=[]):
        self.scriptname = scriptname
        self.docstring = docstring
        self.author = author
        self.options = options

    def __str__(self):
        return f"Scriptname: {self.scriptname}\nAuthor: {self.author}\nOptions: {self.options}\nDocstring:\n{self.docstring}"

def get_scripts():
    Scripts = {}
    scripts = [f for f in os.listdir('scripts/') if '__' not in f and 'runner.py' not in f]
    for script in scripts:
        script_doc_split = re.findall('(?s)"""(.*?)"""', open(f'scripts/{script}', 'r').read())[0].split('\n')[1:]
        name = script_doc_split[0].split(': ')[1]
        author = script_doc_split[1].split(': ')[1]
        options = script_doc_split[2].split(': ')[1].split(',')
        docstring = '\n'.join(['    ' + docline.strip() for docline in script_doc_split[4:-1]])
        Scripts[script] = Script(scriptname=name, author=author, docstring=docstring, options=options)

    return Scripts