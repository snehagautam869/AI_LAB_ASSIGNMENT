student = {"name": "sneha","age" : 23,"city":"mathura"}
print(student)
print(type (student))
student["city"]
student["email"] = "snehgautm2345"
print(student)
if  "email"in student:
    print(student["email"])
else:
    print("no email in student")
email = student.setdefault("email","not provided")
print(email)
name = student.setdefault("name","Unknown")
print(name)

words = ["ai","ml","ai","nlp","ml","ai"]
counts = {}
for w in words:
    counts[w] = counts.setdefault(w,0)+1
print(counts)

book = {"title":"python 101","pages":320}
if 'author' in book:
    print("Author exists")
else:
    print("Author does not exist")

book.setdefault("author" , "Unknown")

book['pages'] = 350

book["edition"] = 1
print(book)

