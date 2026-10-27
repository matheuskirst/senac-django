from datetime import date

def resolve_age(born: date):
    # https://www.geeksforgeeks.org/python/python-program-to-calculate-age-in-year/
    today = date.today()

    try:
        birthday = born.replace(year = today.year)
    except ValueError:
        birthday = born.replace(year = today.year,
                    month = today.month + 1, day = 1)

    if birthday > today:
        return today.year - birthday.year - 1
    else:
        return today.year - birthday.year
