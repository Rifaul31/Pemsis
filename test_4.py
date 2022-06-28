from trafficSimulator import *

# Create simulation
sim = Simulation()
n = 15

# Add multiple roads
sim.create_roads([
    ((100, 100), (150, 100)),
    ((160, 110), (160, 160)),
    ((150, 170), (100, 170)),
    ((90, 160), (90, 110)),
    
    *turn_road((150, 100), (160, 110), TURN_RIGHT),
    *turn_road((160, 160), (150, 170), TURN_RIGHT),
    *turn_road((100, 170), (90, 160), TURN_RIGHT),
    *turn_road((90, 110), (100, 100), TURN_RIGHT)
])

def road(a): return range(a, a+n)
roadPath1 = [0, *road(4), 1, *road(4+n), 2, *road(4+2*n), 3, *road(4+3*n)]
roadPath2 = [1, *road(4+n), 2, *road(4+2*n), 3, *road(4+3*n), 0, *road(4)]
roadPath3 = [2, *road(4+2*n), 3, *road(4+3*n), 0, *road(4), 1, *road(4+n)]
roadPath4 = [3, *road(4+3*n), 0, *road(4), 1, *road(4+n), 2, *road(4+2*n)]
circuit1 = roadPath1 + roadPath1 + roadPath1 + roadPath1
circuit2 = roadPath2 + roadPath2 + roadPath2 + roadPath2
circuit3 = roadPath3 + roadPath3 + roadPath3 + roadPath3
circuit4 = roadPath4 + roadPath4 + roadPath4 + roadPath4

sim.create_gen({
    'vehicle_rate': 17,
    'vehicles': [
        [1, {"path": circuit1}]
    ]
})

sim.create_gen({
    'vehicle_rate': 17,
    'vehicles': [
        [1, {"path": circuit3}]
    ]
})

# Start simulation
win = Window(sim)
win.offset = (-150, -110)
win.run(steps_per_update=5)