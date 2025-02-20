from expense_tracker import Expense, ExpenseDatabase

# Create an expense
expense1 = Expense("Groceries", 50.75)
expense2 = Expense("Internet Bill", 30.00)

# Print expense details
print("Expense 1:", expense1.to_dict())
print("Expense 2:", expense2.to_dict())

# Create the database and add expenses
db = ExpenseDatabase()
db.add_expense(expense1)
db.add_expense(expense2)

# Retrieve expense by ID
retrieved_expense = db.get_expense_by_id(expense1.id)
print("Retrieved Expense:", retrieved_expense.to_dict())

# Retrieve expenses by title
grocery_expenses = db.get_expense_by_title("Groceries")
print("Grocery Expenses:", [exp.to_dict() for exp in grocery_expenses])

# Update an expense
expense1.update(amount=55.00)
print("Updated Expense 1:", expense1.to_dict())

# Remove an expense
db.remove_expense(expense2.id)
print("Database after removal:", db.to_dict())
