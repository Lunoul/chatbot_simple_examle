from datetime import datetime, timedelta
import json
import os


schedule = {
    "Понеділок": ["Математика 9:00-10:30", "Фізика 11:00-12:30", "Програмування 13:30-15:00"],
    "Вівторок": ["Англійська 9:00-10:30", "Історія 11:00-12:30", "Фізкультура 13:30-15:00"],
    "Середа": ["Програмування 9:00-10:30", "Математика 11:00-12:30", "Фізика 13:30-15:00"],
    "Четвер": ["Історія 9:00-10:30", "Англійська 11:00-12:30", "Програмування 13:30-15:00"],
    "П'ятниця": ["Фізика 9:00-10:30", "Математика 11:00-12:30", "Фізкультура 13:30-15:00"]
}


TASKS_FILE = "tasks.json"

def load_tasks():
    """Завантаження завдань з файлу"""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Збереження завдань у файл"""
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

def get_current_day():
    """Отримання поточного дня тижня"""
    days = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
    return days[datetime.now().weekday()]

def get_tomorrow_day():
    """Отримання дня тижня на завтра"""
    days = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
    tomorrow = datetime.now() + timedelta(days=1)
    return days[tomorrow.weekday()]

def show_schedule(day):
    """Виведення розкладу на вказаний день"""
    if day in schedule:
        print(f"\nРозклад на {day}:")
        for lesson in schedule[day]:
            print(f"- {lesson}")
    else:
        print(f"\nНа {day} занять немає")

def add_task():
    """Додавання нового завдання"""
    subject = input("Введіть назву предмету: ")
    due_date = input("Введіть дату виконання (ДД.ММ.РРРР): ")
    description = input("Введіть опис завдання: ")
    
    tasks = load_tasks()
    tasks.append({
        "subject": subject,
        "due_date": due_date,
        "description": description
    })
    save_tasks(tasks)
    print("\nЗавдання успішно додано!")

def show_tasks():
    """Виведення всіх завдань"""
    tasks = load_tasks()
    if not tasks:
        print("\nНемає активних завдань")
        return
    
    print("\nСписок всіх завдань:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. Предмет: {task['subject']}")
        print(f"   Дата: {task['due_date']}")
        print(f"   Опис: {task['description']}")
        print()

def show_reminders():
    """Виведення нагадувань про завдання на сьогодні та завтра"""
    today = datetime.now().strftime("%d.%m.%Y")
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d.%m.%Y")
    
    tasks = load_tasks()
    if not tasks:
        print("\nНемає завдань на сьогодні та завтра")
        return
    
    print("\nНагадування про завдання:")
    for task in tasks:
        if task['due_date'] in [today, tomorrow]:
            day = "сьогодні" if task['due_date'] == today else "завтра"
            print(f"\nПредмет: {task['subject']}")
            print(f"Термін: {day}")
            print(f"Опис: {task['description']}")

def show_help():
    """Виведення списку доступних команд"""
    print("\nДоступні команди:")
    print("- допомога - показати список команд")
    print("- розклад сьогодні - показати розклад на сьогодні")
    print("- розклад завтра - показати розклад на завтра")
    print("- додати завдання - додати нове завдання")
    print("- завдання - показати всі завдання")
    print("- нагадування - показати завдання на сьогодні та завтра")
    print("- вийти - завершити роботу")

def main():
    """Головна функція програми"""
    print("Вітаю! Я бот-помічник для студентів.")
    print("Введіть 'допомога' для отримання списку команд.")
    
    while True:
        command = input("\nВведіть команду: ").lower().strip()
        
        if command == "вийти":
            print("Дякую за використання! До побачення!")
            break
        elif command == "допомога":
            show_help()
        elif command == "розклад сьогодні":
            show_schedule(get_current_day())
        elif command == "розклад завтра":
            show_schedule(get_tomorrow_day())
        elif command == "додати завдання":
            add_task()
        elif command == "завдання":
            show_tasks()
        elif command == "нагадування":
            show_reminders()
        else:
            print("Невідома команда. Введіть 'допомога' для отримання списку команд.")

if __name__ == "__main__":
    main() 