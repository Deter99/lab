import time
import random
# Servers
servers = ["Server A", "Server B", "Server C"]
weights = [3, 1, 2]  # For weighted round robin
connections = [0, 0, 0]  # For least connections
# Simulated client requests
requests = [f"Request {i}" for i in range(1, 11)]

# Round Robin
def round_robin(requests, servers):
    print("\n--- Round Robin ---")
    for i, req in enumerate(requests):
        server = servers[i % len(servers)]
        print(f"{req} -> {server}")
        time.sleep(0.2)

# Weighted Round Robin
def weighted_round_robin(requests, servers, weights):
    print("\n--- Weighted Round Robin ---")
    weighted_list = []
    for i in range(len(servers)):
        weighted_list += [servers[i]] * weights[i]

    for i, req in enumerate(requests):
        server = weighted_list[i % len(weighted_list)]
        print(f"{req} -> {server}")
        time.sleep(0.2)

# Least Connections
def least_connections_lb(requests, servers):
    global connections
    print("\n--- Least Connections ---")
    for req in requests:
        index = connections.index(min(connections))
        connections[index] += 1
        print(f"{req} -> {servers[index]} (Connections: {connections[index]})")
        time.sleep(0.2)

# Least Response Time
def least_response_time(requests, servers):
    print("\n--- Least Response Time ---")
    for req in requests:
        response_times = [random.uniform(0.1, 1.0) for _ in servers]
        index = response_times.index(min(response_times))
        print(f"{req} -> {servers[index]} (Response Time: {response_times[index]:.2f}s)")
        time.sleep(0.2)

# Run all
round_robin(requests, servers)
weighted_round_robin(requests, servers, weights)
least_connections_lb(requests, servers)
least_response_time(requests, servers)