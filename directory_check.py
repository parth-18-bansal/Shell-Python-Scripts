import os

directory = "./shellScripting"
if not os.path.exists(directory):
    print("Directory does not exist")
    os.makedirs(directory)
else:
    print("Directory exists")