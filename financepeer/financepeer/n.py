import mysql.connector
import json
 
mydb = mysql.connector.Connect(host='localhost',user='root',passwd='@975203iitD',port=3306,database='financepeer',auth_plugin='mysql_native_password')
cur=mydb.cursor()

f = open('data.json')
data = json.load(f)
#print(data)
for obj in data:
    userID=obj['userID']
    ID=obj['ID']
    title=obj['title']
    body=obj['body']
    cur.execute('insert into items values(%s,%s,%s,%s)',userID,ID,title,body)
    #print(obj)


#cur.execute('insert into items values(1,1,"sunt aut facere repellat provident occaecati excepturi optio reprehenderit","quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto")')
#cur.execute('insert into items values(1,1,"sunt aut facere repellat provident occaecati excepturi optio reprehenderit","quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto")')

cur.execute("select * from items")
myresult =cur.fetchall()
for x in myresult:
  print(x)