from Node import Node

def find_path(start, end):
  closed_nodes = {}
  open_nodes = [start]

  # ensure the start node has no cost
  start.cost = 0

  while open_nodes:
    node = open_nodes.pop(0)
    if node.key in closed_nodes:
      continue
    neighbors = node.neighbors
    for neighbor, weight in neighbors:
      new_cost = node.cost + weight
      if new_cost < neighbor.cost:
        neighbor.cost = new_cost
        neighbor.parent = node
      open_nodes.append(neighbor)
    closed_nodes[node.key] = node

  path = []
  node = end
  
  while node and node != start:
    path.append(node.key)
    node = node.parent

  path.append(start.key)

  return path[-1::-1]