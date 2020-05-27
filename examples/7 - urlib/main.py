import urllib.request, urllib.parse, urllib.error

print("\nExample One\n")
exampleOne = urllib.request.urlopen("http://jsonplaceholder.typicode.com/posts/1")
for line in exampleOne:
    print(line.decode().rstrip())

# {
#   "userId": 1,
#   "id": 1,
#   "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
#   "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
# }

print("\nExample Two\n")

exampleTwo = urllib.request.urlopen("http://jsonplaceholder.typicode.com/posts")
for line in exampleTwo:
    print(line.decode().rstrip())

# GET ALL printed out