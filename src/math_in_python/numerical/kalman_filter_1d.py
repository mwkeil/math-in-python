"""Kalman filter (1D, constant state)

Equation/idea:
    Estimate one fixed value from noisy measurements by blending the current
    estimate with each new measurement, weighted by how uncertain each is

    Predict (state assumed constant, uncertainty grows by process noise Q):
        P = P + Q

    Update:
        K = P / (P + R)          Kalman gain, between 0 and 1
        x = x + K (z - x)        move the estimate toward measurement z
        P = (1 - K) P            uncertainty shrinks after each measurement

    x = estimate, P = estimate variance, R = measurement noise variance
    Large P (unsure of estimate) -> K near 1 -> trust the measurement
    Large R (noisy sensor)       -> K near 0 -> trust the estimate

Complexity: O(1) time and space per measurement.
When to use: tracking a slowly changing scalar with approximately Gaussian noise.
    Ex: GPS, phone motion tracking, drones, spacecraft navigation (Apollo),
    robot localization, stock-price smoothing
"""

import random


def predict(P: float, Q: float) -> float:
    """Predict step: state is assumed constant, so only uncertainty changes

    Returns the new estimate variance, P + Q
    """
    return P + Q


def update(x: float, P: float, z: float, R: float) -> tuple[float, float, float]:
    """Update step: blend estimate x with measurement z

    Returns (x, P, K): the new estimate, its new variance, and the gain (for testing)
    """
    K = P / (P + R)
    x = x + K * (z - x)
    P = (1 - K) * P
    return x, P, K


def kalman_filter_1d(
    zs: list[float], x0: float, P0: float, Q: float, R: float
) -> list[float]:
    """Run predict then update for each measurement in zs

    x0, P0 are the initial estimate and its variance. Q is process noise. R is measurement noise.

    Returns the estimate after each measurement
    """
    x, P = x0, P0
    estimates = []
    for z in zs:
        P = predict(P, Q)
        x, P, _ = update(x, P, z, R)
        estimates.append(x)
    return estimates


if __name__ == "__main__":
    rng = random.Random(0)
    zs = [10.0 + rng.gauss(0, 2) for _ in range(20)]
    for z, est in zip(zs, kalman_filter_1d(zs, x0=0.0, P0=1000.0, Q=0.0001, R=4.0)):
        print(f"z={z:6.2f} estimate={est:6.2f}")
