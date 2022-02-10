import csv

with open("data.csv",newline="") as x:
    reader = csv.reader(x)
    filedata = list(reader)
filedata.pop(0)
newdata = []
for y in range(len(filedata)):
    weight = filedata[y][2]
    newdata.append(float(weight))

n = len(newdata)
total = 0
for p in newdata:
    total +=p
mean = total/n
print(mean)