def lights(p, b, k):
    lower_bound = p[0] - b[0] + 1
    upper_bound = p[-1] + b[-1] 
    range_of_lights = abs(upper_bound - lower_bound) #to calculate the range of the list,
    room = [0 for x in range (range_of_lights)] #initialize every point in the room has a brightness of 0
    print("size of range ",upper_bound-lower_bound)
    for light in enumerate(p):
        print(f"light number {light[0]} at position {light[1]-lower_bound} with brightness {b[light[0]]}")
        room[light[1]-lower_bound] += b[light[0]]
        side_brightness = b[light[0]]-1
        offset = 0
        while (side_brightness > 0):
            offset += 1
            room[light[1]-lower_bound-offset] = room[light[1]-lower_bound-offset] + side_brightness if light[1]-lower_bound-offset >= 0 else 0
            room[light[1]-lower_bound+offset] = room[light[1]-lower_bound+offset] + side_brightness if light[1]-lower_bound+offset <= upper_bound-lower_bound else 0
            side_brightness -= 1
        print(room)
    invalid_pos = 0
    for brightness in room:
        if brightness >= k:
            invalid_pos +=1
    return invalid_pos
#print("the range of the lights ", lower_bound, upper_bound)
# p => list of the positions of the lamps on the number line
# b => brightness of the lamps in respective to p
# k => the treshold
print(lights([-5,-3, 0, 10], [3, 10, 6, 3], 6))
