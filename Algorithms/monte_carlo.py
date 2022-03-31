import random


"""
for example has system equations:
-2 <= x <= 2
-2 <= y <= 2
x**3 + y**4 + 2 >= 0
3*x + y**2 <= 2
"""

def monte_carlo(number_of_trials: int, coords: list) -> float:
    cnt = 0
    for _ in range(number_of_trials):
        x = random.uniform(coords[0], coords[1])
        y = random.uniform(coords[2], coords[3])
        area_rectangle: float = x * y
        # print(f'{area_rectangle=}')
        if x**3 + y**4 + 2 >= 0 and 3*x + y**2 <= 2:
            cnt += 1

    return (cnt / number_of_trials) * area_rectangle


# run
print(monte_carlo(10**6, [-2, 2, -2, 2]))
