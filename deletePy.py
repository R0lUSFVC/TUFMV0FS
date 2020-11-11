import os

def delete(file):
    if os.path.exists("NotMalware.py"):
        os.remove("NotMalware.py")
    else:
        print("The file does not exist")
