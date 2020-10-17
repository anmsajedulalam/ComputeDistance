"""
Projectile motion analysis

"""

''' 
projectile motion calculator:
projectile motion theorems:
height = y(t) = hs + (t * velocity * sin(theta)) - (g * t*t)/2
distance = x(t) = velocity * cos(theta) * t
where:
t is the time in seconds
velocity is the muzzle velocity of the projectile (meters/second)
theta is the firing angle with respect to ground (radians)
hs is starting height with respect to ground (meters)
g is the gravitational pull (meters/second_square)
'''
import math
def projectile_xy(veloctiy, theta, hs=0.0, g=9.8):
    '''
    here, we will calculate a list of (x, y) projectile motion data points
    where:
    x axis is distance (or range) in meters
    y axis is height in meters
    velocity is muzzle velocity of the projectile (meter/second)
    theta is the firing angle with respect to ground (radians)
    hs is starting height with respect to ground (meters)
    g is the gravitational pull (meters/second_square)
    '''
    data_xy = [] #declaring an array
    t = 0.0 #initial time
    while True:
        # calculating the height y
        y = hs + (t * veloctiy * math.sin(theta)) - (g * t * t)/2
        # when projectile will hit ground level
        if y < 0:
            break
        # calculating the distance x
        x = veloctiy * math.cos(theta) * t
        # appending the (x, y) tuple to the list
        data_xy.append((x, y))
        # using the time in increments of 0.1 seconds
        t += 0.1
    return data_xy
# taking input from user for a firing angle which can be only in between 0-90
print("initial angle can only be in between 0 to 90")
print("input angle")
d = int(input())
theta=d
if d<0:
    print("initial angle can not be less than 0")
elif d>90:
    print("initial angle can not be more than 90")
else:
    theta = math.radians(d)  # radians

# taking input from user for muzzle velocity of the projectile (meters/second)
print("input velocity")
velocity = int(input())
data_ab = projectile_xy(velocity, theta)
# find maximum height
point_height_max = max(data_ab, key = lambda q: q[1])#using lambda function, which is an anonymous function and key for sorting
xm, ym = point_height_max
print('''
    *********Projectile Motion**********
All the results will be described here: 
Using a firing angle of {} degrees
and a muzzle velocity of {} meters/second
the maximum height is {:0.1f} meters
at a distance of {:0.1f} meters,'''.format(d, velocity, ym, xm))
# the maximum distance
x_max = max(data_ab)[0]
print("the maximum distance is {:0.1f} meters.".format(x_max))
