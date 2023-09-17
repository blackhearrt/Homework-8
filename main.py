from datetime import datetime, date


def get_birthdays_per_week(users):
    if not users:
        return {}

    today = datetime.now().date()
    
    # Створюємо порожні словники для днів цього тижня і наступного тижня
    this_week_birthdays = {}
    next_week_birthdays = {}
    
    # Створюємо список днів тижня для використання в ключах словників
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    # Перебираємо користувачів і їх дні народження
    for user in users:
        name = user['name']
        birthday = user['birthday']
        
        # Визначаємо різницю між поточною датою і днем народження
        delta = birthday - today
        
        # Перевіряємо, чи день народження є в майбутньому
        if delta.days >= 0:
            # Визначаємо день народження наступного тижня для поточної дати
            days_until_birthday = (delta)
            if days_until_birthday <= 6:
                day_of_week = days_of_week[(today.weekday() + days_until_birthday) % 5]
                next_week_birthdays.setdefault(day_of_week, []).append(name)
    
    # Переносимо вихідні дні на понеділок
    for day in ['Saturday', 'Sunday']:
        next_week_birthdays.setdefault('Monday', []).extend(next_week_birthdays.pop(day, []))
    
    return next_week_birthdays

# Приклад використання:
if __name__ == "__main__":
    users = [
        {"name": "Bill Gates", "birthday": datetime(1955, 1, 1).date()},
        {"name": "Jan", "birthday": datetime(1990, 2, 2).date()},
        {"name": "Kim", "birthday": datetime(1985, 3, 3).date()}
    ]
    
    birthdays = get_birthdays_per_week(users)
    print(birthdays)