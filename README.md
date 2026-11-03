Expense Tracker (Python)
A simple command-line Expense Tracker built with Python. This is my first Python project, made to practice functions, file handling, and JSON.



📖 About This Project
This is a beginner-friendly Expense Tracker that runs in the terminal. You can add your daily expenses, view them, delete them, and see how much you spent in each category. The data gets saved in a JSON file so it doesn't disappear when you close the program.

I made this project to practice Python basics like functions, loops, and file handling. It uses only Python's built-in modules, so no extra installation is needed.

🚀 Features
Add Expense – Add a new expense with category, amount, and date.

View Expenses – See all your expenses in a numbered list.

Delete Expense – Remove an expense using its list number.

Category Total – See how much you spent in each category.

Grand Total – See your total spending.

Auto Save – Every change is saved to a JSON file automatically.

Input Validation – Wrong inputs are handled properly (no crashes).

Auto Date – The current date is added automatically when you add an expense.

🛠️ Built With
Python 3

JSON (for saving data)

datetime module

File Handling

No external libraries are used. Only Python's built-in stuff.

📂 Folder Structure
text
ExpenseTracker/
│
├── main.py
├── expenses.json
├── README.md
|__ .gitignore
expenses.json gets created automatically when you run the program for the first time. It is not included in the repository.

⚙️ How to Run
Make sure Python 3 is installed on your computer. You can check by running:

bash
python --version
Clone this repository:

bash
git clone https://github.com/Brajkant02/Expense-Tracker-Python.git
Go into the project folder:

bash
cd Expense-Tracker-Python
Run the program:

bash
python main.py
📋 What the Menu Looks Like
When you run the program, you will see this menu:

text
===== EXPENSE TRACKER =====
1. Add Expense
2. View Expenses
3. Delete Expense
4. Category Total
5. Exit
Enter your choice: 1
Enter Category: jsnd
Enter Amount: 130
Expense added successfully!

===== EXPENSE TRACKER =====
1. Add Expense
2. View Expenses
3. Delete Expense
4. Category Total
5. Exit
Enter your choice: 2

----- All Expenses -----
1. 2026-11-04 | Jsnd | ₹130.00
------------------------

===== EXPENSE TRACKER =====
1. Add Expense
2. View Expenses
3. Delete Expense
4. Category Total
5. Exit
Enter your choice: 3

----- All Expenses -----
1. 2026-11-04 | Jsnd | ₹130.00
------------------------
Enter the number to delete: 1
Deleted: Jsnd - ₹130.00

===== EXPENSE TRACKER =====
1. Add Expense
2. View Expenses
3. Delete Expense
4. Category Total
5. Exit
Enter your choice: 3
No expenses to delete!

===== EXPENSE TRACKER =====
1. Add Expense
2. View Expenses
3. Delete Expense
4. Category Total
5. Exit
Enter your choice: 2
No expenses found!

===== EXPENSE TRACKER =====
1. Add Expense
2. View Expenses
3. Delete Expense
4. Category Total
5. Exit
Enter your choice: 1
Enter Category: Food
Enter Amount: 100
Expense added successfully!

===== EXPENSE TRACKER =====
1. Add Expense
2. View Expenses
3. Delete Expense
4. Category Total
5. Exit
Enter your choice: food
Invalid choice! Please try again.

===== EXPENSE TRACKER =====
1. Add Expense
2. View Expenses
3. Delete Expense
4. Category Total
5. Exit
Enter your choice: 1
Enter Category: food
Enter Amount: 120
Expense added successfully!

💾 How Data is Saved
All expenses are saved inside expenses.json in JSON format. Here is an example of how it looks:

json
[
    {
        "date": "2026-11-04",
        "category": "Food",
        "amount": 120.0
    }
]
When you open the program again, it automatically loads the saved data from this file.

🎯 What I Learned From This Project
While building this, I practiced:

Writing and using Python functions

Working with lists and dictionaries

Using loops and if-else statements

Reading and writing files in Python

Saving and loading data with JSON

Handling errors using try-except

Getting the current date using datetime

Validating user input

🤝 Want to Contribute?
If you find any bug or want to add a feature, feel free to open an issue or make a pull request. All suggestions are welcome!



👨‍💻 About Me
Brajkant

I am learning Python and this is one of my practice projects.

GitHub: @Brajkant

📌 Project Status
✅ Completed – Beginner Python Project

Made with Python as a learning project.