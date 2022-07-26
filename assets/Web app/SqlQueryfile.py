import pdfquery
import sqlite3
#Connection to the DB
conn = sqlite3.connect('memory.db')
cur = conn.cursor()
# Execute query on the sqlite DB
cur.execute("CREATE TABLE IF NOT EXISTS `Files` (`id` varchar(20) NOT NULL, `course` varchar(264) NULL,  `course_code` varchar(233) NULL, `pdf` varbinary(300000) NOT NULL, `text` varchar(200)  NOT NULL,`image` blob(200)  NOT NULL, PRIMARY KEY (`id`));")

def insert(a,b,c,d,e,f):
    cur.execute("INSERT INTO `Files` (`id`,`course`,`course_code`, `pdf`, `text`, `image`) VALUES(%a,%a,%a,%a,%a,%a);"%(a,b,c,d,e,f))
    

for i in range(17):
    #insert(i,i+1,i+2,"pdffile.pdf",i+4,i+5)
    pass
    
    

def select(a,b,c,d,e,f):
    rows=[]
    if a:
        qr=(cur.execute("SELECT * FROM `Files` WHERE `id`=%s"%(a)))
        for q in qr:
            rows.append(q)
        
    if b:
       qr=(cur.execute("SELECT * FROM `Files` WHERE `course`=%s"%(b)))
       for q in qr:
            rows.append(q)
    if c:
       qr=(cur.execute("SELECT * FROM `Files` WHERE `course_code`=%s"%(c)))
       for q in qr:
            rows.append(q)
    if d:
        #try:
        qr=(cur.execute("SELECT `pdf` FROM `Files` "))
        
        for q in qr:
            print(pdfquery.query(d,q[0]))
            print("file",q)
       
    if e:
       qr=(cur.execute("SELECT * FROM `Files` WHERE `text`=%s"%(e)))
       for q in qr:
            rows.append(q)
    if f:
        qr=(cur.execute("SELECT * FROM `Files` WHERE `image`=%s"%(f)))
        for q in qr:
            rows.append(q)
    
    #print(rows)
    return rows    
 
a=None
b=None
c=None
d='bears'
e=None
f=None
rows=select(a,b,c,d,e,f)
#rows=cur.execute("SELECT * FROM `Files`") 
#rows=cur.fetchall()
#print("first query")
for row in rows:
    print(row)
    pass

conn.commit()      

conn.close()
