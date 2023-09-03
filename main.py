from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    users = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
    }
    current_day = date.today().weekday()
    current_date = date.today()
    monday = current_date - timedelta(days=current_day)
    for user in users:
        user_birthday = user["birthday"]
        user_birthday_this_year = date(
            current_date.year, user_birthday.month, user_birthday.day
        )
        if user_birthday_this_year < current_date:
            user_birthday_this_year = date(
                current_date.year + 1, user_birthday.month, user_birthday.day
            )
        days_until_birthday = (user_birthday_this_year - current_date).days
        if 0 <= days_until_birthday <= 4:
            day_of_week = (monday + timedelta(days_until_birthday)).strftime("%A")
            users[day_of_week].append(user["name"])

    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
