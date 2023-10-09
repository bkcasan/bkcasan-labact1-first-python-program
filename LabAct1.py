# KIRBY LAB ACTIVITY 1
# Please enter your weight in pounds
lbs_input = input("Enter weight in pounds")
lbs = int(lbs_input)
kg = lbs * 0.453592

print(f"Weight in pounds (lbs): {lbs}")
print(f"Weight converted to kilograms (kg): {kg}")
print("=====================================================")

# Please enter the distance in miles
mi_input = input("enter distance in miles")
mi = int(mi_input) 
km = mi * 1.60934

print(f"Length in miles (mi): {mi}")
print(f"Length converted to kilometers (km): {km}")
print("=====================================================")

# Please enter your temperature in Fahrenheit
f_input = input("Enter temperature in Fahrenheit")
f = int(f_input)
c = (f - 32) * 5/9

print(f"Temperature in Fahrenheit (f): {f}\u00b0F")
print(f"Temperature converted to Celsius (c): {round(c, 2)}\u00b0C")
print("=====================================================")

# make a list of the ages of the students
# please enter ages of students
while True:
    try:
        Student1 = int(input("Student 1 age ?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:
        #age was successfully parsed!
        #we're ready to exit the loop.
        break

while True:
    try:
        Student2 = int(input("Student 2 age ?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:
        break

while True:
    try:
        Student3 = int(input("Student 3 age ?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:
        break

while True:
    try:
        Student4 = int(input("Student 4 age ?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:
        break

while True:
    try:
        Student5 = int(input("Student 5 age ?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:
        break

while True:
    try:
        Student6 = int(input("Student 6 age ?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:
        break

while True:
    try:
        Student7 = int(input("Student 7 age ?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:
        break

while True:
    try:
        Student8 = int(input("Student 8 age ?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:
        break

while True:
    try:
        Student9 = int(input("Student 9 age ?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:
        break

while True:
    try:
        Student10 = int(input("Student 10 age ?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:
        break

A, B, C, D, E = Student1, Student2, Student3, Student4, Student5
F, G, H, I, J = Student6, Student7, Student8, Student9, Student10
average = (A + B + C + D + E + F + G + H + I + J) / 10

print(f"Student 1: {Student1} ")
print(f"Student 2: {Student2}")
print(f"Student 3: {Student3}")
print(f"Student 4: {Student4}")
print(f"Student 5: {Student5}")
print(f"Student 6: {Student6}")
print(f"Student 7: {Student7}")
print(f"Student 8: {Student8}")
print(f"Student 9: {Student9}")
print(f"Student 10: {Student10}")
print(f"The average age of the students is: {average}")
print("======================================================")

# Characters
name1 = "Sung Jin-Woo"
name2 = "Cha Hae-In"
name3 = "Go Gun-Hee"
name4 = "Yoo Jin-Ho"
name5 = "Thomas Andre"

# Equipment names
tool1 = "Red Knight's Sword"
tool2 = "Azure Dragon's Armor"
tool3 = "Goblin Slayer's Bow"
tool4 = "Hunter's Cloak"
tool5 = "Berserker Gauntlets"

# Abilities
skill1 = "Shadow Summon"
skill2 = "Berserk"
skill3 = "Dragon's Roar"
skill4 = "Sorcerer's Gaze"
skill5 = "Mirage Step"

# storyline
story = f"""
As {name1} attacks the Beast Monarch with his {tool1}, {name2} prepares her
skill {skill2} in order to gain some ground between her and the Monarch. Its a 
2v1 and yet both hunters are having a hard time. {name3} joins the battle and 
immediately attacks with his {skill3}. The Beast Monarch being completely 
distracted by {name1} and {name2} gets a direct hit from the "skill3". The hunters
regrouped in order to prepare for the next attack. As they wait for the smoke to settle
{name3} tells the {name1} and {name2} that the others are on their way. The Beast Monarch
stood there unfazed as the smoke slowly starts clearing out. {name1} uses his skill 
{skill1} to deal with the Beast Monarch's minions and {name2} equips her {tool2} to reduce
incoming damage. The Beast Monarch activates {skill2} and {skill4} and charges 
towards {name3} and sends him flying to the sky. {name1} shouts and cries for help
but the Beast Monarch just laughs at him and throws a punch, but to his surprise
{name4} and {name5} jumps into action stopping the fist of the Beast Monarch.
The monarch backs up and assesses the situation. {name4} uses the {tool4} to activate
its invisibility skill and proceeds to find a spot where he could use {tool3}. {name5}
attacks the Beast Monarch with his {tool5} and exchange blows with him. The fight continues
until all the heroes were exhausted. The battle field was full of smoke, nearly all of the 
heroes have fallen, except for {name1} who has successfully pierced the Beast Monarch's heart.
"""
print(story)
