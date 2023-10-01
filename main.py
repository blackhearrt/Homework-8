from datetime import date, datetime, timedelta



def get_birthdays_per_week(users):
    if not users:
        return {}
    
    # Визначення поточної дати та інтервалу в тиждень.
    today = date.today()
    next_week = today + timedelta(days=7)  
    
    # Створення робочих словників.
    weekday = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday'}
    birthdays = {day: [] for day in weekday.values()}
    
    # Сортування днів народження та додавання іменинників до словника.
    for user in users:
        name = user['name'].split()[0]
        birthday = user['birthday'].replace(year=today.year)
        
        if birthday < today:  
            birthday = birthday.replace(year=today.year + 1)
        if today <= birthday <= next_week:
            day_of_week = birthday.strftime("%A")
            if day_of_week not in weekday.values():
                day_of_week = "Monday"
            birthdays[day_of_week].append(name)
             
    birthdays = {day: names for day, names in birthdays.items() if names}             
    return birthdays
    


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")