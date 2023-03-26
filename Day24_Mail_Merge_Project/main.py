#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import os

os.chdir("/Users/yuuki/Documents/workspace/100_Days_of_Code/Day24_Mail_Merge_Project")

# template = ""
with open("Input/Letters/starting_letter.txt", mode="r") as f:
    template = f.read()

with open("Input/Names/invited_names.txt", mode="r") as names:
    while True:
        name = names.readline().strip()
        if not name:
            break
        text = template.replace("[name]", name)
        letter_title = "letter_for_" + name + ".txt"
        with open(f"Output/ReadyToSend/{letter_title}", mode="w") as letter:
            letter.write(text)
