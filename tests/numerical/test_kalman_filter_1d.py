import random

import pytest

from math_in_python.numerical.kalman_filter_1d import kalman_filter_1d, update


def test_update_closed_form():
    x, P, K = update(0.0, 4.0, 2.0, 1.0)
    assert x == pytest.approx(1.6)
    assert K == pytest.approx(0.8)
    assert P == pytest.approx(0.8)


def test_converges_to_true_value():
    rng = random.Random(0)
    zs = [10.0 + rng.gauss(0, 2) for _ in range(200)]
    est = kalman_filter_1d(zs, x0=0.0, P0=1000.0, Q=0.0001, R=4.0)
    assert est[-1] == pytest.approx(10.0, abs=0.5)
