import csv

with open("data.csv",newline="") as x:
    reader = csv.reader(x)
    filedata = list(reader)
filedata.pop(0)
newdata = []
for y in range(len(filedata)):
    height = filedata[y][2]
    newdata.append(float(height))

n = len(newdata)
newdata.sort()
if n%2==0:
    meadian1 = float(newdata[n//2])
    meadian2 = float(newdata[n//2+1])
    meadian = (meadian1+meadian2)/2
else:
    meadian = newdata[n//2]
print(meadian)