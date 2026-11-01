import numpy as np
import matplotlib.pyplot as plt

CONFIG ={
    "grid_size":{
        "width": 20,
        "height": 20
    },
    "food_fraction": 0.05,
    "water_fraction": 0.1,
    "initial_population": 20,
    "hunger_per_step": 2,
    "thirst_per_step": 3,
    "food_value": 20,
    "water_value": 30,
    "thirst_after_eating": 1,
    "regrow_food": 10,
    "death_limit": 100
} 
survival_times = []
Death_causes = {"starvation": 0, "thirst": 0}

MOVES = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0), "stay": (0, 0)}

rng = np.random.default_rng(42) #fixed seed so the results repeat

def choose_action(rng):
        # choose a random action
        return rng.choice(["up", "down", "left", "right", "stay"])

def step(grid, agent, action):
            
    agent["pos_x"] = (agent["pos_x"] + MOVES[action][0]) % CONFIG["grid_size"]["width"]
    agent["pos_y"] = (agent["pos_y"] + MOVES[action][1]) % CONFIG["grid_size"]["height"]

    agent["satiety"] -= CONFIG["hunger_per_step"]
    agent["hydration"] -= CONFIG["thirst_per_step"]
    
    tile = grid[agent["pos_y"]][agent["pos_x"]]
    if tile == 1:
        agent["satiety"] = min(100, agent["satiety"] + CONFIG["food_value"])
        agent["hydration"] = min(100, agent["hydration"] - CONFIG["thirst_after_eating"])
        grid[agent["pos_y"]][agent["pos_x"]] = 0

    elif tile == 2:
        agent["hydration"] = min(100, agent["hydration"] + CONFIG["water_value"])

    agent["steps"] += 1

    if agent["satiety"] <= 0 or agent["hydration"] <= 0:
        agent["alive"] = False
        agent["cause"] = "starvation" if agent["satiety"] <= 0 else "thirst"

def make_wld():
    n = CONFIG["grid_size"]
    grid = np.zeros((n["width"],n["height"]), dtype=int)
    r = rng.random((n["width"],n["height"]))
    grid[r < CONFIG["food_fraction"]] = 1
    grid[(r >= CONFIG["food_fraction"]) & (r < CONFIG["water_fraction"])] = 2

    return grid

def make_agent():
    AGENT = {
        "pos_x": CONFIG["grid_size"]["width"] // 2,
        "pos_y": CONFIG["grid_size"]["height"] // 2,
        "satiety": 100,
        "hydration": 100,
        "alive": True,
        "steps": 0,
        "cause": None
    }
    return AGENT

def run_life(rng):
    agent = make_agent()
    grid = make_wld()

    while agent["alive"] and agent["steps"] < 1000:
        action = choose_action(rng)
        step(grid, agent, action)

    return agent

for _ in range(1000):
    a = run_life(rng)
    survival_times.append(a["steps"])
    Death_causes[a["cause"]] += 1
    # print(a["steps"], a["cause"])

print("Average survival time:", np.mean(survival_times))
print("Death causes:", Death_causes)
print("min survival time:", np.min(survival_times))

plt.hist(survival_times, bins=range(0, max(survival_times) + 2))
plt.xlabel("Steps survived")
plt.ylabel("Number of lives")
plt.title("Random agent baseline (1000 lives)")
plt.show()