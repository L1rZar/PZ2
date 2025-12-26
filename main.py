from decorators_module import measure_time, validate_range
from math_functions import FUNCTIONS
from visualization import print_table, plot_xy

@measure_time
@validate_range
def compute_xy(a, b, step, func):
    #создает векторы X и Y для выбранной функции
    x_values = []
    y_values = []
    x = a
    # Избегаем накопления ошибки: <= b + маленький_eps
    while x <= b + 1e-9:
        x_values.append(x)
        y_values.append(func(x))
        x += step
    return x_values, y_values

def main():
    print("Добро пожаловать в демонстрацию модульного программирования!")
    print("Доступные функции:")
    for key, (desc, _) in FUNCTIONS.items():
        print(f"{key}: {desc}")

    func_choice = input("Выберите функцию (введите номер): ").strip()
    if func_choice not in FUNCTIONS:
        print("Неверный выбор функции.")
        return

    try:
        a = float(input("Введите a (начало интервала по оси X): "))
        b = float(input("Введите b (конец интервала по оси X): "))
        step = float(input("Введите шаг (Меньше шаг → больше точек на графике → линия получается более плавной): "))
    except ValueError:
        print("Ошибка ввода числа.")
        return

    desc, func = FUNCTIONS[func_choice]
    print(f"Вы выбрали функцию: {desc}")

    try:
        x_values, y_values = compute_xy(a, b, step, func)
    except ValueError as e:
        print("Ошибка:", e)
        return

    print("Таблица значений:")
    print_table(x_values, y_values)

    plot_xy(x_values, y_values, title=desc)

if __name__ == "__main__":
    main()
