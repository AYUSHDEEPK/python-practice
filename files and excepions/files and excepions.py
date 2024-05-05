from pathlib import Path
path = Path('python practice/files and excepions/pi_digit.txt')
contents = path.read_text()
print(contents)
pat=Path('python practice/files and excepions/pi_digit.txt')
contents = path.read_text()#used to read text of a specified file.
lines=contents.splitlines()#used to split the content in lines and make them parts in list.
print(lines)#it will print in list.
#use can also print by giving indexing.
#for example
print(lines[2])
#if i want to write somthing in specified file,for that i can use path.write_text("......")
#if i want to write multiple lines in specified file i will write it like this
# content="i love programming\n"
# content+="i lov to code\n"
# path=Path('python practice/files and excepions/pi_digit.txt')
# path.write_text(content)
#storing data
#we can store data using json module
#json stands for javascript object notation was originally developed for javascript.however,it has since beocome a common format used bu many languages
