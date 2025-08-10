import matplotlib.pyplot as plt


def plot_graph(
    x_values: list[float], y_values: list[float], title: str, x_label: str, y_label: str
):
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, marker="o")
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.show()
