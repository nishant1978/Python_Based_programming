myList = [1,2,3,4,5]

def select_in_list(item):
    if item % 2 != 0:
        return item

print(list(filter(select_in_list,myList)))
	
