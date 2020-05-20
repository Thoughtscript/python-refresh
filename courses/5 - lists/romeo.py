# enter 'romeo.txt'
fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    lineBuffer = line.rstrip().split(" ")
    for word in lineBuffer:
        if (word not in lst):
            lst.append(word)

lst.sort()
print(lst)