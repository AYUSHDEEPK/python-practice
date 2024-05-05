#note= never make the file name as json
import json
#to use json we can use json module
from pathlib import Path
num=[1,2,3,4,5]
path=Path("python practice/files and excepions/numbers.json")
content=json.dumps(num)#this is used to store the given data in a specified file.
path.write_text(content)#this is used to write the given data in a specified file.
#if i want to read the json file,for that we can use json.loads()because we cant directly access the json formatted file.
#example
content=path.read_text()
username=json.loads(content)
print(f"welcome back,{username}")