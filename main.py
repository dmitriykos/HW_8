from datetime import datetime, timedelta

# поточна дата, початок періоду та кинець періоду в який визначаємо юзерів
current_date = datetime.now()
start_period = current_date - \
    timedelta(days=current_date.weekday()) + timedelta(days=1)
end_period = start_period + timedelta(days=7)


# визначаємо період
def get_str_period(start_period: datetime, end_period: datetime) -> dict[str, str]:
    delta = end_period - start_period   # as timedelta
    days = [start_period + timedelta(days=i) for i in range(delta.days + 1)]
    return {d.strftime("%m-%d"): d.strftime("%Y") for d in days}


# основна функція
def get_birthdays_per_week(users):
    period_bd = get_str_period(start_period, end_period)
    this_year_bd = {}
    for user in users:
        birthdate = user["birthday"][5:]
    # переформатуємо дату народження в формат datetime для кожного юзера
        user_bd = datetime.strptime(user["birthday"], "%Y-%m-%d").date()
    # день народження в поточному році
        current_year_bd = user_bd.replace(year=current_date.year)
        if birthdate in list(period_bd):
            if not this_year_bd.get(current_year_bd):
                this_year_bd[current_year_bd] = [user["name"]]
            else:
                this_year_bd[current_year_bd].append(user["name"])

    for k, v in this_year_bd.items():
        day_of_week = k.strftime("%A")
        if day_of_week == "Sunday" or day_of_week == "Saturday":
            print(f'Monday (transfer from weekends) : {", ".join(v)}')
        else:
            print(f'{day_of_week} : {", ".join(v)}')


users = [
    {"name": "Bill", "birthday": "1994-08-24"},
    {"name": "Tom", "birthday": "1990-12-25"},
    {"name": "Nil", "birthday": "1992-01-23"},
    {"name": "Tod", "birthday": "1990-01-21"},
    {"name": "Ned", "birthday": "1998-12-24"},
    {"name": "Pol", "birthday": "1995-01-25"},
    {"name": "Rud", "birthday": "1990-01-19"},
    {"name": "Sem", "birthday": "2000-01-19"},
]

get_birthdays_per_week(users)
