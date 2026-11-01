Primal: An Evolving Agent Civilization Simulation

A simulation where a small group of agents start with nothing but primal instincts (hunger, thirst, fatigue, fear) and must survive, adapt, and eventually build something like a civilization. The agents are never told what to become. Their bodies, brains, and behaviors are meant to emerge from environmental pressure and trade-offs, the way human evolution did.

The brain is built from scratch, with no ML libraries doing the work, as a way of learning AI and machine learning from first principles.

Status: early work in progress. Version 1 (world + random baseline) is complete. Everything beyond that is the plan.

The idea

Most agent simulations hand the agents goals. This project tries the opposite:

Agents have drives (hunger, thirst, tiredness), and what counts as "good" behavior is whatever reduces those needs.
Every trait has a cost (a bigger brain burns more energy, a longer childhood needs more parental care), so nothing grows without limit.
The environment creates the pressure, and traits that help survival and reproduction spread over generations.
Intelligence, kin bonds, cooperation, tool use, and culture are not scripted. They either emerge or they don't, and both outcomes are results.

The long-term target is a 3D version in Unreal Engine with 20 founding agents (10 male, 10 female). The brain is prototyped first in a simple Python grid world, where experiments are fast and easy to measure.

Current status: Version 1

A single agent lives on a 20x20 grid that wraps around at the edges. It must find food and water before its needs run out. In this version the agent moves randomly, which gives a baseline that every smarter agent must beat.

World rules
Setting	Value
Grid	20 x 20, wrapping edges
Food tiles	5% of the grid, randomly placed
Water tiles	5% of the grid, randomly placed
Actions	up, down, left, right, stay
Agent rules

All levels run from 100 (full) down to 0 (dead).

Event	Effect
Every step	satiety -2, hydration -3
Step on food	satiety +20 (cap 100), hydration -1, food tile is used up
Step on water	hydration +30 (cap 100), water tile stays
Satiety or hydration reaches 0	agent dies (cause recorded)
Baseline result: random agent, 1,000 lives
Metric	Result
Average survival	43.7 steps
Deaths by thirst	742
Deaths by starvation	258

Baseline histogram

The histogram has a clear structure. Deaths cluster at 33-34 steps (agents that never found water), and further peaks appear every 10 steps, because one meal or one drink buys about 10 more steps. The shape follows directly from the food and water values, which makes it a useful check that the rules work as designed.

How to run

Requires Python 3.9+ and two packages:

bash
pip install numpy matplotlib
python world.py

The random seed is fixed, so results repeat exactly.

Design principles
Simulate in steps, not seconds. Real-time speed matters only for display. Training and experiments run as fast as the CPU allows.
Separate the world from the brain. step() applies an action to the world, and choose_action() decides what to do. This lets the brain be swapped (random, rule-based, learned) without touching the world.
Never reward intelligence directly. Fitness is survival and reproduction, nothing else.
Every trait has a price. Brain size, body size, and sensing range all cost energy or risk.
Measure everything. Log every run, fix seeds, and compare any new agent against the baseline.
Roadmap
Version 2: a fuller body and world
 Food regrowth: eaten food regrows after 10 steps (a per-tile timer grid)
 Energy and sleep: energy falls while awake, sleep is suggested at 40, penalties begin at 20, a forced collapse happens at 0, and sleeping restores energy at half the usual drain
 Age: an age counter and death by old age, as groundwork for life stages
Version 3: smarter brains
 Second baseline: persistent heading (keep direction most of the time instead of fresh random moves)
 Rule-based agent (rest while comfortable, search when needy), plus a movement cost so resting has real value
 Senses: the agent sees nearby tiles
 Learning from drives: tabular Q-learning, with reward defined as reduction of a need
 Neural network policy written from scratch, trained through neuroevolution
Version 4: populations and evolution
 Many agents sharing one world, plus predators and seasonal scarcity
 Birth, death, and inheritance, with a genome of evolvable traits
 Parallel independent worlds, so selection is not drowned out by genetic drift in tiny populations
Version 5: social life
 Kin recognition through early-life familiarity
 Attachment, loneliness, and parental care as drives
 Imitation and a simple signal channel, so shared meaning can emerge
Version 6: Unreal Engine
 Port the trained brain into Unreal (C++ or an external Python service)
 3D world, animation, day-night cycle, visualization of lineages
Planned evolvable traits

Inspired by changes seen in the human fossil record. Each trait gets a cost and a benefit, and the environment decides which pays off.

Trait	Cost	Pressure favoring it
Efficient locomotion	Less ability to escape predators by climbing	Food spread far apart
Manipulation skill	Needs brain capacity	Objects that can be used as tools
Brain size	Constant energy drain, riskier birth	Hard-to-find, calorie-dense food and social complexity
Infancy length	Parents pay care costs for longer	Bigger brains need more learning time
Pair bonding	Energy cost of body size and aggression	Offspring survive better with two caregivers
Heat tolerance	Cold nights vs overheating by day	Foraging in open sun

A good result is a curve that rises, levels off, and shifts when the environment changes. A runaway or collapsing curve means the costs need tuning.

Honest limitations
This is an open research-style problem. Emergent civilization is not guaranteed, and the first results will be simple survival and foraging behavior.
Twenty agents is a small population for evolution, which is why parallel worlds are in the plan.
Parameters (food density, costs, regrowth time) need careful tuning. A lot of the work is in the balance.
Inspiration
Park et al., Generative Agents: Interactive Simulacra of Human Behavior (2023), a simulation of 25 LLM-driven agents. This project deliberately takes the other route (instinct-driven brains, evolution, no language model).
Work on human evolution: bipedalism, brain size, prolonged infancy, social learning, and cultural evolution.

Author

Built by Avirj, a mechatronics engineering student, as a first deep project in AI and ML.
