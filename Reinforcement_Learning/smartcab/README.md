# [Train a Smartcab How to Drive](https://github.com/udacity/machine-learning/tree/master/projects/smartcab)

```
In the not-so-distant future, taxicab companies across the United States no longer employ human drivers to operate their fleet of vehicles. Instead, the taxicabs are operated by self-driving agents, known as *smartcabs*, to transport people from one location to another within the cities those companies operate. In major metropolitan areas, such as Chicago, New York City, and San Francisco, an increasing number of people have come to depend on *smartcabs* to get to where they need to go as safely and reliably as possible. Although *smartcabs* have become the transport of choice, concerns have arose that a self-driving agent might not be as safe or reliable as human drivers, particularly when considering city traffic lights and other vehicles. To alleviate these concerns, your task as an employee for a national taxicab company is to use reinforcement learning techniques to construct a demonstration of a *smartcab* operating in real-time to prove that both safety and reliability can be achieved.
```

Apply reinforcement learning techniques for a self-driving agent in a simplified world to aid it in effectively reaching its destinations in the allotted time. First, investigate the environment the agent operates in by constructing a very basic driving implementation. Once the agent is successful at operating within the environment, identify each possible state the agent can be in when considering such things as traffic lights and oncoming traffic at each intersection. With states identified, implement a Q-Learning algorithm for the self-driving agent to guide the agent towards its destination within the allotted time. Finally, improve upon the Q-Learning algorithm to find the best configuration of learning and exploration factors to ensure the self-driving agent is reaching its destinations with consistently positive results.


- `/logs/`: contains all log files that are given from the simulation when specific prerequisites are met.    
- `/images/`: contains various images of cars to be used in the graphical user interface.  
- `/smartcab/`: contains the Python scripts that create the environment, graphical user interface, the simulation, and the agents.  
	- `agent.py`: the main working Python file.  
	- `environment.py`: creates the *smartcab* environment.  
	- `planner.py`: creates a high-level planner for the agent to follow towards a set goal.  
	- `simulation.py`: creates the simulation and graphical user interface.  
- `smartcab.ipynb`: the main file for smartcab implementation.  
- `visuals.py`: provides supplementary visualizations for the analysis.  


## Definitions

### Environment

The *smartcab* operates in an ideal, grid-like city (similar to New York City), with roads going in the North-South and East-West directions. Other vehicles will certainly be present on the road, but there will be no pedestrians to be concerned with. At each intersection there is a traffic light that either allows traffic in the North-South direction or the East-West direction. U.S. Right-of-Way rules apply: 
- On a green light, a left turn is permitted if there is no oncoming traffic making a right turn or coming straight through the intersection.  
- On a red light, a right turn is permitted if no oncoming traffic is approaching from your left through the intersection.  

### Inputs and Outputs

Assume that the *smartcab* is assigned a route plan based on the passengers' starting location and destination. The route is split at each intersection into waypoints, and assume that the *smartcab*, at any instant, is at some intersection in the world. Therefore, the next waypoint to the destination, assuming the destination has not already been reached, is one intersection away in one direction (North, South, East, or West). The *smartcab* has only an egocentric view of the intersection it is at: It can determine the state of the traffic light for its direction of movement, and whether there is a vehicle at the intersection for each of the oncoming directions. For each action, the *smartcab* may either idle at the intersection, or drive to the next intersection to the left, right, or ahead of it. Finally, each trip has a time to reach the destination which decreases for each action taken (the passengers want to get there quickly).  If the allotted time becomes zero before reaching the destination, the trip has failed.

### Rewards and Goal

The *smartcab* will receive positive or negative rewards based on the action it as taken. Expectedly, the *smartcab* will receive a small positive reward when making a good action, and a varying amount of negative reward dependent on the severity of the traffic violation it would have committed. Based on the rewards and penalties the *smartcab* receives, the self-driving agent implementation should learn an optimal policy for driving on the city roads while obeying traffic rules, avoiding accidents, and reaching passengers? destinations in the allotted time.

