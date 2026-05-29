#Создайте класс «Календарь», который имеет атрибуты год, месяц и день. Добавьте
#методы для определения дня недели, проверки на високосный год и определения
#количества дней в месяце.

import datetime


class Calendar:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def is_leap(self):
        """Проверка на високосный год"""
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    def days_in_month(self):
        """Количество дней в месяце"""
        if self.month in (1, 3, 5, 7, 8, 10, 12):
            return 31
        if self.month in (4, 6, 9, 11):
            return 30
        if self.month == 2:
            return 29 if self.is_leap() else 28

    def day_of_week(self):
        """День недели"""
        date = datetime.date(self.year, self.month, self.day)
        return date.strftime("%A")


# тест
calendar = Calendar(2024, 3, 15)
print("Високосный:", calendar.is_leap())
print("Дней в месяце:", calendar.days_in_month())
print("День недели:", calendar.day_of_week())