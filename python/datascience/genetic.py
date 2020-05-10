import numpy as np
import matplotlib.pyplot as plt
from evol import Population, Evolution

# https://dev.to/fernandezpablo/introduction-to-genetic-algorithms-in-python-e9p

np.random.seed(1234)

def f(x): return 8 * x - 2 * x ** 2

def random_guy(): return np.random.randint(low=-1_000_000, high=1_000_000)

initGenerationSize = 100
firstGen = [random_guy() for _ in range(initGenerationSize)]

pop = Population(chromosomes = firstGen, eval_function = f, maximize = True)
survivors = pop.survive(fraction = 0.1)

def pickParents(population):
    mom, dad = np.random.choice(population, size = 2)
    return mom, dad

def makeChild(mom, dad):
    return (mom + dad) / 2

def randomNoise(individual, sigma):
    noise = np.random.normal(loc = 0, scale = 10) * sigma
    return individual + noise

newGeneration = survivors.breed(parent_picker = pickParents, combiner = makeChild).mutate(randomNoise, sigma = 1)

def fitTest(generation):
    fit = sorted(generation.evaluate(), key = lambda x: x.fitness)[-1]
    return fit.chromosome

generations = 10
fitTestOfEachGen = []

gen = newGeneration
for _ in range(generations):
    survivors = gen.survive(fraction = 0.1)
    newGen = survivors.breed(parent_picker = pickParents, combiner = makeChild).mutate(randomNoise, sigma = 1)
    fitTestOfEachGen.append(fitTest(newGen))
    gen = newGen

# TODO matplotlib for chart
print(fitTestOfEachGen[-1])
x = np.linspace(-140, 150, 1000)
fig, ax = plt.subplots()
ax.plot(x, f(x))
plt.show()