# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

class Workers:
    def __init__(self,name: str, salary: int, bonus:str):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def pay_bonus(self):
        return {self.name: self.salary * (float(self.bonus[:-1]) / 100)}


wrk_1 = Workers('Olga', 10000, '10.25%')
wrk_2 = Workers('Denis', 15000, '20.5%')
wrk_3 = Workers('Kolya', 120000, '13.75%')
for wrk in [wrk_1, wrk_2, wrk_3]:
    print(wrk.pay_bonus())