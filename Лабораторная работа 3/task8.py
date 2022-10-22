money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

balance = money_capital + salary - spend

while balance > 0:

    spend = spend * (1 + increase)
    balance = balance + salary - spend

    month += 1

print(month)
