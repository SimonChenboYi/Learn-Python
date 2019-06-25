def number(bus_stops):
    people_in_bus = 0
    for bus_stop in bus_stops:
        people_in_bus += (bus_stop[0] - bus_stop[1])
    return people_in_bus

print(number([[10,0],[3,5],[5,8]]))



# Number of people in the bus
# There is a bus moving in the city, and it takes and drop some people in each bus stop.
#
# You are provided with a list (or array) of integer arrays (or tuples). Each integer array has two items which represent number of people get into bus (The first item) and number of people get off the bus (The second item) in a bus stop.
#
# Your task is to return number of people who are still in the bus after the last bus station (after the last array). Even though it is the last bus stop, the bus is not empty and some people are still in the bus, and they are probably sleeping there :D
#
# https://www.codewars.com/kata/number-of-people-in-the-bus/python