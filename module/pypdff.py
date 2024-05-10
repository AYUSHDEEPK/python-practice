import pypdf
a=pypdf.PdfReader('Eric Matthes.pdf')
str=''
for i in range(1,554):#i have run the loop according to the number of pages preset in the pdf.
    str+=a._get_page(i).extract_text()#this will extract the text from the pdf of given page.
    with open(f'hello/text{i}.txt','w',encoding="utf-8") as f:# it will create a new file every time 
         f.write(str)#this will write the extracted text.
         str=''#again the str will be empty.

#this will extract the pdf and convert it into text and save each page in each file in hello folder.
#make sure you have already made a hello folder.
