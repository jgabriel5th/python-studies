'''
CONSTANT = "Variables" that won't change.
Many conditions in the same if-structure(bad).
    <- Complexity count(bad).
'''
# \ <- is used to break like in the middle of a Python code.
speed = 63# actual car speed.
car_position = 98 # position where the car is in the road.

RADAR_1 = 60 # max speed permitted in radar 1
POSITION_1 = 100 # position where the radar 1 is 
RADAR_RANGE = 1 # Range distance that the radar takes.
carSpeedRadar1 = speed > RADAR_1
carFinedRadar1 = (car_position >= POSITION_1 - RADAR_RANGE) and (car_position <= POSITION_1 + RADAR_RANGE)

# First version of code:
# if (speed > RADAR_1) and (car_position >= POSITION_1 - RADAR_RANGE) and \
#     (car_position <= POSITION_1 + RADAR_RANGE):
#     print('The car is beyond the speed limit permitted. Fine imposed.')
# else:
#     print('The car is according to speed limit.')

# Final verison of code(legibility aplied):
if carSpeedRadar1 and carFinedRadar1:
    print('The car is beyond the speed limit permitted. Fine imposed.')
else:
    print('The car is according to speed limit.')