import math

def equal(float1, float2, percision = 2):
            if abs(float1 - float2) < 1*10**-percision:
                return True
            return False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x**2 + self.y**2)**0.5

    def euclidean_distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def angle_between(self, other):
        vert = other.y - self.y
        horiz = other.x - self.x
        return math.atan2(vert, horiz)
    
    def dot_product(self, other):
        return self.x*other.x + self.y*other.y

    def __repr__(self) -> str:
        return f"({self.x}|{self.y})"
    
class Triangle:
    def __init__(self, p1:Point, p2:Point, p3:Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def side_lengths(self) -> tuple[float]:
        d1 = self.p1.euclidean_distance(self.p2)
        d2 = self.p2.euclidean_distance(self.p3)
        d3 = self.p3.euclidean_distance(self.p1)
        return float(d1), float(d2), float(d3)
    
    def angles(self):
        a1 = self.p1.angle_between(self.p2)
        a2 = self.p2.angle_between(self.p3)
        a3 = self.p3.angle_between(self.p1)
        return float(a1), float(a2), float(a3)
    
    def side_classification(self) -> str:

        equal_sides = 0
        d1, d2, d3 = self.side_lengths()

        equal_sides += 1 if equal(d1,d2) else 0
        equal_sides += 1 if equal(d2,d3) else 0
        equal_sides += 1 if equal(d3,d1) else 0

        match equal_sides:
            case 0:
                return "scalene"
            case 3:
                return "equilateral"
            case _:
                return "isosceles"

    def angle_classification(self) -> str:

        angles_60 = 0

        for angle in self.angles():
            print(abs(math.degrees(angle)))

        for angle in self.angles():
            angle = abs(math.degrees(angle))

            if equal(angle, 90):
                return "right"
            if angle > 90:
                return "obtuse"
            if equal(angle, 60):
                angles_60 += 1

        
        if angles_60 == 3:
            return "equiangular"

        return "acute"



def test_triangle_side_lengths():
    triangle = Triangle(Point(0,0), Point(0,3), Point(4,3)) 
    d1, d2, d3 = triangle.side_lengths()

    assert d1 == float(3)
    assert d2 == float(4)
    assert d3 == float(5)


# def test_triangle_angles():
#     triangle = Triangle(Point(10,1), Point(0,0), Point(3,2)) 
#     a1, a2, a3 = triangle.angles()

#     assert a1 >= 0
#     assert a2 >= 0
#     assert a3 >= 0


def test_triangle_side_classification():
    scalene = Triangle(Point(0,0), Point(0,3), Point(4,3))
    #equilateral = Triangle(Point(0,0), Point(0,3), Point(4,3))
    isosceles = Triangle(Point(0,0), Point(3,0), Point(0,3))

    assert scalene.side_classification() == "scalene"
    assert isosceles.side_classification() == "isosceles"


def test_triangle_angle_classification():
    right = Triangle(Point(0,0), Point(0,3), Point(3,0))
    obtuse = Triangle(Point(0,0), Point(-1, 3), Point(3,0))
    acute = Triangle(Point(0,0), Point(1,3), Point(3,0))
    #equiangular = Triangle(Point(0,0), Point(0,3), Point(3,0))

    assert right.angle_classification() == "right"
    assert obtuse.angle_classification() == "obtuse"
    assert acute.angle_classification() == "acute"
    #assert obtuse.angle_classification() == "isosceles"


a = Point(1,1)
b = Point(4,1)
c = Point(1,4)
points = [a,b,c]

alpha = 0
bata = 0
gamma = 0
angles = []

for p1,p2,p3 in zip(points, (points+points)[1:], (points+points)[2:]):
    vector_p1_p2 = Point(p2.x -p1.x, p2.y - p1.y)
    vector_p1_p3 = Point(p3.x -p1.x, p3.y - p1.y)

    dot_product = vector_p1_p2.dot_product(vector_p1_p3)

    mag_v_p1_p2 = vector_p1_p2.distance_to_origin()
    mag_v_p1_p3 = vector_p1_p3.distance_to_origin()
    mag_product = mag_v_p1_p2*mag_v_p1_p3

    print(vector_p1_p2, vector_p1_p3)
    print(dot_product)
    print(mag_product)

# for i, _ in enumerate(points):
#     angles.append(points[i].angle_between(points[(i+1)%3]))

# angles_deg = list(map(lambda x: x*180/math.pi,angles))

# for i, _ in enumerate(angles_deg):
#     print(angles_deg[i] - angles_deg[(i+1)%3])

# print(angles_deg)

# for p1,p2,p3 in zip(points, (points+points)[1:], (points+points)[2:]):
#     print(p1,p2,p3)

#     point1 = Point(p1.x - p3.x, p1.y - p3.y)
#     point2 = Point(p2.x - p3.x, p2.y - p3.y)

#     print(point1,point2,p3)

#     angle = p1.angle_between(p2)
#     angle_deg = (math.degrees(angle) + 360) % 360
#     print(angle_deg)


# for p1,p2,p3 in zip(points, (points+points)[1:], (points+points)[2:]):
#     print(p1,p2)

#     point1 = Point(p1.x, p1.y)
#     point2 = Point(p2.x, p2.y)

#     angle = p1.angle_between(p2)
#     angle_deg = (math.degrees(angle) + 360) % 360
#     print(angle_deg)
