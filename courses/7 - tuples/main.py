# mbox-short.txt
## this answer required using tuples, lists, and dicts
## enter mbox-short.txt

name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)

listBuffer = list()

## iterate through to capture data

for line in handle:
    lineBuffer = line.split(" ")
    if (lineBuffer[0] == "From"):
        timeBuffer = lineBuffer[6].split(":")
        hour = int(timeBuffer[0])
        if (hour < 10):
            listBuffer.append(("0" + str(hour), 1))
        else:
            listBuffer.append((str(hour), 1))

listBuffer.sort()
counts = dict()

## then crunch

for (hour, count) in listBuffer:
    counts[hour] = counts.get(hour, 0) + 1

## print it out

for (hour, count) in counts.items():
    if (count > 0): print(str(hour) + " " + str(count))