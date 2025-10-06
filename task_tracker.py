import os
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
ENDC = '\033[0m'

FILE_NAME = 'tasks.txt'

def categorize_task(task_name, days_left):
    """
    Определяет категорию и возвращает строку с цветным форматированием.
    """
    days = int(days_left)
    
    if days < 0:
        return f"{RED}ПРОСРОЧЕНО ({abs(days)} дн. назад): {task_name}{ENDC}"
    elif days <= 30:
        return f"{GREEN}ТЕКУЩАЯ (осталось {days} дн.): {task_name}{ENDC}"
    else:
        # Будущие (больше 30 дней)
        return f"{BLUE}БУДУЩАЯ (осталось {days} дн.): {task_name}{ENDC}"

def process_tasks():
    # Проверка наличия файла
    if not os.path.exists(FILE_NAME):
        print("Ошибка: Файл tasks.txt не найден!")
        print("Создайте его и заполните данными.")
        return

    print("\n--- Отчет по задачам ---\n")
    
    try:
        # Открываем и читаем файл. 'with open' гарантирует его закрытие.
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            for line in file:
                # Убираем лишние пробелы и символы перевода строки
                line = line.strip() 
                if not line:
                    continue # Пропускаем пустые строки
                
                # Разделяем строку по разделителю '|'
                parts = line.split('|')
                
                if len(parts) == 2:
                    task_name = parts[0].strip()
                    days_left = parts[1].strip()
                    
                    # Вызываем нашу функцию для форматирования и выводим
                    print(categorize_task(task_name, days_left))
                    
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")

if __name__ == "__main__":
    process_tasks()