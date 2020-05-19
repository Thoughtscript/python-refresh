# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

# Reused variables for crunching avg
result = float(0)
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue

    startIndex = line.find("0.")
    endIndex = len(line)
    result += float(line[startIndex:endIndex])
    count = count + 1

avg = result / count
print("Average spam confidence: " + str(avg))