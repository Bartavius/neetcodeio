
from collections import defaultdict
import json
from typing import List
import heapq
import random

with open("./generate_test.json", "r") as file:
  data = json.load(file)

target = set(data['targetSensors']) # goal states
shuffled = list(target)
# random.shuffle(shuffled)

risks = data['risks'] # edges
sensors = data['sensors'] # vectors / nodes

risk_lookup = {
    (edge["fromSensor"], edge["toSensor"]): edge["risk"]
    for edge in risks
}

adj_lookup = {
  sensor['id']: sensor['dependencies'] for sensor in sensors
}

def check_risk(start, to) -> int:
  '''
  checks the edge risk from 'start' node to 'to' node. return -1 if edge doesn't exist.
  
  :param start: starting node
  :param to: ending node

  :return: -1 if edge doesn't exist but otherwise the rise score
  :rtype: int
  '''
  return risk_lookup.get((start, to), -1)

def get_dependencies(id) -> List[int]:
  '''
  returns the list of neighbor nodes for a given sensor id
  
  :param id: sensor id

  :return: list of neighbor sensor ids
  :rtype: List[int]
  '''
  return adj_lookup.get(id, [])

def tweaked_djikstra():
  
  total_risk = 0
  paths = {}

  while target:
    sensor = shuffled.pop(0)
    target.remove(sensor)

    risk, mini_path = djikstra(sensor)
    total_risk += risk

    paths[sensor] = (mini_path)

  # reconstructing paths again if didn't terminate at start
  for path in paths.values():
    start = path[0]
    neighbors = adj_lookup[start]

    # continue if we're at a start with no dependencies
    if not neighbors:
      continue

    # otherwise, look for another target to join 
    else:
      end = path[-1]
      paths[end] = paths[start] + path[1:]


  return list(paths.values()), total_risk

def djikstra(start):
  '''
  djikstra but terminating condition is either hitting another target or a start
  '''
  dist = {sensor['id']: float("inf") for sensor in sensors}
  dist[start] = 0

  prev = {} # for path reconstruction

  pq = [(0, start)]
  end = None

  while pq:
    curr_dist, u = heapq.heappop(pq)

    # Skip outdated queue entries
    if curr_dist > dist[u]:
        continue
    
    # Terminating condition: if we reached a sensor with no
    # dependencies/another target
    if u == 0 or u in target: 
        
        # TODO: select the LOWEST RISK ROOT, NOT JUST THE FIRST ONE
        end = u
        break

    for v in get_dependencies(u):
        weight = check_risk(v, u)  # this is reversed since we're back propagating
        
        # should never get -1 but leaving this here for debug in case
        if weight < 0:
          print('-1 WEIGHT RECEIVED FROM', u, "->", v)

        new_dist = curr_dist + weight
        if new_dist < dist[v]:
            dist[v] = new_dist
            prev[v] = u

            heapq.heappush(pq, (new_dist, v))

  # If end was never reached
  found_a_target = len(set(prev.keys()).intersection(target))
  found_a_node_with_no_dependencies = [node for node in prev if adj_lookup[node] == []]
  if not (found_a_target or found_a_node_with_no_dependencies):
    return float("inf"), []

  # Reconstruct path otherwise
  path = []
  cur = end
  while cur != start:
      path.append(cur)

      # update edge to 0 risk
      print("turning edge", (cur, prev[cur]), "from", risk_lookup[(cur, prev[cur])], "to 0")
      risk_lookup[(cur, prev[cur])] = 0

      cur = prev[cur]

  path.append(start)

  return dist[end], path

def brute_force():
    paths = {}
    total = 0

    while target:
        node = target.pop()

        best_risk = float("inf")
        best_path = None

        # (current_node, path_so_far, remaining_risk, visited)
        stack = [(node, [node], 1000, set([node]))]

        while stack:
            cur, path, r, visited = stack.pop()

            # terminal condition
            if cur == 0:
              if r < best_risk:
                  print("detected lower risk", r, "for path", path)
                  best_risk = r
                  best_path = path
              continue

            for dep in get_dependencies(cur):
                if dep in visited:
                    continue  # prevent cycles

                new_risk = r - check_risk(dep, cur)
                stack.append((
                    dep,
                    path + [dep],
                    new_risk,
                    visited | {dep}
                ))

        if best_path is None:
            continue

        paths[node] = best_path
        paths[node].reverse()

        # convert chosen path edges to zero risk
        for i in range(len(best_path) - 1):
            parent = best_path[i]
            child = best_path[i + 1]
            risk_lookup[(parent, child)] = 0

        total += 1000 - best_risk
        print("total risk:", total)
        
    
    return paths.values()

       


# Prim's Algorithm
def MST(startid):
  start = (0, startid, -1)

  visited = set()
  heap = [start] # (risk, current, parent)
  mst = {} # parent: node, risk

  while heap and len(mst) < len(sensors) - 1:
    risk, current_node, parent = heapq.heappop(heap)

    if current_node in visited:
       continue
    
    visited.add(current_node)

    # stop mst the moment we find
    if parent != -1:
       mst[current_node] = parent, risk # we're back propogating so current_node is parent

    neighbors = get_dependencies(current_node)
    for neighbor in neighbors:
        edge_risk = check_risk(neighbor, current_node)
        if neighbor not in visited:
            heapq.heappush(heap, (edge_risk, neighbor, current_node))

  return mst


def shortest_path_to_MST(target):
    # Start at leaf node (no dependencies)
    start = target.pop()  # or target[0] if you don't want to modify
    mst = MST(start)
    
    print("MST:", mst)
    
    # Traverse up the MST
    current = start
    path = [current]  # leaf → parent
    lowest_risk = float('inf')
    lowest_risk_node = current

    while current in mst:
        parent, risk = mst[current]
        # update lowest risk if needed
        if risk < lowest_risk:
            lowest_risk = risk
            lowest_risk_node = current

        current = parent
        path.append(current)

        # stop if current node has dependencies (not a leaf)
        if get_dependencies(current):
            break

    path.reverse()  # optional: root/dependency → leaf
    print("Path:", path)
    print("Lowest-risk node along path:", lowest_risk_node, "with risk:", lowest_risk)

    return path, lowest_risk_node



# # first idea
print(tweaked_djikstra())
# ''' 
# best 66 risk
# ([[0, 7, 15, 19, 25], [0, 7, 15, 23, 26], [0, 7, 15, 19, 27], [0, 7, 15, 19, 28], [0, 7, 15, 23, 29], [0, 7, 15, 23, 30]], 66)'''

# 64 risk score
# [[3, 10, 15, 19, 25], [3, 10, 15, 23, 26], [3, 10, 15, 19, 27], [3, 10, 15, 19, 28], [3, 10, 15, 23, 29], [3, 10, 15, 23, 30]]
# print(brute_force())

# # second idea
# print(shortest_path_to_MST(targets))
