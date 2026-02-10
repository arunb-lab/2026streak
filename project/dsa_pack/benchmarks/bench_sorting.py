from __future__ import annotations

import random

from project.dsa_pack.algorithms.sorting import merge_sort
from project.dsa_pack.benchmarks.bench_harness import print_result, run_benchmark


def _data(n: int = 200) -> list[int]:
    rng = random.Random(1)
    return [rng.randint(-10_000, 10_000) for _ in range(n)]


def bench_builtin_sorted() -> None:
    arr = _data()
    sorted(arr)


def bench_merge_sort() -> None:
    arr = _data()
    merge_sort(arr)


def main() -> None:
    r1 = run_benchmark("built-in sorted", bench_builtin_sorted, number=2000, runs=5)
    r2 = run_benchmark("merge_sort (python)", bench_merge_sort, number=2000, runs=5)
    print_result(r1)
    print_result(r2)


if __name__ == "__main__":
    main()
