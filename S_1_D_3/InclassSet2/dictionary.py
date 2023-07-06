employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

data = {employee: defaults for employee in employees}

print(data)
