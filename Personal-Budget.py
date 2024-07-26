# Question 1 task 1

class BudgetCategory:

    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__expenses = []

# Question 1 task 2

    def get_category_name(self):
        return self.__category_name
    
    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_category_name(self, category_name):
        if not isinstance(category_name, str):
            raise ValueError("Category name must be a valid string.")
        self.__category_name = category_name

    def set_allocated_budget(self, amount):
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Budget can't be negative.")
        self.__allocated_budget = amount

# Question 1 task 3

    def add_expense(self, expense_amount):
        if not isinstance(expense_amount, (int, float)) or expense_amount < 0:
            raise ValueError("Expense must be a positive number.")
        if expense_amount > self.__allocated_budget:
            raise ValueError("Expense is greater than the allocated budget.")
        self.__expenses.append(expense_amount)

# Question 1 task 4

    def get_total_expenses(self):
        return sum(self.__expenses)
    
    def display_category_summary(self):
        print(f"Category: {self.__category_name}")
        print(f"Initial Budget: {self.__allocated_budget}")
        print(f"Remaining Budget: {self.__allocated_budget - sum(self.__expenses)}")

if __name__ == "__main__":
    category = BudgetCategory("Rent", 400)
    category.display_category_summary()

    category.add_expense(30)
    category.display_category_summary()