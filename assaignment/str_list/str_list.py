x = [2,54,-2,7,12,98]
min_num = x[0]
max_num = x[0]

for i in x:
    if min_num >  i:
        min_num = i
    if  max_num < i:
        max_num = i
print max_num, min_num

#find and replace

str = "It's thanksgiving day. It's my birthday,too"
print str
print str.find("day")
str = str.replace("day", "month")
print str

#printing the first and last value in the array

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[len(x)-1]


#new_list

x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x.sort()
first = x[0:len(x)/2]
second = x[len(x)/2:len(x)]
second.insert(0, first)
print second
