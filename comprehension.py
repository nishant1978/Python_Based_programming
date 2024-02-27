my_List = [char for char in 'hello']
my_List2 = [char for char in range(1,101)]
my_list_square = [char for char in list(map(lambda item:item**2, my_List2))]
my_list_square_new_style = [num**2 for num in range(1,100) if num % 2 ==0]
dic ={
    'a': 2,
    'b': 4
}

adhoc_List = ['a','b','a','d','e','f']

#print(my_list_square_new_style)

#print(my_List)
#print(my_List2)
#print(my_list_square)

# with set (Change bracket to curly bracket) and dictionary 
my_set = {char for char in 'hello'}
my_dic = {k:v*2 for k,v in dic.items() if v % 4 ==0}
my_dic2 = {num:num*2 for num in [1,2,3,4]}

#How to find duplicates
duplicates = list(set(x for x in adhoc_List if adhoc_List.count(x) > 1))

print(duplicates)


#print(my_dic2)
