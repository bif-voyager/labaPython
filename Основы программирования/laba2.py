from itertools import product


def task1_count_sequences() -> int:
    letters = "KATEP"
    start = "P"
    end = "K"
    count = 0
    for middle in product(letters, repeat=4):
        count += 1
    return count


def to_base(n: int, base: int) -> str:
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % base))
        n //= base
    return "".join(reversed(digits))


def task2_count_distinct_digits_in_base6() -> int:
    value = 216**6 + 216**4 + 36**6 - 6**14 - 24
    base6 = to_base(value, 6)
    return len(set(base6))


def task3_find_mask_numbers():
    results = []
    for a in range(10):
        for b in range(10):
            for c in range(10):
                n = int(f"12345{a}{b}8{c}")
                if n <= 10**9 and n % 23 == 0:
                    results.append((n, n // 23))
    return results


if __name__ == "__main__":
    print("Задача 1. Количество последовательностей:", task1_count_sequences())
    print("Задача 2. Число разных цифр в записи в СС осн. 6:",
          task2_count_distinct_digits_in_base6())

    print("Задача 3. Числа по маске 12345??8?, кратные 23:")
    for n, q in task3_find_mask_numbers():
        print(n, q, sep="\t")
