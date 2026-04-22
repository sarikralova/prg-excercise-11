import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(hodnoty):
    for j in range(len(hodnoty)):
        min_index = j
        min_value = hodnoty[min_index]
        for i in range(j + 1, len(hodnoty)):
            if hodnoty[i] < min_value:
                min_index = i
                min_value = hodnoty[i]
        hodnoty[j], hodnoty[min_index] = hodnoty[min_index], hodnoty[j]
    return hodnoty

def bubble_sort(cisla):
    cisla = cisla.copy()

    plt.ion()
    plt.show()

    for j in range(len(cisla)):
        for i in range(0, len(cisla) - j - 1):

            index_highlight1 = i
            index_highlight2 = i + 1
            colors = ["steelblue"] * len(cisla)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"

            plt.clf()
            plt.bar(range(len(cisla)), cisla, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)

            if cisla[i] > cisla[i + 1]:
                cisla[i], cisla[i + 1] = cisla[i + 1], cisla[i]

    plt.ioff()
    plt.show()

    return cisla

if __name__ == "__main__":

    hodnoty = random_numbers(20)
    print(hodnoty)
    print(bubble_sort(hodnoty))