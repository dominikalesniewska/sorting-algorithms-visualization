import random
from plot import Plot

if __name__ == "__main__":
    samples = random.sample(range(0, 100), 100)
    plot = Plot(samples, "Insertion Sort")
    plot.run()
