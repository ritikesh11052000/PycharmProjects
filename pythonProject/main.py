# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
#
#
# print(f'Pssst, the solution is {chosen_word}.')
#
#
# display = []
# word_length = len(chosen_word)
# for _ in range(word_length):
#     display += "_"
#
#
# while not word_length:
#
#
#
#
# guess = input("Guess a letter: ").lower()
#
#
# for position in range(word_length):
#     letter = chosen_word[position]
#
#     if letter == guess:
#         display[position] = letter
#
# print(display)












# for letter in word:
#     display += "_"
# print(display)

# for i in range(len(word)):
#     display += "_"
# print(f"totoal letters in word are : {i}")
# print(display)















# sky = "clear"
# def my_function():
#   if sky == "clear":
#     print("blue")
#   elif sky == "cloudy":
#     print("grey")
#   print("hello")
# print("word")




































# #Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# # Eazy Level - Order not randomised:
# # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""
#
# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)
#
# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)
#
# print(f"your pass is : {password}")
#
#




















# import random
#
# # Write your code here 👇
# # list.random
#
#
#
# target = 100
# for number in range (1,target+1):
#   if number %3 == 0 and number %5 == 0:
#     print("fizzBuzz")
#   elif number % 3 == 0 :
#     print("fizz")
#   elif number % 5 == 0 :
#     print("buzz")
#   else:
#     print(number)
#




























# target = int(input())  # Enter a number between 0 and 1000
# # 🚨 Do not change the code above ☝️
#
# # Write your code here 👇
#
# # evnn_num = 0
#
# # for num in range(2,target + 1,2):
# #   # print(num)
# #   evnn_num += num
# # print(evnn_num)
#
# #second method : -
# sum = 0
# for num in range(1, target + 1):
#   # print(num)
#   if num % 2 == 0:
#     sum += num
# print(sum)



























# for i in range(2,22,2):
#   print(i)















# total = 0
# for num in range(2,201,2):
#   # total +=1
#   # print(total)
#   print(num)

















# # Input a list of student scores
# student_scores = input("enter students score : ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
#
# heighest_score = 0
# for score in student_scores:
#   if score>heighest_score:
#     heighest_score = score
# print(heighest_score)












# # Input a list of student scores
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
#
# # Write your code below this row 👇
# # print(f"The highest score in the class is: {max(student_scores)}")
#
# heighest_score = 0
#
# for score in student_scores:
#   if score > heighest_score:
#     heighest_score = score
# print(f"The highest score in the class is: {heighest_score}")
















# # Input a Python list of student heights
# student_heights = input("enter students heights : ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
#
# total_height = 0
#
# for heights in student_heights:
#   total_height += heights
# print(f"total height = {total_height}")
#
#
# number_of_student = 0
# for student in student_heights:
#   number_of_student +=1
# print(f"number of students = {number_of_student}")
#
#
# average_height = round(total_height/number_of_student)
# print(f"average height = {average_height}")
#
















"""crew = ["luffy", "zoro", "sanji"]
for crew_m in crew:
    print(crew_m)
    print(crew_m + " fight")
print(crew)
"""





















# import random
# print("welcome to password generator")
# letter = int(input("enter the number of letter you like in your password"))
# symbols = int(input("how many number of symbols do you like in your password"))
# number = int(input("how many digits or number you want in your password"))
#
# random_num = random.randint(1,10)
# print(random_num)





















"""import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print(f"{rock},\n {paper},\n {scissors}")
img = [rock,paper,scissors]

user = int(input("enter 0 - rock , 1 - paper , 2 -scissors  : \n "))
print(f"your choice is : {user}")

if user >= 3 or user < 0:
    print("invalid number pleas select between 0 to 2")
else:

    print(img[user])

    robot = random.randint(0,2)

    print(f"bot choice: {robot} ")
    print(img[robot])



    if user == 0 and robot == 2:
        print("you wins !")
    elif robot == 0 and user == 2:
        print("you lose")

    elif robot > user:
        print("you lose")
    elif user > robot:
        print("you win!")

    elif robot == user:
        print("It's a draw")

"""











