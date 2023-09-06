from datetime import timedelta, date, datetime


def get_birthdays_per_week(users):
    if not users:
        return {}

    today = date.today()

    current_day_of_week = today.weekday()

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    birthdays_per_week = {day: [] for day in weekdays}

    for user in users:
        birthday = user["birthday"]

        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        day_of_week = birthday.weekday()

        if day_of_week >= current_day_of_week:
            day_name = weekdays[(day_of_week - current_day_of_week) % 5]
            birthdays_per_week[day_name].append(user["name"])
        else:
            next_monday = today + timedelta(days=(7 - current_day_of_week))
            day_name = "Monday"
            birthdays_per_week[day_name].append(user["name"])

    return birthdays_per_week


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
