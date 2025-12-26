import matplotlib.pyplot as plt

def print_table(x_values, y_values):
    """Печатает X и Y в две строки."""
    # Простой вариант без форматирования разрядности:
    print("X:", " ".join(f"{x:.3f}" for x in x_values))
    print("Y:", " ".join(f"{y:.3f}" for y in y_values))

def plot_xy(x_values, y_values, title="График функции"):
    """Строит график по векторам X и Y."""
    plt.figure()
    plt.plot(x_values, y_values, marker="o")
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()
