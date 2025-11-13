from typing import Any, List, Tuple

# 1. Линеаризация списков

def linearize_recursive(xs: List[Any]) -> List[Any]:
    result: List[Any] = []
    for item in xs:
        if isinstance(item, list):
            # если элемент сам список — разворачиваем его рекурсивно
            result.extend(linearize_recursive(item))
        else:
            result.append(item)
    return result


def linearize_iterative(xs: List[Any]) -> List[Any]:
    """
    Нерекурсивная линеаризация вложенного списка.
    Используется собственный стек вместо вызовов функций.
    """
    result: List[Any] = []
    stack: List[Any] = [xs]

    while stack:
        current = stack.pop()
        if isinstance(current, list):
            # кладём элементы в стек в обратном порядке, чтобы сохранялся исходный порядок
            for elem in reversed(current):
                stack.append(elem)
        else:
            result.append(current)

    return result

# 2. Последовательности a_k и b_k

def ab_recursive(k: int) -> Tuple[int, int]:

    if k < 1:
        raise ValueError("k должно быть натуральным (k >= 1)")
    if k == 1:
        return 1, 1

    a_prev, b_prev = ab_recursive(k - 1)
    a_k = 2 * b_prev + a_prev
    b_k = 2 * a_prev + b_prev
    return a_k, b_k


def ab_iterative(k: int) -> Tuple[int, int]:
    """
    Нерекурсивный расчёт пары (a_k, b_k) с использованием цикла.
    """
    if k < 1:
        raise ValueError("k должно быть натуральным (k >= 1)")

    a, b = 1, 1  # значения для k = 1
    for _ in range(2, k + 1):
        a_new = 2 * b + a
        b_new = 2 * a + b
        a, b = a_new, b_new

    return a, b


#  Демонстрация работы кода

if __name__ == "__main__":
    # Пример для задачи 1
    nested = [1, 2, [3, 4, [5, [6, []]]]]
    print("Исходный список:", nested)
    print("Рекурсивная линеаризация: ", linearize_recursive(nested))
    print("Итеративная линеаризация: ", linearize_iterative(nested))

    print("\nЗадача 2. Значения a_k и b_k:")
    for k in range(1, 8):
        a_r, b_r = ab_recursive(k)
        a_i, b_i = ab_iterative(k)
        print(f"k = {k}: рекурсивно a={a_r}, b={b_r}; "
              f"итеративно a={a_i}, b={b_i}")
