#work with list comprehensions

#list comprehension is a one line for loop
#to get our list of departments, took our existing list of products, made anew list of departments, looped through items in the original list
#then we appended the original item to the new list. when we appended we conditionally appended them. can append a transformed version of htem. 
#looping through one list, can do this in one line
#for item in item (for item in existing list of items)
#will loop through each item in our list of items
#can use for filtering or transforming purposes, if using list comprehension for filtering purposes, will be more like
#def teams_from(city):
    #return [team for team in teams if team["city"] == city]
    #have everything in square brackets and then the fist item will be what you want to return
    #the variable that we want to call each item
    #if the variable is matching what we coded, will return that
    
    my_numbers = [1, 2, 3, 4, 5, 6, 7]

    print("ORIGINAL LIST", my_numbers)
    #how to get this to be 100,200,300,400, etc (multiply by 100)

    #will need to get a mapped list or a filtered list

    new_numbers = []
    for i in my_numbers:
            print(i)
#these are two different methods to do this multiplying
    mapped_list = [i * 100 for i in my_numbers]
    print("MAPPED LIST", mapped_list)
    exit()


    filtered_list = []
    for x in my_numbers:
        if x > 3:
            filtered_list.append(x)
            print("Filtered List:", filtered_list)

    new_filtered_list = [_____ for x in my_numbers x > 3]

    #list comprehensions exercise in his repository
    #did list comprehensions and approach to the grocery exercise