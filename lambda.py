#lambda are the anonymous function which is used only once. 
#We run and throw it away.#There is no name attached to the function. 
#Once the interpretor runs this line of code, runs it.
#But it does not remember it.

from functools import reduce

my_list = [ 1,2,3,4]
my_tuple = [ (2,3), (0,-2), (1,8), (4,10)]

print(list(map(lambda item:item * 2, my_list)))
print(list(filter(lambda item:item % 2 != 0, my_list)))

#square list
print(list(map(lambda item:item**2, my_list)))

#list as tuple to be sorted using 2nd parameter of the tuple
my_tuple.sort(key= lambda x : x[1])
print(my_tuple)

