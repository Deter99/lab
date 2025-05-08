import numpy as np
num_ants = 10
num_iterations = 100
alpha = 1
beta = 5
evaporation = 0.5
Q = 100

distances = np.array([
    [0,2,9,10,7],[1,0,6,4,3],[15,7,0,8,3],[6,3,12,0,11],[9,7,5,2,0]
])
num_cities = len(distances)
pheromone = np.ones((num_cities, num_cities))
best_tour = None
best_length = float('inf')

def choose_next_city(probabilities):
    return np.random.choice(range(len(probabilities)), p=probabilities)

def ant_tour(start):
    tour = [start]
    unvisited = set(range(num_cities)) - {start}
    for _ in range(num_cities - 1):
        current = tour[-1]
        probs = []
        for j in unvisited:
            tau = pheromone[current][j] ** alpha
            eta = (1 / distances[current][j]) ** beta
            probs.append(tau * eta)
        probs = np.array(probs)
        probs /= probs.sum()
        next_city = list(unvisited)[choose_next_city(probs)]
        tour.append(next_city)
        unvisited.remove(next_city)
    return tour

def total_distance(tour):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)) + distances[tour[-1]][tour[0]]

for _ in range(num_iterations):
    all_tours = [ant_tour(np.random.randint(num_cities)) for _ in range(num_ants)]
    pheromone *= (1 - evaporation)
    for tour in all_tours:
        length = total_distance(tour)
        for i in range(num_cities):
            a, b = tour[i], tour[(i + 1) % num_cities]
            pheromone[a][b] += Q / length
            pheromone[b][a] += Q / length
        if length < best_length:
            best_length = length
            best_tour = tour

print("Best tour:", best_tour)
print("Best cost:", best_length)