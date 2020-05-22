import re

# partial_text.txt for testing - sum 27486, total of 7 values
# regex_sum_42.txt for testing - sum 445833, total of 90 values
# regex_sum_551919.txt for submission - total of 102 values

numCount = 0
sum = 0
#handle = open("partial_text.txt")
#handle = open("regex_sum_42.txt")
handle = open("regex_sum_551919.txt")

for line in handle:

    # wow this took me a while - I over-complicated it by using ^ and $
    start = re.findall("[0-9]+", line)

    for x in start:
        val = int(x)
        sum += int(val)
        numCount += 1

print("numCount: " + str(numCount))
print("sum: " + str(sum))