import math 
import csv
with open("C:/Users/HOME/Downloads/d.csv", newline="") as d:
    data = csv.reader(d)
    filedata = list(data)
file = filedata[0]
def mean(file):
    length = len(file)
    total=0
    for i in file:
        total+=int(i)
    mean = total/length
    return mean
print(mean)
#squaring and evaluating the values
squaredlist = []
for i in file:
    a = int(i)-mean(file)
    a = a**2
    squaredlist.append(a)
#evaluating the sum  
sum = 0
for i in squaredlist:
    sum = sum+i
#dividing the sum by total values
result = sum/(len(file)-1)  
#getting the standard deviation
stddev = math.sqrt(result)
print(stddev)   

