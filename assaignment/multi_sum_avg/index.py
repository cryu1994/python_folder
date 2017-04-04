for i in range(1, 1000):
    if i % 2 != 0:
        print i

#part II

for x in range(5, 100):
    if x % 5 == 0:
        print x

#sum list
a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a:
    sum += i
print sum

#avg list

g = [1, 2, 5, 10, 255, 3]
sum = 0
avg = 0
count = 0
for i in g:
    count += 1
    sum += i
avg = sum / count
print avg

