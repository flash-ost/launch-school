"""
How big is the room?
Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

Note: 1 square meter == 10.7639 square feet
"""
# length = float(input('Please enter length of the room: '))
# width = float(input('Please enter width of the room: '))

# area_meters = length * width
# area_feet = area_meters * 10.7639
# print(f'Room\'s area is {area_meters} square meters or {area_feet} square feet.')

"""
Further Exploration
Modify the program to let the user specify the measurement type (meters or feet). Compute the area accordingly and print it and its conversion in parentheses.
"""
ALLOWED_TYPES = ['meters', 'feet']
FEET_IN_METER = 10.7639

while True:
    measurement_type = input('Please specify measurement type (meters or feet): ')
    if measurement_type not in ALLOWED_TYPES:
        print('This is not a valid type.')
        continue
    break

length = float(input('Please enter length of the room: '))
width = float(input('Please enter width of the room: '))

if measurement_type == 'meters':
    area_meters = length * width
    area_feet = area_meters * FEET_IN_METER
    print(f'Room\'s area is {area_meters:.2f} square meters ({area_feet:.2f} square feet).')
else:
    area_feet = length * width
    area_meters = area_feet / FEET_IN_METER
    print(f'Room\'s area is {area_feet:.2f} square feet ({area_meters:.2f} square meters).')