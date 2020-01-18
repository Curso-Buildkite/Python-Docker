
from __future__ import division
import numpy

n = 10000000
# 2D data spread uniformly across a square of A=1
data = numpy.random.uniform(-0.5, 0.5, size=(n, 2))
data = numpy.random.uniform(-0.5, 0.5, size=(n, 2))
data = numpy.random.uniform(-0.5, 0.5, size=(n, 2))
data = numpy.random.uniform(-0.5, 0.5, size=(n, 2))

# Count points that are within distance 0.5 from center
inside = len(
    numpy.argwhere(
        numpy.linalg.norm(data, axis=1) < 0.5
    )
)

# Calculate pi
print(inside / n * 4)
