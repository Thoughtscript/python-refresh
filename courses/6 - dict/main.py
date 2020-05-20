# enter mbox-short.txt

name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)

counter = dict()
most = 0
emailOfMost = ""

for line in handle:
    lineBuffer = line.split(" ")
    if (lineBuffer[0] == "From"):
        email = lineBuffer[1]
        counter[email] = counter.get(email, 0) + 1
        if (counter.get(email, 0) > most):
            most = counter.get(email)
            emailOfMost = email

print(str(emailOfMost) + " " + str(most))