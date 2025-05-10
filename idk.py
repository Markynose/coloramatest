

# Імпортуємо colorama та модулі для інтроспекції
import colorama
import inspect
import pprint

# Ініціалізуємо colorama (потрібно для правильної роботи кольорів)
colorama.init()

# Виведемо основну інформацію про бібліотеку
print(f"Версія colorama: {colorama.__version__}")
print(f"Файл бібліотеки: {colorama.__file__}")
print(f"Пакет бібліотеки: {colorama.__package__}")
print("-" * 50)

# Отримуємо всі атрибути та методи colorama
colorama_attributes = dir(colorama)
print(f"Кількість атрибутів і методів: {len(colorama_attributes)}")
print("Всі атрибути та методи:")
for attr in sorted(colorama_attributes):
    print(f" - {attr}")
print("-" * 50)

# Досліджуємо основні модулі
print("Основні модулі colorama:")
for attr in dir(colorama):
    if not attr.startswith("__"):
        obj = getattr(colorama, attr)
        if inspect.ismodule(obj):
            print(f" - {attr}: {obj}")
print("-" * 50)

# Досліджуємо модуль Fore (кольори тексту)
print("Кольори тексту (Fore):")
for attr in dir(colorama.Fore):
    if not attr.startswith("__"):
        print(f" - {attr}: {getattr(colorama.Fore, attr)}")
print("-" * 50)

# Досліджуємо модуль Back (кольори фону)
print("Кольори фону (Back):")
for attr in dir(colorama.Back):
    if not attr.startswith("__"):
        print(f" - {attr}: {getattr(colorama.Back, attr)}")
print("-" * 50)

# Досліджуємо модуль Style (стилі тексту)
print("Стилі тексту (Style):")
for attr in dir(colorama.Style):
    if not attr.startswith("__"):
        print(f" - {attr}: {getattr(colorama.Style, attr)}")
print("-" * 50)

# Демонстрація використання colorama
print("Демонстрація використання colorama:")
print(f"{colorama.Fore.RED}Цей текст червоний{colorama.Style.RESET_ALL}")
print(f"{colorama.Fore.GREEN}Цей текст зелений{colorama.Style.RESET_ALL}")
print(f"{colorama.Back.BLUE}{colorama.Fore.WHITE}Білий текст на синьому фоні{colorama.Style.RESET_ALL}")
print(f"{colorama.Fore.YELLOW}{colorama.Style.BRIGHT}Яскраво-жовтий текст{colorama.Style.RESET_ALL}")
print(f"{colorama.Fore.MAGENTA}{colorama.Style.DIM}Приглушений пурпурний текст{colorama.Style.RESET_ALL}")
print("-" * 50)

# Перевіримо функцію init
print("Аналіз функції init:")
init_signature = inspect.signature(colorama.init)
print(f"Підпис: {init_signature}")
print("Параметри:")
for param_name, param in init_signature.parameters.items():
    print(f" - {param_name}: {param.default if param.default != inspect.Parameter.empty else 'No default'}")
print("-" * 50)

# Дослідимо функцію deinit
print("Аналіз функції deinit:")
if hasattr(colorama, "deinit"):
    deinit_signature = inspect.signature(colorama.deinit)
    print(f"Підпис: {deinit_signature}")
else:
    print("Функція deinit не знайдена")
print("-" * 50)

# Дослідимо функцію reinit
print("Аналіз функції reinit:")
if hasattr(colorama, "reinit"):
    reinit_signature = inspect.signature(colorama.reinit)
    print(f"Підпис: {reinit_signature}")
else:
    print("Функція reinit не знайдена")