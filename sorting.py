import random

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
    for j in range(len(cisla)):
        for i in range(0, len(cisla) - j - 1):
            if cisla[i] > cisla[i + 1]:
                cisla[i], cisla[i + 1] = cisla[i + 1], cisla[i]
    return cisla

if __name__ == "__main__":

    test = [5, 1, 4, 2, 8]
    print(test)
    print(bubble_sort(test))
    print(test)

    hodnoty = random_numbers(20)
    print(hodnoty)
    print(bubble_sort(hodnoty))