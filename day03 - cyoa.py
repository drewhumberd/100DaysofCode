from supportfiles.art import cyoa_logo
print(cyoa_logo)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
fail_choice = "To choose not to decide is its own decision. You are paralyzed by existential guilt. GAME OVER!"
first_fork = input('''
Your boat docks at a small pier. Before you are two paths:
one to the LEFT winds along the beach, one to the RIGHT 
leads deep into an overgrown thicket. Which way will you go?
''')
if first_fork == "right":
    print('''
You wander through the thicket for hours until you fall into
a hole concealed by brush. You die. Slowly. GAME OVER!
    ''')
elif first_fork == "left":
    second_fork = input('''
After following the path inland, you reach a small lake. You can see a boat
in the distance. Do you WAIT for the boat or SWIM across the lake?
    ''')
    if second_fork == "swim":
        print('''
You venture carefully into the lake. As the chilly water reaches your neck, you see
a dark shadow moving toward you. You turn to flee, but it's too late -- you're
devoured by a giant trout. GAME OVER!
        ''')
    elif second_fork == "wait":
        third_fork = input('''
After waiting an interminable amount of time, the boat returns to your side of the lake.
It's rowed by a tiny figure wearing a large cloak. You board the boat and cross the lake.
On the opposite side, you follow a path to a house with three doors. Do you try the RED
door, the YELLOW door, or the BLUE door?
        ''')
        if third_fork == "red":
            print('''
You open the red door. A gout of flame bursts from it and ignites you. It's too far to
reach the lake. You never learned to stop, drop, and roll. GAME OVER!
            ''')
        elif third_fork == "blue":
            print('''
You open the blue door. A horde of indescribable beasts pours forth. You are
trampled. Perhaps listening will serve you better next time. GAME OVER!
            ''')
        elif third_fork == "yellow":
            print('''
You have wisely chosen the color of gold. Clearly the designers of this puzzle enjoyed
heavy-handed symbolism. You open the door to find treasure beyond your wildest dreams
of avarice. GAME OVER (but in a good way!)
            ''')
        else:
            print(fail_choice)
    else:
        print(fail_choice)
else:
    print(fail_choice)