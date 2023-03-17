# Import the necessary libraries
import pymysql as idk
from django.shortcuts import render

# Connect to the MySQL server and extract the data
conn = idk.connect(user='root', password='mysql', host='localhost', database='ch',port=3306)
cursor = conn.cursor()
cursor.execute('SELECT * FROM ch')
data = cursor.fetchall()

# Define a Django view to render the data in a template
def table_view(request):
    return render(request, 'table.html', {'data': data})
zen=list(data[0])
print(zen,data)