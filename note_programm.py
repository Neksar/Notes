import json
import datetime

# Функция для сохранения заметок в файл
def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file)

# Функция для чтения заметок из файла
def load_notes():
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

# Функция для добавления новой заметки
def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка добавлена успешно!")

# Функция для редактирования существующей заметки
def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note["id"] == note_id:
            new_title = input("Введите новый заголовок заметки: ")
            new_body = input("Введите новый текст заметки: ")
            note["title"] = new_title
            note["body"] = new_body
            note["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка отредактирована успешно!")
            return
    print("Заметка с указанным ID не найдена.")

# Функция для удаления заметки
def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка удалена успешно!")
            return
    print("Заметка с указанным ID не найдена.")

# Функция для вывода списка заметок
def display_notes():
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Текст: {note['body']}")
        print(f"Дата/Время: {note['timestamp']}")
        print()

# Функция для фильтрации заметок по дате
def filter_notes_by_date():
    date_str = input("Введите дату для фильтрации (в формате ГГГГ-ММ-ДД): ")
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        filtered_notes = [note for note in notes if datetime.datetime.strptime(note["timestamp"], "%Y-%m-%d %H:%M:%S").date() == date]
        if len(filtered_notes) > 0:
            print(f"Найдено {len(filtered_notes)} заметок:")
            for note in filtered_notes:
                print(f"ID: {note['id']}")
                print(f"Заголовок: {note['title']}")
                print(f"Текст: {note['body']}")
                print(f"Дата/Время: {note['timestamp']}")
                print()
        else:
            print("Заметки не найдены.")
    except ValueError:
        print("Некорректный формат даты.")

# Основная логика программы
notes = load_notes()

while True:
    print("1. Добавить заметку")
    print("2. Редактировать заметку")
    print("3. Удалить заметку")
    print("4. Вывести список заметок")
    print("5. Фильтрация заметок по дате")
    print("0. Выход")
    choice = input("Выберите действие: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        edit_note()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        display_notes()
    elif choice == "5":
        filter_notes_by_date()
    elif choice == "0":
        break
    else:
        print("Некорректный выбор.")