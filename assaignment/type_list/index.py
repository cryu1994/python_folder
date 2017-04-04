l =  [145, 23, "hello", "world"]
def type_list(x):
    str_count = 0
    int_count = 0
    sum_num = 0
    new_arr = "String: "
    for i in x:
        if type(i) == str:
            str_count += 1
            new_arr = new_arr + " " + i
        if type(i) == int or type(i) == float:
            int_count += 1
            sum_num += i
    if str_count == 0 and int_count > 0:
        print("this is a int type")
    elif str_count > 0 and int_count == 0:
        print("this is a str type")
    else:
        print("mixed type")
    print new_arr
    print "Sum: " + str(sum_num)

type_list(l)
