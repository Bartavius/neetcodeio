
import json
from typing import List
import heapq

with open("./generate_test.json", "r") as file:
  data = json.load(file)

target = set(data['targetSensors']) # goal states
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
    sensor = target.pop()

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
    if not get_dependencies(u) or u in target:
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

            # update edge to 0 risk
            risk_lookup[(v, u)] = 0

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
      cur = prev[cur]
  path.append(start)

  return dist[end], path

    
print(tweaked_djikstra()) # 21 risk score