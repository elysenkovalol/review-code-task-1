import datetime as dt


class Record:
    def __init__(self, amount, comment, date='None'):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        
class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        return sum(rec.amount for rec in self.records if rec.date == dt.datetime.now().date())

    def get_week_stats(self):
        today = dt.datetime.now().date()
        week_ago = today - dt.timedelta(days=7)
        return sum(rec.amount for rec in self.records if week_ago <= rec.date <= today)


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):  # Получает остаток калорий на сегодня
        x = self.limit - self.get_today_stats()
        if x > 0:
            return f'Сегодня можно съесть что-нибудь' \
                   f' ещё, но с общей калорийностью не более {x} кКал'
            return ('Хватит есть!')


class CashCalculator(Calculator):
    USD_RATE = float(60)  # Курс доллар США.
    EURO_RATE = float(70)  # Курс Евро.
    RUB_RATE = 1.0
    def get_today_cash_remained(self, currency):
        cash_remained = self.limit - self.get_today_stats()

        rates = {
            'usd': (self.USD_RATE, 'USD'), 
            'eur': (self.EURO_RATE, 'Euro'), 
            'rub': (self.RUB_RATE, 'руб')

        rate = d.get(currency)
        if currency not in rates:
            return f'Неизвестная валюта {currency}'

        rate, currency_type = rates[currency]
        cash_remained /= rate
        rounded_cash = round(cash_remained, 2)

        if cash_remained > 0:
            return (
                f'На сегодня осталось {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        if cash_remained == 0:
            return f'На сегодня осталось {rounded_cash} {currency_type}'
        elif rounded_cash == 0:
            return 'Денег нет, держись'
        else:
            return f'Денег нет, держись: твой долг - {-rounded_cash:.2f} {currency_type}'

    def get_week_stats(self):
        return super().get_week_stats()
