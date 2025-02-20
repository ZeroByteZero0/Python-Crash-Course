#LISTS
#   *list: a collection of items in a particular order which are denoted by the [index]
#   *mutable, meaning they may be changed
#   *the items may be non-homogeneous
#   *([ ]) brackets are used to enclose the contents of the list
#   *printing the list will print out the contents separated by commas and includes the brackets
#   *individual 'elements' can be treated as strings from the list, called by specifying the index
#   *bicycles[0] would return 'trek', you can use string methods in this instance
bicycles = ['trek', 'giant', 'redline', 'specialized']
print(bicycles)
print(bicycles[0].title())

#INDEX POSITIONS START AT 0, NOT AT 1
#   *most programming languages do the same and begin 'counting' a list's elements from 0
#   *this introduces 'off-by-one' errors where unexpected results occur
#   *[-1] returns the last element in a list, [-2] returns second to last element, etc...
print(bicycles[-1].title())

#USING INDIVIDUAL VALUES FROM A LIST
#   *you can use a value from a list in the same way as you would any other variable
message = f"Hello World I have a {bicycles[-1].title()}"
print(message)

#MODIFYING, ADDING, AND REMOVING ELEMENTS
#   *most lists are made to be 'dynamic' meaning the list may be modified
#   *you can reassign any value in a list, just remember to use the correct index
list_1 = ['honda','yamaha','suzuki','ducati']
print(list_1)
list_1[0] = 'aprilla'
print(list_1)

#ADDING ITEMS TO A LIST
#   *(append) method adds an item to the end of a list
list_2 = ['a','b','c']
print(list_2)
list_2.append('d')
print(list_2)

#INSERTING ITEMS TO A LIST
#   *(insert) method adds an item at the specified index, first specify index, then add item
list_3 = ['honda', 'yamaha', 'suzuki']
print(list_3)
list_3.insert(0,'royal enfield')
print(list_3)

#DELETING ITEMS FROM A LIST
#   *(del) statement will delete the item at specified index, makes value inaccessible
list_4 = ['honda', 'yamaha', 'suzuki']
print(list_4)
del list_4[0]
print(list_4)

#REMOVING ITEMS USING THE POP METHOD
#   *(pop) removes the item at the end of the list and allows you to work with the data
list_5 = ['honda', 'yamaha', 'suzuki']
#   *popping a value from the list and storing in a variable named stored_pop
stored_pop = list_5.pop()
print(list_5)
print(stored_pop)
#POPPING ITEMS FROM ANY POSITION IN A LIST
#   *you may also pop a value from a specified index
stored_pop2 = list_5.pop(0)
print(stored_pop2)

#REMOVING AN ITEM BY VALUE
#   *(remove) method allows you to remove an item from the list when the index is unknown
list_6 = ['honda','yamaha','ducati']
print(list_6)
list_6.remove('ducati')
print(list_6)

#   *can also use remove method to loop through a list to take out every instance of a value
#   *can also save the value being removed to a variable

#ORGANIZING A LIST
#   *Python includes methods that allow lists to be sorted
#   *(sort) method returns a list as alphabetically organized and changes order of list forever
#   *(reverse=True) parameter in (sort) method returns reverse alphabetical ordered list
cars = ['audi','bmw','subaru','toyota', 'ford','suzuki','alpha-romeo','saab','mini-cooper']
cars.sort()
print(cars)

#   *(sorted) method allows you to sort a list temporarily without permanently modifying the list
#   *(reverse=True) parameter also works for (sorted) method returns reverse-alphabetical list
#   *important to note that capital letters are sorted differently than lowercase letters
cars = ['bmw','tesla','ford','gmc','chevy','dodge','Porsche','Bugatti']
print(sorted(cars))
print(cars)


#PRINTING A LIST IN REVERSE ORDER
#   *(reverse) method doesn't sort alphabetically but permanently reverses a lists order
cars.reverse()
print(cars)

#FINDING THE LENGTH OF A LIST
#   *(len) function returns the length of a list, starts at 1, so there are no off-by-one errors
print(len(cars))

#AVOIDING INDEXING ERRORS WHEN WORKING WITH LISTS
#   *lists have indexes, indexing begins at (0)
#   *[-1] will always return last item in a list unless the list is empty []
#   *print(cars[8]) would return an error
#   *print(cars[-1]) would return last item in a list
#   *if an indexing error occurs, print list to see current status of the contents
#   *sometimes adjusting the index by one results in solving the error
#   *lists are dynamically handled by different functions and methods
#   *checking the status of the list helps to sort out any logical errors