PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_lists:
    names = names_lists.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as Letter:
    content = Letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = content.replace(PLACEHOLDER, stripped_name)

        with open(f"./Output/ReadyToSend/letter_to_{stripped_name}.txt", mode="w") as completed_letter:
        
            completed_letter.write(new_letter)



