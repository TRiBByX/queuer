import os
import re

class Script:
    def __init__(self, scriptname, author, docstring='', options=[]):
        self.scriptname = scriptname
        self.docstring = docstring
        self.author = author
        self.options = options

def get_scripts():
    scripts = [f for f in os.listdir('scripts/') if '__' not in f and 'runner.py' not in f]
    return{script: Script(scriptname=script, docstring=re.findall('(?s)"""(.*?)"""', open(f'scripts/{script}', 'r').read())) for script in scripts}
