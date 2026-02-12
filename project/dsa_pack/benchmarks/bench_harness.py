from __future__ import annotations

import statistics
import timeit
from dataclasses import dataclass
from typing import Callable, List


@dataclass
class BenchResult:
    name: str
    runs: int
    number: int
    times: List[float]

    @property
    def mean(self) -> float:
        return statistics.mean(self.times)

    @property
    def stdev(self) -> float:
        return statistics.pstdev(self.times)


def run_benchmark(
    name: str, fn: Callable[[], None], *, number: int = 10_000, runs: int = 7
) -> BenchResult:
    timer = timeit.Timer(fn)
    times = [timer.timeit(number=number) for _ in range(runs)]
    return BenchResult(name=name, runs=runs, number=number, times=times)


def print_result(r: BenchResult) -> None:
    per_call_us = (r.mean / r.number) * 1e6
    print(
        f"{r.name}: mean={r.mean:.6f}s (runs={r.runs}, number={r.number}) "
        f"~ {per_call_us:.2f}us/call"
    )
