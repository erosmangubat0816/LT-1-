#This asks the user for the value of thenumber of notebooks and boxes
number_of_notebooks = int(input((print("What is the total amount of notebooks?"))))
box_number = int(input((print("How many of them fit inside one box?"))))

#We use an if statement just in case if the value of box_number is greater than number_of_notebooks,we place the notebooks in loose pack
if box_number < number_of_notebooks: 
    total_in_box = print("the total number of boxes tha can be filled is:", number_of_notebooks//box_number)
    leftover = print("the number of leftover notebooks is:", number_of_notebooks % box_number, "left" )

elif box_number > number_of_notebooks:
    print("A full box cannot be filled, therefore", number_of_notebooks ,"shall go in the loose pack")