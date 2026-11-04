from typing import Callable, Iterator


# yields all float numbers found in the text
def generator_numbers(text: str) -> Iterator[float]:
    words_list = text.split()
    for potential_float in words_list:
        try:
            float_number = float(potential_float)
        except ValueError:
            continue

        yield float_number


# returns total profit, sum of all float numbers found by func
def sum_profit(text: str, func: Callable[[str], Iterator[float]]) -> float:
    floats_iterator = func(text)
    total_profit = sum(floats_iterator)
    return total_profit


text = "Загальний дохід працівника складається з 0 декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів. 100"
print("загальний дохiд: " + str(sum_profit(text, generator_numbers)))
