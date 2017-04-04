list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2,2,"hello"]

def compare_list(userInput):
    if list_one == list_two:
        print("The lists are the same.")
    if list_one != list_two:
        print("The lists are not the same.")
compare_list((list_one, list_two))
