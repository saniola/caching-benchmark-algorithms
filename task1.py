import random
import time
from functools import lru_cache


def range_sum_no_cache(array, L, R):
    return sum(array[L : R + 1])


def update_no_cache(array, index, value):
    array[index] = value


@lru_cache(maxsize=1000)
def cached_range_sum(array_id, L, R):
    global array_storage
    return sum(array_storage[array_id][L : R + 1])


def range_sum_with_cache(array, L, R):
    global array_storage
    array_id = id(array)
    if array_id not in array_storage:
        array_storage[array_id] = array
    return cached_range_sum(array_id, L, R)


def update_with_cache(array, index, value):
    global array_storage
    array[index] = value
    array_id = id(array)
    if array_id in array_storage:
        cached_range_sum.cache_clear()
        array_storage[array_id] = array


array_storage = {}

N = 100_000
Q = 50_000
array = [random.randint(1, 100) for _ in range(N)]
queries = []
for _ in range(Q):
    query_type = random.choice(["Range", "Update"])
    if query_type == "Range":
        L = random.randint(0, N - 1)
        R = random.randint(L, N - 1)
        queries.append((query_type, L, R))
    else:
        index = random.randint(0, N - 1)
        value = random.randint(1, 100)
        queries.append((query_type, index, value))

start_time = time.time()
for query in queries:
    if query[0] == "Range":
        _, L, R = query
        range_sum_no_cache(array, L, R)
    else:
        _, index, value = query
        update_no_cache(array, index, value)
time_no_cache = time.time() - start_time

start_time = time.time()
for query in queries:
    if query[0] == "Range":
        _, L, R = query
        range_sum_with_cache(array, L, R)
    else:
        _, index, value = query
        update_with_cache(array, index, value)
time_with_cache = time.time() - start_time

print(f"Час виконання без кешування: {time_no_cache:.2f} секунд")
print(f"Час виконання з LRU-кешем: {time_with_cache:.2f} секунд")
