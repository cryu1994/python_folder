
#first, i wanna go through the array
#second, i wanna pick some valuse in the array
#third, i wanna select the rest of the words assign by the first_vals
l = ['hello','world','my','name','is','Anna']
def find_char(x):
    words_count = 0
    new_word = []
    for i in x:
        while i < len(x):
            for j in i:
                if i == x[j]:
                    j += i
                    words_count += 1
    print i.sort(x)
find_char("ojjeje")
