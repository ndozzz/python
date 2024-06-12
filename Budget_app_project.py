class Category():
    
    def __init__(self, category):
        self.category = category
        self.ledger = []

    """
    def __str__(self):
        header = self.category.center(30,'*')
        ledger = ''
        for i in self.ledger:
            a = i["description"].ljust(23)
            b = f'{i["amount"]:7.2f}\n'
            ledger += a+b
        display = f'{z}\n{list1}Total: {str(sum(i["amount"] for i in n):.2f)}'
    """
    def __str__(self):
        header = self.category.center(30, '*')
        ledger_str = ''
        for item in self.ledger:
            description = item["description"][:23].ljust(23)
            amount = f'{item["amount"]:7.2f}'
            ledger_str += f'{description}{amount}\n'
        balance = self.get_balance
        total = f'Total: {sum(item["amount"] for item in self.ledger):.2f}'
        return f'{header}\n{ledger_str}{total}'
        

    def deposit(self, amount, description = ''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = '' ):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False


    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.category}")
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False
        

    def get_balance(self):
        return sum(_["amount"] for _ in self.ledger)
        
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True
"""
def create_spend_chart(categories):
    total = 0
    for i in categories:
        for _ in i.ledger:
            if _["amount"] < 0:
                total += -_["amount"]
    total_spent = sum(-item["amount"] for category in categories for item in category.ledger if item["amount"] < 0)
    spend_percentages = [
(sum(-_["amount"] for _ in i.ledger if _["amount"] < 0) / total) * 100 for i in categories
]
    chart_percentage = {category.category: spend_percentages[i] for i, category in enumerate(categories)}
    sorted_dict = {}
    for key in sorted(chart_percentage, key=chart_percentage.get):
        sorted_dict[key] = chart_percentage[key]
    chart ='Percentage spent by category\n'
    for i in range(100, -1, -10):
        chart += str(i).rjust(3)+'|'
        for _ in sorted_dict:
            if sorted_dict[_] >= i:
                chart += ' o '
            else:
                chart += '   '
        chart += '\n'
    chart += '    '
    for i in sorted_dict:
        chart += '---'
    chart += '-'
    chart += '\n'

    for _ in range(max(map(len, sorted_dict))):
        chart += '    '
        for i in sorted_dict:
            if _ < len(i):
                chart += f' {i[_]} '
            else:
                chart += '   '
        chart += '\n'
    return chart.rstrip('\n')
"""
def create_spend_chart(categories):
    # Calculate the total spend and the percentage spent by category
    total_spent = sum(-item["amount"] for category in categories for item in category.ledger if item["amount"] < 0)
    spend_percentages = [
        (sum(-item["amount"] for item in category.ledger if item["amount"] < 0) / total_spent) * 100 for category in categories
    ]

    # Prepare the chart
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for percentage in spend_percentages:
            chart += "o  " if percentage >= i else "   "
        chart += "\n"

    # Add the horizontal line
    chart += "    -" + "---" * len(categories) + "\n"

    # Prepare the category names vertically
    max_length = max(len(category.category) for category in categories)
    for i in range(max_length):
        chart += "     "
        for category in categories:
            if i < len(category.category):
                chart += category.category[i] + "  "
            else:
                chart += "   "
        chart += "\n"

    return chart.strip('\n')
display = ''
x = 'display'
y = '*' * ((30 - len(x))//2)+x+'*' * ((30 - len(x))//2)
if len(y)<30:
    y += '*'
print(y)
z = x.center(30,'*')
print(z)

n = [{"amount": 1000, "desc": 'test1'},{"amount": -200, "desc": 'test2'}]
list1 = ''
for i in n:
    a = i["desc"].ljust(23)
    b = f'{i["amount"]:7.2f}\n'
    list1 += a+b
print(f'{z}\n{list1}Total: {sum(i["amount"] for i in n):.2f}')
food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(20, 'Pants')
categories = [food,clothing]
total = 0
print(clothing)
print(food)
for i in range(100, -1, -10):
    print(i)
for i in categories:
    for _ in i.ledger:
        if _["amount"] < 0:
            total += -_["amount"]
print(total)
total_spent = sum(-item["amount"] for category in categories for item in category.ledger if item["amount"] < 0)
print(total_spent)
print(sum(_["amount"] for i in categories for _ in i.ledger if _["amount"] < 0))
spend_percentages = [
(sum(-_["amount"] for _ in i.ledger if _["amount"] < 0) / total) * 100 for i in categories
]
print(spend_percentages)
chart_percentage = {category.category: spend_percentages[i] for i, category in enumerate(categories)}
print(chart_percentage)
sorted_dict = {}
for key in sorted(chart_percentage, key=chart_percentage.get):
    sorted_dict[key] = chart_percentage[key]
 
print(sorted_dict)
chart ='Percentage spent by category\n'
for i in range(100, -1, -10):
    chart += str(i).rjust(3)+'|'
    for _ in sorted_dict:
        if sorted_dict[_] >= i:
            chart += ' o '
        else:
            chart += '   '
    chart += '\n'
chart += '    '
for i in sorted_dict:
    chart += '---'
chart += '-'
chart += '\n'

for _ in range(max(map(len, sorted_dict))):
    chart += '    '
    for i in sorted_dict:
        if _ < len(i):
            chart += f' {i[_]} '
        else:
            chart += '   '
    chart += '\n'
print(chart)
print(range(max(map(len, sorted_dict))))
print(create_spend_chart(categories))