# Sign your name: Peggy Barley

  #1. Make the following program work. (3 mistakes)

midichlorians = float(input("Enter midichlorian count: "))

if midichlorians > 10000:
    print("You have serious Jedi potential")
else:
    print("Jedi, you will never be.")


 #2. Make the following program work. (3 mistakes)

x = int(input("Enter a number: "))
if x == 3:
    print("You entered 3")
else:
    print("Why would you enter", x, "? Why not 3?")


# 3. Make the following program work. (4 mistakes)

answer = input("What is the name of Poe Dameron's Droid? ")
if answer == "BB8":
    print("Correct!")
else:
    print("Incorrect! It is BB8.")


  # 4. Make the following program work. (4 mistakes)

jedi = str("Name one of the top 3 greatest Jedi.")
if jedi.lower() == "Yoda" or "Luke Skywalker" or "Obi-Wan Kenobi":
    print("That is correct!")
else:
    print("Incorrect!", jedi,"is not one of the top # greatest Jedi's")



 # 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
 #    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.

print()
print("Welcome to the Jedi Academy!")
print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")
print()

user_input = input("Choose a character?")
if user_input.lower() == "a" or "jedi master":
    sensitivity = 1000
    print("Sensitivity: ", sensitivity)
elif user_input.lower() == "b" or "sith lord":
    sensitivity = 900
    print("Sensitivity: ", sensitivity)
elif user_input.lower() == "c" or "droid":
    sensitivity = 0
    print("Sensitivity: ", sensitivity)
else:
    print("Not a choice!")
    print("Sensitivity: ")

