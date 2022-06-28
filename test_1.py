from trafficSimulator import *

# Create simulation
sim = Simulation()

# Add multiple roads
sim.create_roads([
    ((100, 100), (200, 100)),
    
])

path = [0, 0, 0, 0, 0, 0]
circuit = path + path + path + path

sim.create_gen({
    'vehicle_rate': 60,
    'vehicles': [
        [1, {"path": circuit}]
    ]
})

# Start simulation
win = Window(sim)
win.offset = (-150, -110)
win.run(steps_per_update=5)