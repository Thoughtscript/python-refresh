# enter mbox-short.txt

fname = input("Enter file name: ")
if len(fname) < 1: fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    lineBuffer = line.split(" ")
    if (lineBuffer[0] == 'From'):
        count = count + 1
        print(lineBuffer[1])

print("There were", count, "lines in the file with From as the first word")

