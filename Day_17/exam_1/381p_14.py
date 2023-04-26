# import random

# # ask the user for three integer n, m, k where k > (m*n)
# # create a two dimensional table (list of lists) x of size n*m
# # populate the list with n*m unique random integers in the range 1 through k

# # 3 x 4 array
# # 3 rows, 4 columns
# # a[c][r]

# # a[1][2]

# # row 0 (array 0): 1, 2, 3, 4
# # row 1 (array 1): 1, 2, 3, 4
# # row 2 (array 2): 1, 2, 3, 4



# # in this problem
# # final answer is gonna be n rows, m columns
# # answer_array
# # answer_array[row][column] = 

# from xml.dom.pulldom import CHARACTERS


# def two_dimensional_randoms():
#   n = int(input("enter n: "))
#   m = int(input("enter m: "))
#   k = int(input("enter k: "))
#   if k <= (m*n):
#     print("You have not entered numbers that meet the requirements")
#     return
  
#   already_used_numbers = set()
#   two_dimensional_solution = [] #technically one-dimensional right now, but we can add lists inside of it
#   #if I add three lists to this [[1,2,3],[2,3,4],[3,4,5]]
#   #by default starts at 0, goes until but not including END_INDEX

#   # loop through all of the rows, one iteration per row
#   for x in range(n): 

#     #all the numbers we have so far in the current iteration for the row. clear at the start of the row
#     current_row_numbers = []

#     #loop through as many columns as specified
#     for y in range(m):

#       #we need the number to be unique. start off by assuming it's not unique to just make sure the while loop runs at least once
#       number_unique = False

#       #keep searching until we get a unique number
#       while number_unique is False:

#         #generate a random number on the specified interval
#         random_number = random.randint(1,k)

#         #only allow the program to continue and add the new number if it is not already used
#         if random_number not in already_used_numbers:
#           number_unique = True

#           # add the number we find to the set
#           already_used_numbers.add(random_number)

#       #once we find a unique number, add it to the current_row_numbers
#       current_row_numbers.append(random_number)
#       # looking inside current_row_numbers
#       # after the first iteration [17]
#       # then [17,34]
#       #etc until you finish going through all the columns

#     #when a full row is finished, add it to the two_dimensional_solution 
#     two_dimensional_solution.append(current_row_numbers)
#     #what this will look like as it grows:
#     #it will start off empty []
#     # [[17,34]] [] -> add to that list [17,34] which is being considered to an element
#     # on the second iteration
#     #[[17,34],[18,22]] -> add to the list [18,22]
#     #etc until you finish filling up all the rows

#   print(two_dimensional_solution)


# two_dimensional_randoms()


#   # example_string = "example"
  
#   #one way to iterate through a string
#   # for character in example_string:
#   #   print(character)

#   #another way to iterate through a string
#   # for character_index in range(len(example_string)):
#   #   print(character_index)
#   #   print(example_string[character_index])

# stable sort what it is
# the elements that are the same that come in a certain order need to stay in that order
# [Judge, Alonso, Trout, Harper]
# Judge:37, Alonso: 40, Trout: 37, Harper:43
# sort from most HRs to least HRs
# both of the following are valid
# Harper, Alonso, Trout, Judge
# a stable sort would be able to guarantee: Harper, Alonso, Judge, Trout (every single time)
# a stable sort is a sort that guarantees that for elements with the same key value, the order they enter with is the order they exit with

# seniority used as a tie-breaker, guaranteed

#try coding insertion sort

def insertion_sort(number_array):
  correctly_placed_numbers = 0
  for number_to_place in number_array:
    
    # to make sure when we have one correct number placed, we have to start by checking correctly_placed_numbers minus one
    # we go until -1 because we want to include going through the zero index, for when we hit the front of the array
    # python does not execute the loop for the end_index. in this case, that's -1. but it will execute everything until then, which means in our case, it will execute 0 which is what we want
    for index_of_previously_seen_number in range(correctly_placed_numbers, -1, -1):
      
      #check if we hit the beginning of the list, in which case place the element
      if index_of_previously_seen_number == 0:
        number_array[0] = number_to_place
        break

      #when we run this, suppose element 0 = 5, element 1 = 2
      #correctly_placed_numbers = 1, so the first index we are gonna look at is 1
      #that is actually where 2 is already located!
      #but the reason we're doing that is that if we do not, then when 2 is examined, we will already be at index 0
      #the if loop above will execute, and we will "lose" 5 and never actually place it
      #since we want to move 5 first, we are gonna start at index 1, where 2 is currently located, to give us room to move 5 into

      previously_seen_number = number_array[index_of_previously_seen_number - 1]

      #stable sort: insertion sort is stable, because this is < and it is not <=
      #this is the key component that makes it a stable sort!
      if number_to_place < previously_seen_number:

        #move the previously_seen_number over by one to create space for the new number
        number_array[index_of_previously_seen_number] = previously_seen_number
        #this connects to the huge comment thing above
        #we are placing 5 where we are RIGHT NOW when we are looking at 2 - which is index 1, where 2 is currently located
      else:
        
        #place the number_to_compare in the current index
        number_array[index_of_previously_seen_number] = number_to_place
        break

    correctly_placed_numbers += 1
        
  return number_array



# for (int i = 10; i >= 0; i--)
# all python lets you do
# for (int i = 10; i > -1; i--)

    



number_array = [2,5,7,7,4,13,1,8]
print(insertion_sort(number_array))






# mergesort, insertion sort, 