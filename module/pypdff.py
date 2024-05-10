import pypdf
a=pypdf.PdfReader('Eric Matthes.pdf')
str=''
for i in range(1,554):
    str+=a._get_page(i).extract_text()
    with open(f'hello/text{i}.txt','w',encoding="utf-8") as f:
         f.write(str)
         str=''

#this will extract the pdf and convert it into text and save each page in each file in hello folder.