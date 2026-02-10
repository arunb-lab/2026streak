from __future__ import annotations

from collections import deque

from project.dsa_pack.benchmarks.bench_harness import print_result, run_benchmark


def bench_list_queue() -> None:
    q = []
    for i in range(100):
        q.append(i)
    q.pop(0)


def bench_deque_queue() -> None:
    q = deque(range(100))
    q.append(100)
    q.popleft()


def main() -> None:
    r1 = run_benchmark("list: append + pop(0)", bench_list_queue, number=20_000, runs=5)
    r2 = run_benchmark("deque: append + popleft", bench_deque_queue, number=200_000, runs=5)
    print_result(r1)
    print_result(r2)


if __name__ == "__main__":
    main()
