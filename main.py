import datetime as dt


class Record:
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        self.date = (
            dt.datetime.now().date() if
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        return sum([rec.amount for rec in self.records if rec.date == dt.datetime.now().date()])

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
        else:
            return ('Хватит есть!')


class CashCalculator(Calculator):
    USD_RATE = 60.0  # Курс доллар США.
    EURO_RATE = 70.0  # Курс Евро.
    RUB_RATE = 1.0
    def get_today_cash_remained(self, currency):
        cash_remained = self.limit - self.get_today_stats()

        rates = {'usd': (USD_RATE, 'USD'), 'eur': (EURO_RATE, 'Euro'), 'rub': (RUB_RATE, 'руб')}

        if currency not in rates:
            return f'Неизвестная валюта {currency}'

        rate, currency_name = rates[currency]
        cash_remained /= rate
        rounded_cash = round(cash_remained, 2)

        if cash_remained > 0:
            return (f'На сегодня осталось {rounded_cash} {currency_name}')
        if cash_remained == 0:
            return 'Денег нет, держись'
        elif cash_remained < 0:
            return 'Денег нет, держись: твой долг - {-cash_remained:.2f} {currency_type}

    def get_week_stats(self):
        super().get_week_stats()
