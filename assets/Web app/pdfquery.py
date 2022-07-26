import PyPDF2
#q=input('enter query')
def query(q,f):
    llist=[]
    pdf=open(f,'rb')
    pdfreader=PyPDF2.PdfFileReader(pdf)
    pages=pdfreader.numPages
    for i in range(pages):
        pageobj=pdfreader.getPage(i)
        lines=pageobj.extractText().split("\n")
        for line in lines:
            wordlist=line.split(" ")
            for word in wordlist:
                if q in word:
                    llist.append(line)
    return llist
        
	
	
