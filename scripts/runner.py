import os

class Runner:
    def __init__(self):
        self.script = get_scipts()

def get_scipts():
    scripts = []
    for f in os.listdir():
        if '__' not in f and 'runner.py' not in f:
            scripts.append(f)
    return scripts