"""l1 = [" ", " ", " "]
l2 = [" ", " ", " "]
l3 = [" ", " ", " "]

map = [l1, l2, l3]

print("Where do you want to put your treasure chest? It will be displayed as X.")
position = input("Enter the position (e.g., A1, B2, C3): ")
letter = position[0].upper()

a_b_c = ["A", "B", "C"]

L_index = a_b_c.index(letter)
N_index = int(position[1]) - 1
map[N_index][L_index] = "X"

print(f"{l1}\n{l2}\n{l3}")


"""





#
"""
#line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("where you want to put 'x' e.g (a1,a2,a3)(b1,b2,b2,b3)(c1,c2,c3) : ") # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
# Your code below
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
"""


































"""list = ["Afghanistan", "Albania", "Algeria", "Andorra",
        "Angola", "Antigua and Barbuda", "Argentina",
        "Armenia", "Australia", "Austria", "Azerbaijan",
        "Bahamas", "Bahrain", "Bangladesh", "Barbados",
        "Belarus", "Belgium", "Belize", "Benin", "Bhutan",
        "Bolivia", "Bosnia and Herzegovina", "Botswana",
        "Brazil", "Brunei", "Bulgaria", "Burkina Faso",
        "Burundi", "Cabo Verde", "Cambodia", "Cameroon",
        "Canada", "Central African Republic", "Chad",
        "Chile", "China", "Colombia", "Comoros", "Congo",
        "Democratic Republic of the", "Congo",
       ]

anime_list = [
    "Naruto",
    "One Piece",
    "Dragon Ball Z",
    "Death Note",
    "Attack on Titan",
    "My Hero Academia",
    "Fullmetal Alchemist: Brotherhood",
    "One Punch Man",
    "Tokyo Ghoul",
    "Sword Art Online",
    "Hunter x Hunter",
    "Bleach",
    "Fairy Tail",
    "Demon Slayer",
    "Steins;Gate",
    "Code Geass",
    "Cowboy Bebop",
    "Neon Genesis Evangelion",
    "Black Clover",
    "Dragon Ball",
    "JoJo's Bizarre Adventure",
    "The Seven Deadly Sins",
    "Naruto Shippuden",
    "Re:Zero",
    "Mob Psycho 100",
    "The Promised Neverland",
    "Overlord",
    "Gurren Lagann",
    "Erased",
    "Haikyuu!!",
    "Attack on Titan: Junior High",
    "Black Butler",
    "Death Parade",
    "Durarara!!",
    "Noragami",
    "No Game No Life",
    "Assassination Classroom",
    "Akame ga Kill!",
    "Fate/stay night",
    "Blue Exorcist",
    "Parasyte",
    "Soul Eater",
    "Toradora!",
    "High School DxD",
    "The Rising of the Shield Hero",
    "Fruits Basket",
    "Danganronpa",
    "Hellsing",
    "Magi: The Labyrinth of Magic"
]

print(anime_list,list)

length = len(list)

print(f"{length}")

print(f"{list[4]}")





"""














"""

names = ["sanji","nami","luffy","zoro","ussap","robin","choper","jinbme","franky","Brook","zeus"]

# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random

num_item = len(names)

random_choice = random.randint(0,num_item -1)

p_w_pay = names[random_choice]
print(f"{p_w_pay} is going to buy the meal today!")


"""













"""import random
list = ["luffy", "zoro","sanji","jinmbe"]
list[3] = "usap"
list.extend(["ace","sabo"])
print(list)
"""













"""import random
random_int = random.randint(0,1)
if random_int == 1:
    print("heads")
else:
   print("tails")

"""























"""import random
#import module
#print(module.pi)
random_int = random.randint(1,10)
print(random_int)


random_float = random.random() * 5
print(random_float)

love_score = random.randint(1,100)
print(f"score is {love_score}")


"""




























#print(
'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************

