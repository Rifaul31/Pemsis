from trafficSimulator import *

# Create simulation
sim = Simulation()

# Add multiple roads
sim.create_roads([
    ((100, 100), (110, 100)),
    ((110, 100), (120, 100)),
    ((120, 100), (130, 100)),
    ((130, 100), (140, 100)),
    ((140, 100), (150, 100)),
    ((150, 100), (160, 100)),
    ((160, 100), (170, 100)),
    ((170, 100), (180, 100)),
    ((180, 100), (190, 100)),
    ((190, 100), (200, 100)),

    ((200, 100), (210, 100)),
    ((210, 100), (220, 100)),
    ((220, 100), (230, 100)),
    ((230, 100), (240, 100)),
    ((240, 100), (250, 100)),
    ((250, 100), (260, 100)),
    ((260, 100), (270, 100)),
    ((270, 100), (280, 100)),
    ((280, 100), (290, 100)),
    ((290, 100), (300, 100)),
    
])

path1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
path2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]
path3 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 1]
path4 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2]
path5 = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3]
path6 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4]
path7 = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5]
path8 = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6]
path9 = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7]
path10 = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8]
path11 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
path12 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
path13 = [12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
path14 = [13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
path15 = [14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
path16 = [15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
path17 = [16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
path18 = [17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
path19 = [18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
path20 = [19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

road1 = path1 + path1 + path1 + path1 + path1 + path1 + path1 + path1 + path1 + path1 + path1 + path1 + path1 + path1 + path1 + path1 + path1 + path1 + path1 + path1
road2 = path2 + path2 + path2 + path2 + path2 + path2 + path2 + path2 + path2 + path2 + path2 + path2 + path2 + path2 + path2 + path2 + path2 + path2 + path2 + path2
road3 = path3 + path3 + path3 + path3 + path3 + path3 + path3 + path3 + path3 + path3 + path3 + path3 + path3 + path3 + path3 + path3 + path3 + path3 + path3 + path3
road4 = path4 + path4 + path4 + path4 + path4 + path4 + path4 + path4 + path4 + path4 + path4 + path4 + path4 + path4 + path4 + path4 + path4 + path4 + path4 + path4
road5 = path5 + path5 + path5 + path5 + path5 + path5 + path5 + path5 + path5 + path5 + path5 + path5 + path5 + path5 + path5 + path5 + path5 + path5 + path5 + path5

road6 = path6 + path6 + path6 + path6 + path6 + path6 + path6 + path6 + path6 + path6 + path6 + path6 + path6 + path6 + path6 + path6 + path6 + path6 + path6 + path6
road7 = path2 + path7 + path7 + path7 + path7 + path7 + path7 + path7 + path7 + path7 + path7 + path7 + path7 + path7 + path7 + path7 + path7 + path7 + path7 + path7
road8 = path8 + path8 + path8 + path8 + path8 + path8 + path8 + path8 + path8 + path8 + path8 + path8 + path8 + path8 + path8 + path8 + path8 + path8 + path8 + path8
road9 = path9 + path9 + path9 + path9 + path9 + path9 + path9 + path9 + path9 + path9 + path9 + path9 + path9 + path9 + path9 + path9 + path9 + path9 + path9 + path9
road10 = path10 + path10 + path10 + path10 + path10 + path10 + path10 + path10 + path10 + path10 + path10 + path10 + path10 + path10 + path10 + path10 + path10 + path10 + path10 + path10

road11 = path11 + path11 + path11 + path11 + path11 + path11 + path11 + path11 + path11 + path11 + path11 + path11 + path11 + path11 + path11 + path11 + path11 + path11 + path11 + path11
road12 = path12 + path12 + path12 + path12 + path12 + path12 + path12 + path12 + path12 + path12 + path12 + path12 + path12 + path12 + path12 + path12 + path12 + path12 + path12 + path12
road13 = path13 + path13 + path13 + path13 + path13 + path13 + path13 + path13 + path13 + path13 + path13 + path13 + path13 + path13 + path13 + path13 + path13 + path13 + path13 + path13
road14 = path14 + path14 + path14 + path14 + path14 + path14 + path14 + path14 + path14 + path14 + path14 + path14 + path14 + path14 + path14 + path14 + path14 + path14 + path14 + path14
road15 = path15 + path15 + path15 + path15 + path15 + path15 + path15 + path15 + path15 + path15 + path15 + path15 + path15 + path15 + path15 + path15 + path15 + path15 + path15 + path15

road16 = path16 + path16 + path16 + path16 + path16 + path16 + path16 + path16 + path16 + path16 + path16 + path16 + path16 + path16 + path16 + path16 + path16 + path16 + path16 + path16
road17 = path17 + path17 + path17 + path17 + path17 + path17 + path17 + path17 + path17 + path17 + path17 + path17 + path17 + path17 + path17 + path17 + path17 + path17 + path17 + path17
road18 = path18 + path18 + path18 + path18 + path18 + path18 + path18 + path18 + path18 + path18 + path18 + path18 + path18 + path18 + path18 + path18 + path18 + path18 + path18 + path18
road19 = path19 + path19 + path19 + path19 + path19 + path19 + path19 + path19 + path19 + path19 + path19 + path19 + path19 + path19 + path19 + path19 + path19 + path19 + path19 + path19
road20 = path20 + path20 + path20 + path20 + path20 + path20 + path20 + path20 + path20 + path20 + path20 + path20 + path20 + path20 + path20 + path20 + path20 + path20 + path20 + path20

circuit1 = road1 + road1 + road1 + road1 + road1 + road1 + road1 + road1 + road1 + road1 + road1 + road1 + road1 + road1 + road1
circuit2 = road2 + road2 + road2 + road2 + road2 + road2 + road2 + road2 + road2 + road2 + road2 + road2 + road2 + road2 + road2
circuit3 = road3 + road3 + road3 + road3 + road3 + road3 + road3 + road3 + road3 + road3 + road3 + road3 + road3 + road3 + road3
circuit4 = road4 + road4 + road4 + road4 + road4 + road4 + road4 + road4 + road4 + road4 + road4 + road4 + road4 + road4 + road4
circuit5 = road5 + road5 + road5 + road5 + road5 + road5 + road5 + road5 + road5 + road5 + road5 + road5 + road5 + road5 + road5
circuit6 = road6 + road6 + road6 + road6 + road6 + road6 + road6 + road6 + road6 + road6 + road6 + road6 + road6 + road6 + road6
circuit7 = road7 + road7 + road7 + road7 + road7 + road7 + road7 + road7 + road7 + road7 + road7 + road7 + road7 + road7 + road7
circuit8 = road8 + road8 + road8 + road8 + road8 + road8 + road8 + road8 + road8 + road8 + road8 + road8 + road8 + road8 + road8
circuit9 = road9 + road9 + road9 + road9 + road9 + road9 + road9 + road9 + road9 + road9 + road9 + road9 + road9 + road9 + road9
circuit10 = road10 + road10 + road10 + road10 + road10 + road10 + road10 + road10 + road10 + road10 + road10 + road10 + road10 + road10 + road10

circuit11 = road11 + road11 + road11 + road11 + road11 + road11 + road11 + road11 + road11 + road11 + road11 + road11 + road11 + road11 + road11
circuit12 = road12 + road12 + road12 + road12 + road12 + road12 + road12 + road12 + road12 + road12 + road12 + road12 + road12 + road12 + road12
circuit13 = road13 + road13 + road13 + road13 + road13 + road13 + road13 + road13 + road13 + road13 + road13 + road13 + road13 + road13 + road13
circuit14 = road14 + road14 + road14 + road14 + road14 + road14 + road14 + road14 + road14 + road14 + road14 + road14 + road14 + road14 + road14
circuit15 = road15 + road15 + road15 + road15 + road15 + road15 + road15 + road15 + road15 + road15 + road15 + road15 + road15 + road15 + road15
circuit16 = road16 + road16 + road16 + road16 + road16 + road16 + road16 + road16 + road16 + road16 + road16 + road16 + road16 + road16 + road16
circuit17 = road17 + road17 + road17 + road17 + road17 + road17 + road17 + road17 + road17 + road17 + road17 + road17 + road17 + road17 + road17
circuit18 = road18 + road18 + road18 + road18 + road18 + road18 + road18 + road18 + road18 + road18 + road18 + road18 + road18 + road18 + road18
circuit19 = road19 + road19 + road19 + road19 + road19 + road19 + road19 + road19 + road19 + road19 + road19 + road19 + road19 + road19 + road19
circuit20 = road20 + road20 + road20 + road20 + road20 + road20 + road20 + road20 + road20 + road20 + road20 + road20 + road20 + road20 + road20

sim.create_gen({
    'vehicle_rate': 120,
    'vehicles': [
        [1, {"path": circuit1}],
        [1, {"path": circuit2}],
        [1, {"path": circuit3}],
        [1, {"path": circuit4}],
        [1, {"path": circuit5}],
        [1, {"path": circuit6}],
        [1, {"path": circuit7}],
        [1, {"path": circuit8}],
        [1, {"path": circuit9}],
        [1, {"path": circuit10}],
        [1, {"path": circuit11}],
        [1, {"path": circuit12}],
        [1, {"path": circuit13}],
        [1, {"path": circuit14}],
        [1, {"path": circuit15}],
        [1, {"path": circuit16}],
        [1, {"path": circuit17}],
        [1, {"path": circuit18}],
        [1, {"path": circuit19}],
        [1, {"path": circuit20}],
    ]
})

# Start simulation
win = Window(sim)
win.offset = (-150, -110)
win.run(steps_per_update=5)