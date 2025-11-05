# Mail-merge-project
This project is part of a Python learning exercise where we create a Mail Merge system that automatically inserts personalized names into a template letter using placeholders and text files. 
It demonstrates:

Reading files

Working with lists and strings

Removing newline characters

Replacing placeholders dynamically

Writing multiple output files efficiently

🚀 How It Works

The program reads:

A list of names from invited_names.txt

A letter template called starting_letter.txt, which contains a placeholder:

[name]


For each name:

The placeholder is replaced with the actual name

A new personalized letter file is generated inside the ReadyToSend folder

📂 Project Structure
📦 Mail Merge Project
 ┣ 📂 Input
 ┃ ┣ 📄 invited_names.txt
 ┃ ┗ 📄 starting_letter.txt
 ┣ 📂 Output
 ┃ ┗ 📄 (Personalized Letters Appear Here)
 ┗ 📄 main.py


✅ You can edit the template letter
✅ You can add as many names as you like
