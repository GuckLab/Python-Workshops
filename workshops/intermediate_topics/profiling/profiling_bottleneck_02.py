"""
Profiling to find a bottleneck in a function

`kernprof -lv workshops/intermediate_topics/profiling/profiling_bottleneck_02.py`

"""
from __future__ import annotations

import numpy as np
import time


class SimpleSimulation:

    def __init__(self,
                 image: np.ndarray,
                 pixel_size: float,
                 alpha: int | float,
                 iterations: int,
                 beta_extended: list[tuple, tuple] = None,
                 **kwargs: dict) -> None:
        """Use `self.run` to run a simulation."""
        self.image = image
        self.pixel_size = pixel_size
        self.alpha = alpha
        self.beta_extended = beta_extended
        self.constants: list[tuple, tuple] = None
        self.iterations = iterations
        self.kwargs = kwargs
        self.output_array: np.ndarray = None

    @profile
    def _handle_constants(self) -> None:
        """Construct correct type for constants"""
        if self.beta_extended is not None:
            self.constants = self.beta_extended.insert(0, (self.alpha,))
        else:
            self.constants = list((self.alpha,))

    @profile
    def run(self) -> np.ndarray:
        """Run the simulation"""
        if self.constants is None:
            self._handle_constants()

        # do complex simulation here
        self.output_array = np.ones(self.image.shape)
        self.output_array = self.output_array + 41

        mean_value = np.mean(self.output_array, axis=(-1, -2))

        time.sleep(0.25)  # this will look huge when profiling!

        self.output_array = self.output_array + mean_value

        return self.output_array


if __name__ == "__main__":
    # simple simulation type-hints
    simple_runner = SimpleSimulation(image=np.ones((512, 512)), pixel_size=2.3, alpha=5, iterations=1)
    for _ in range(3):
        arr = simple_runner.run()
