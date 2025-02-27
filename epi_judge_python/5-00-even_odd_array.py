import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def even_odd(Arr: List[int]) -> None:
    # TODO - you fill in here.
    next_even, next_odd = 0, len(Arr)-1
    while next_even<next_odd:
        if Arr[next_even]%2==0:
            next_even+=1
        else:
            Arr[next_even], Arr[next_odd] = Arr[next_odd], Arr[next_even]
            next_odd-=1
    return Arr


@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('5-00-even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))
