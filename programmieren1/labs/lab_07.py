import math

def equal(float1, float2, percision = 5):
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
        self.right = True if self.angle_classification() == "right" else False

    def side_lengths(self) -> tuple[float]:
        d1 = self.p1.euclidean_distance(self.p2)
        d2 = self.p2.euclidean_distance(self.p3)
        d3 = self.p3.euclidean_distance(self.p1)
        return float(d1), float(d2), float(d3)

    def angles(self):
        points = [self.p1,self.p2,self.p3]

        angles_lst = []

        for p1,p2,p3 in zip(points, (points+points)[1:], (points+points)[2:]):
            vector_p1_p2 = Point(p2.x -p1.x, p2.y - p1.y)
            vector_p1_p3 = Point(p3.x -p1.x, p3.y - p1.y)

            dot_product = vector_p1_p2.dot_product(vector_p1_p3)

            mag_v_p1_p2 = vector_p1_p2.distance_to_origin()
            mag_v_p1_p3 = vector_p1_p3.distance_to_origin()
            magnitude_product = mag_v_p1_p2*mag_v_p1_p3

            cos = dot_product / magnitude_product
            acos = math.acos(cos)
            angles_lst.append(math.degrees(acos))

        return tuple(angles_lst)
    
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
            angle = abs(angle)

            if equal(angle, 90):
                return "right"
            if angle > 90:
                return "obtuse"
            if equal(angle, 60):
                angles_60 += 1

        if angles_60 == 3:
            return "equiangular"

        return "acute"
    
    def is_right(self):
        return self.right

    def area(self):
        a, b, c = self.side_lengths()
        s = 1/2*(a+b+c)
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        return area

    def perimeter(self):
        return sum(self.side_lengths())

class Vector:
    def __init__(self, vector):
        self.vector = vector
    
    def as_list(self):
        return self.vector

    def size(self):
        return len(self.vector)

    def magnitude(self):
        """
        >>> v1 = Vector([2,0])
        >>> v1.magnitude()
        2.0
        >>> v2 = Vector([3,4])
        >>> v2.magnitude()
        5.0
        """
        return math.sqrt(sum(map(lambda x: x**2, self.vector)))

    def euclidean_distance(self, other):
        """
        >>> v1 = Vector([2,0])
        >>> v2 = Vector([0,2])
        >>> v1.euclidean_distance(v2)
        2.8284271247461903
        """
        return math.sqrt(sum(map(lambda x, y:(x-y)**2, self.as_list(), other.as_list())))
            
    def normalized(self):
        """
        >>> v1 = Vector([4,2])
        >>> v1.normalized().as_list()
        [1.0, 0.0]
        >>> v2 = Vector([100, 12, 24, 7, 0])
        >>> v2.normalized().as_list()
        [1.0, 0.12, 0.24, 0.07, 0.0]
        >>> v2 = Vector([1,1])
        >>> v2.normalized().as_list()
        [0.0, 0.0]
        """
        def normalize(n, min, max): 
            """
            >>> normalize(10, 5, 15)
            0.5
            >>> normalize(2, 2, 15)
            0.0
            >>> normalize(14, 5, 15)
            0.9
            """
            try:
                return (n - min) / (max - min)
            except:
                return 0.0
        
        return Vector(list(map(lambda x: normalize(x, min(self.as_list()), max(self.as_list())), self.as_list())))

    def cosine_similarity(self, other):
        """
        >>> v1 = Vector([0, 2])
        >>> v2 = Vector([2, 0])
        >>> v1.cosine_similarity(v2)
        0.0
        >>> v1 = Vector([2, 2])
        >>> v2 = Vector([-1, -1])
        >>> v1.cosine_similarity(v2)
        0.0
        >>> v1 = Vector([2, 2])
        >>> v2 = Vector([-1, -1])
        >>> v1.cosine_similarity(v2)
        0.0
        """
        dot_product = 0
        mag_product = abs(self.magnitude()) * abs(other.magnitude())
        for v1, v2 in zip(self.normalized().as_list(), other.normalized().as_list()):
            dot_product += v1 * v2
        
        return dot_product / mag_product




    def __add__(self, other):
        if self.size() != other.size():
            raise OverflowError("Vector lengths are not equal.")
        
        result_vector = []
        for vi, vj in zip(self.as_list(), other.as_list()):
            result_vector.append(vi+vj)

        return Vector([result_vector])

    def __sub__(self, other):
        if self.size() != other.size():
            raise OverflowError("Vector lengths are not equal.")

        result_vector = []
        for vi, vj in zip(self.as_list(), other.as_list()):
            result_vector.append(vi-vj)

        return Vector([result_vector])

    def __mul__(self, other):
        if self.size() != other.size():
            raise OverflowError("Vector lengths are not equal.")

        scalar = 0
        for vi, vj in zip(self.as_list(), other.as_list()):
            scalar += vi*vj

        return scalar

    def __truediv__(self, other):
        if self.size() != other.size():
            raise OverflowError("Vector lengths are not equal.")

        result_vector = []
        for vi, vj in zip(self.as_list(), other.as_list()):
            result_vector.append(vi/vj)
        
        return Vector([result_vector])

def test_triangle_side_lengths():
    triangle = Triangle(Point(0,0), Point(0,3), Point(4,3)) 
    d1, d2, d3 = triangle.side_lengths()

    assert d1 == float(3)
    assert d2 == float(4)
    assert d3 == float(5)

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

def test_triangle_area():
    t = Triangle(Point(0,0), Point(0,3), Point(3,0))
    assert equal(t.area(),4.5)

def test_triangle_perimiter():
    t = Triangle(Point(0,0), Point(0,3), Point(3,0))
    a,b,c = t.side_lengths()
    assert equal(t.perimeter(), a+b+c)


"""
compute without a computer:

"A cool gray car"

"A cool gray car"

"gray"

"gray"

"A cool gray car"

"A cool plaid car"

"plaid"

"gray"

"small"

AttributeError "Car has not attribute size"

"small"

AttributeError "Object has not attribute size"
"""