#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 20:27:06 2024

@author: attaullahabbasi
"""

import random

class Agent:
    def __init__(self, id, world):
        self.id = id
        self.world = world
        self.x = random.randint(0, world.size - 1)
        self.y = random.randint(0, world.size - 1)
        
    def find_empty_patch(self):
        while True:
            x = random.randint(0, self.world.size - 1)
            y = random.randint(0, self.world.size - 1)
            if self.world.grid[x][y] is None:
                return x, y

    def move(self):
        new_x, new_y = self.find_empty_patch()
        self.world.grid[self.x][self.y] = None
        self.x = new_x
        self.y = new_y
        self.world.grid[self.x][self.y] = self.id


class World:
    def __init__(self, size, num_agents):
        self.size = size
        self.num_agents = num_agents
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.agents = [Agent(i, self) for i in range(num_agents)]
        # Place agents in the world
        for agent in self.agents:
            self.grid[agent.x][agent.y] = agent.id

    def step(self):
        for agent in self.agents:
            agent.move()
            

def run_simulation(world_size, num_agents, num_steps):
    world = World(world_size, num_agents)
    for step in range(num_steps):
        world.step()
        print(f"Step {step+1} completed")
        for row in world.grid:
            print(row)
        print()  # Empty line for better readability

if __name__ == "__main__":
    world_size = 5  # small grid
    num_agents = 3  # small number of agents
    num_steps = 10  # small number of loops
    run_simulation(world_size, num_agents, num_steps)