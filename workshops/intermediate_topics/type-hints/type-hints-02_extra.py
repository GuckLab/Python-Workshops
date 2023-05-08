"""
Type hints

More type-hint types
"""

# python < 3.10 you need to import annotations (e.g. pipe) operator
# from __future__ import annotations

import numpy as np


class SimpleSimulation:

    def __init__(self,
                 image: np.ndarray,  # won't hint correctly if numpy isn't installed!
                 pixel_size: float,
                 alpha: int | float,
                 beta_extended: list[tuple, tuple],
                 iterations: int,
                 **kwargs: dict):
        """Use `self.run` to run a simulation."""
        self.image = image
        self.pixel_size = pixel_size
        self.alpha = alpha
        self.beta_extended = beta_extended
        self.constants: list[tuple, tuple]
        self.iterations = iterations
        self.kwargs = kwargs
        self.output_array: np.ndarray = None

    def _handle_constants(self) -> None:
        """Construct correct type for constants"""
        if self.beta_extended is not None:
            self.constants = self.beta_extended.insert(0, (self.alpha,))
        else:
            self.constants = list((self.alpha,))

    def run(self) -> np.ndarray:
        """Run the simulation"""
        if self.constants is None:
            self._handle_constants()

        # do complex simulation here
        self.output_array = np.ones(self.image.shape)

        return self.output_array


class ComplexSimulation:
    def __init__(self, simple_sim_object: SimpleSimulation):
        """A really complex simulation!!!"""
        self.simple_sim_runner = simple_sim_object  # instance of SimpleSimulation

    def run(self) -> np.ndarray:
        # here comes the complex part...
        for i in range(self.simple_sim_runner.iterations):
            output_array = self.simple_sim_runner.run()
            # use new output as input
            self.simple_sim_runner.image = output_array

        return self.simple_sim_runner.image


if __name__ == "__main__":
    # simple simulation type-hints
    simple_runner = SimpleSimulation(...)
    simple_runner.run()

    # OR

    # complex simulation type-hints
    simple_runner = SimpleSimulation(...)
    complex_runner = ComplexSimulation(simple_runner)
    complex_runner.run()
