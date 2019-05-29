class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.draw()

# In python, we can sign the attribute to instance outside class

point1.x = 10
point1.y = 20

print(point1.x)

point2 = Point()
point2.x = 3
print(point2.x)


class PointClone:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


pointclone = PointClone(10, 20)
print(pointclone.x)
print(pointclone.y)