'''
#)
"""print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".:  ').lower()

if choice1 == "left":
    choice2 = input(
        'You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. :  ').lower()

    if choice2 == "wait":
        choice3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors: 'red', 'blue', and 'yellow'. Which color do you choose? : ").lower()

        if choice3 == "red":
            print("Burned by fire. Game Over.")
        elif choice3 == "blue":
            print("Eaten by beasts. Game Over.")
        elif choice3 == "yellow":
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")"""



























"""print("welcome to the roller coaster")
height = int(input("what's you height : "))
bill = 0

if height >= 120:
  print("you can ride")
  age = int(input("what's your age : "))
  if age <= 4:
    bill = 3
    print("please pay $4")
  elif age <=12:
    bill = 5
    print("please pay $5,")
  elif age <= 18:
    bill = 8
    print("please pay $7")
  elif age>=45 and age <=55:#and logical operator
      print("free ride")
  else:
    bill = 10
    print("please pay $12.")

  photo = input("do you want a photo ? Y / N : ")
  if photo == "Y":
    bill += 3
    print(f"your bill is {bill}")
else:
  print("you are under age or you height is less")


"""






























"""print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # What size pizza do you want? "S", "M", or "L"
add_pepperoni = input()  # Do you want pepperoni? "Y" or "N"
extra_cheese = input()  # Do you want extra cheese? "Y" or "N"

# Your code below this line 👇
bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")"""


















"""print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bill = 0
if size == "S":
  bill += 15
elif size == "M":
    bill += 20
else :
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill +=2
  else:
    bill +=3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")



"""






















"""
#print("welcome to the roller coaster")
height = int(input("what's you height : "))
bill = 0

if height >= 120:
  print("you can ride")
  age = int(input("what's your age : "))
  if age <= 4:
    bill = 3
    print("please pay $4")
  elif age <=12:
    bill = 5
    print("please pay $5,")
  elif age <= 18:
    bill = 8
    print("please pay $7")
  else:
    bill = 10
    print("please pay $12.")

  photo = input("do you want a photo ? Y / N : ")
  if photo == "Y":
    bill += 3
    print(f"your bill is {bill}")
else:
  print("you are under age or you height is less")
"""


















"""# Which year do you want to check?
year = int(input("Enter the year : "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")
"""























"""# Enter your height in meters e.g., 1.55
height = float(input("Enter you height: "))
# Enter your weight in kilograms e.g., 72
weight = int(input("Enter your weight: "))
# 🚨 Don't change the code above 👆
BMI = weight / (height * height)"""
"""print(height)
print(weight)"""
"""# Write your code below this line 👇
if BMI < 18.5:
  print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
  print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
  print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
  print(f"Your BMI is {BMI}, you are obese.")


else:
  print(f"Your BMI is {BMI}, you are  clinically obese.")"""

"""print("welcome to the coster")
height = int(input("what's you height :"))

if height >= 120:
  print("you can ride")
  age = int(input("what's your age"))
  if age <= 4:
    print("please pay $4")
  elif age <=12:
    print("please pay $5,")
  elif age <= 18:
    print("please pay $7")
  else:
    print("please pay $12.")


else:
  print("you are under age or you height is less")"""




















"""# Which number do you want to check?
number = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if number % 2 == 0:
  print("This is an even number.")
  print(number)
else:
  print("This is an odd number.")
  print(number)"""



















"""#Day 2 - udemy python course task/Project: -
print("welcome to the tip claculator")
bill = float(input("what was the total bill-"))
tip = int(input("what percentage tip would you like to give ? 10, 12, or 15? : -"))
people = int(input("how many people to spilt the bill-"))

bill_with_tip = tip/100 * bill +bill
#tip_as_percent = tip/100
#total_tip_amount = bill * tip_as_percent

#total_bill = bill + total_tip_amount

bill_per_person = bill_with_tip/people
final_amount = "{:2f}".format(bill_per_person)
print(int(input(f" each person should pay- {final_amount}")))

"""
































"""import random

def get_player_names():
    player1_name = input("Enter player 1's name: ")
    player2_name = input("Enter player 2's name: ")
    return player1_name, player2_name

def get_player_symbol():
    while True:
        player_symbol = input("Do you want to be X or O: ").upper()
        if player_symbol in ['X', 'O']:
            return player_symbol
        else:
            print("Invalid input. Please choose X or O.")

def print_board(board):
    print("   0 1 2")
    for i, row in enumerate(board):
        print(f"{i}  {' '.join(cell if cell else ' ' for cell in row)}")

def make_move_for_robot(board, opponent_symbol):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == "":
            board[row][col] = opponent_symbol
            break

def get_move(board, player_symbol, player_name):
    while True:
        try:
            row = int(input(f"{player_name}, enter row number (0-2): "))
            col = int(input(f"{player_name}, enter column number (0-2): "))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == "":
                board[row][col] = player_symbol
                break
            else:
                print("Invalid input. Please enter a valid row and column number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    player1_name, player2_name = get_player_names()
    player1_symbol = get_player_symbol()
    player2_symbol = "O" if player1_symbol == "X" else "X"
    board = [['' for _ in range(3)] for _ in range(3)]

    opponent_choice = input("Do you want to play against a robot (r) or a person (p): ").lower()
    print_board(board)

    current_turn = player1_symbol  # Start with player 1's turn

    while True:
        if opponent_choice == "p":
            if current_turn == player1_symbol:
                get_move(board, player1_symbol, player1_name)
            else:
                get_move(board, player2_symbol, player2_name)
        else:
            if current_turn == player1_symbol:
                get_move(board, player1_symbol, player1_name)
            else:
                print("Robot's turn:")
                make_move_for_robot(board, player2_symbol)

        print_board(board)
        winner = check_win(board)
        if winner:
            if winner == player1_symbol:
                print(f"{player1_name} wins!")
            else:
                print(f"{player2_name} wins!")
            break
        if check_tie(board):
            print("It's a tie!")
            break

        current_turn = player2_symbol if current_turn == player1_symbol else player1_symbol  # Switch turns

def check_win(board):
    for player in ['X', 'O']:
        for row in board:
            if all(cell == player for cell in row):
                return player
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return player
        if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
            return player
    return None

def check_tie(board):
    return all(all(cell != "" for cell in row) for row in board)

if __name__ == "__main__":
    main()
"""



"""def extendList(val, list=None):
  if list is None:
    list = []
  list.append(val)
  return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)"""






"""temp = input("enter ur temp")
temp = float(temp)
print(temp)
temp = temp + 1.5
print(type(temp))
print(temp)
"""













"""M_list = [1,2,3,4]
count = 1
for item in M_list:
    if item == 4:
        print("item matched")
        count +=1
        break
print("found at loaction", count)
"""










#list1 = [4,3,5,1,2]
#list2 = ['LUFFY','ZORO','SANJI','JINBE']
#del list2[3]
#print(list2)
#list3 = list2.copy()
#list2.pop()
#print(list2)
#print(list3)
#list2.reverse()
#print(list2)
#list1.sort()
#print(list1)
#print(list2.count('ZORO'))
#print(list2.index('ZORO'))
#list2.insert(1,'CHOPPER')
#list2.remove('JINBE')
#list2.clear()
#print(list2)
"""list2.append('CHOPPER')
list.extend(list2)
print(list2)
print(len(list2))"""




















"""one_piece = list(('LUFFY',17,True))
print(one_piece[0])
print(type(one_piece))"""


















"""sentance = input('enter your sentance : ')
print('your sentance is: '+sentance)
world = input('enter the word to replace: ')
word1 = input('enter the word to replace: ')
print(sentance.replace(world,word1))"""


















"""
name = input('enter your name : ')
age = int(input('enter you age : '))

#print('so your name is ' + name + ' and your age is ' +str(age) + ' years old')
#print('so your name is ' + name + ' and your age is ', age)
"""

