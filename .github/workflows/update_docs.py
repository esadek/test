import os

directory = os.path.dirname(__file__)

print("In update_docs.py")

with open(directory + "/../../README.md") as f:
    text = f.read()

with open(directory + "/../DOCS.md", "w") as f:
    f.write(text)
