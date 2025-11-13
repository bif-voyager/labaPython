from functools import wraps
from typing import Iterable, Tuple, Union, Callable

Number = Union[int, float]

def check_args(arg_types: Tuple[type, ...] = (int, float),
               min_value: Number | None = None,
               max_value: Number | None = None) -> Callable:
    """
    Декоратор, который проверяет:
      - что все позиционные аргументы имеют допустимый тип;
      - что они лежат в заданном диапазоне [min_value, max_value].
     Если проверка не проходит — выбрасывается исключение TypeError или ValueError.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for x in args:
                if not isinstance(x, arg_types):
                    raise TypeError(
                        f"Недопустимый тип аргумента {x!r}: "
                        f"ожидались типы {arg_types}, получен {type(x)}"
                    )
                if min_value is not None and x < min_value:
                    raise ValueError(
                        f"Аргумент {x!r} меньше минимально допустимого {min_value}"
                    )
                if max_value is not None and x > max_value:
                    raise ValueError(
                        f"Аргумент {x!r} больше максимально допустимого {max_value}"
                    )
            return func(*args, **kwargs)

        return wrapper

    return decorator

def make_averager(min_value: Number | None = None,
                  max_value: Number | None = None) -> Callable:
    """
    Фабрика замыканий.
    Возвращает функцию-замыкание averager, которая:
    - принимает произвольное количество чисел;
    - накапливает их сумму и количество во внутреннем состоянии;
    - возвращает текущее среднее арифметическое.

    К замыканию применяется декоратор check_args для проверки аргументов.
    """

    total = 0.0      # накопленная сумма
    count = 0        # количество добавленных значений

    @check_args((int, float), min_value=min_value, max_value=max_value)
    def averager(*values: Number) -> float:
        nonlocal total, count
        for v in values:
            total += v
            count += 1
        if count == 0:
            raise ZeroDivisionError("Нельзя вычислить среднее без значений")
        return total / count

    return averager

# Демонстрация

if __name__ == "__main__":
    # Замыкание, которое принимает только числа от 0 до 100
    avg = make_averager(min_value=0, max_value=100)

    print("Добавляем 10, 20, 30...")
    print("Среднее:", avg(10, 20, 30))  # (10+20+30)/3 = 20

    print("Добавляем ещё 40...")
    print("Новое среднее:", avg(40))    # (10+20+30+40)/4 = 25

    print("Пробуем добавить недопустимое значение -5...")
    try:
        avg(-5)
    except Exception as e:
        print("Ожидаемая ошибка:", e)

    print("Пробуем передать строку...")
    try:
        avg("100")  # type: ignore[arg-type]
    except Exception as e:
        print("Ожидаемая ошибка:", e)