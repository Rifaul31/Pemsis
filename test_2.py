from trafficSimulator import *

# Create simulation
sim = Simulation()

# Add multiple roads
sim.create_roads([
    ((100, 100), (200, 100)),
    ((200, 100), (300, 100)),

])

path1 = [0, 1, 0, 1, 0, 1, 0, 1]
# path1 = [0, 0, 0, 0, 0, 0, 0, 0]
path2 = [1, 0, 1, 0, 1, 0, 1, 0]

circuit1 = path1 + path1 + path1 + path1 + path1 + path1 + path1
circuit2 = path2 + path2 + path2 + path2 + path2 + path2 + path2

sim.create_gen({
    'vehicle_rate': 60,
    'vehicles': [
        [1, {"path": circuit1}],
        [1, {"path": circuit2}]
    ]
})

# Start simulation
win = Window(sim)
win.offset = (-150, -110)
win.run(steps_per_update=5)