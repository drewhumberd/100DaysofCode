#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as ls:
    names_return = ls.readlines()

names = []
for name in names_return:
    names.append(name.strip("\n"))

for name in names:
    with open("Input/Letters/starting_letter.txt") as letter:
        text = letter.read()
        finish = text.replace("[name]", name)
        with open(f"Output/ReadyToSend/{name}.txt", "w") as complete:
            complete.write(finish)