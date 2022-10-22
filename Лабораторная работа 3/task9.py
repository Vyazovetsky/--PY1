salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев


for moth in range(1, months + 1):

    differece = spend - salary  # разность зарплаты и траты
    spend = spend * (1 + increase)  # повышение трат со второго месяца
    need_money += differece  # необходимая сумма денег

print(round(need_money))


