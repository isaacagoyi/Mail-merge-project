#TODO: Create a letter using starting_letter.txt 

#Read the .txt files that contains the list of invited users
with open("./Input/Names/invited_names.txt", mode="r") as names:
    name_list = [line.strip() for line in names]

# Read the starting_letter.txt file and replace the [user] placeholder with the name of the user
with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
    letter = letter.read()

# Loop through the list of invited users and create a new invitation letter for the users.
# All letters are to be stored in the ReadyToSend folder
for name in name_list:
    updated_letter = letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as invite:
        invite.write(updated_letter)

