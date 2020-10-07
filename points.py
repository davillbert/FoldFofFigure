
class Point: #test2 #test3 lilu nell
    # Класс Point - содержит координаты точки #жопа
    def __init__(self, point_input):
        self.x = point_input[0] #hello
        self.y = point_input[1]

    def __repr__(self):
        return("X coordinate: {}; Y coordinate: {}".format(self.x, self.y))

class Edge:
    def __init__(self, p1, p2):
        # переменные экземпляра класса. их значения доступны только объекту
        self.p1, self.p2 = (p1, p2)
        
        if (self.p2.x - self.p1.x) != 0:
            self.a = (self.p2.y - self.p1.y)/(self.p2.x - self.p1.x)  
        else:
            self.a = 0
        self.b = self.p1.y - (self.a * self.p1.x)

    def __repr__(self):
        return "Edge(%s, %s)" % (self.p1, self.p2)
    def info(self):
        print("Edge(%s, %s; %s, %s)" % (self.p1.x, self.p1.y, self.p2.x, self.p2.y))
    def on_edge(self, x,y):
        if(x <= max(self.p1.x, self.p2.x)) and (x >= min(self.p1.x, self.p2.x)) and (y <= max(self.p1.y, self.p2.y)) and (y >= min(self.p1.y, self.p2.y)):
            return True
        else:
            return False
    def move_first(self, p):
        self.p1 = p
    def move_second(self, p):
        self.p2 = p


point_input = []
point_coord = []
point_quantity = 0 #Счётчик количества точек
point_arr = []
edge_arr = []

print("Write coordinates of your point, please")
print("Consistenly enter coordinates along the X and Y axis separated by SPACE, please")

for point_input in iter(input, ''):
    point_input = point_input.split()

    # Проверка, ввели ли только 2 координаты
    if not len(point_input) == 2:
        print("ERROR: Two coordinates should be given")
        exit(0)

    # Проверка, ввели ли числа
    try:
        point_input[0] = float(point_input[0])
        point_input[1] = float(point_input[1])

    except:
        print("ERROR: Coordinates should be set by numbers")
        exit(0)

    # print(point_input)

    point_arr.append(Point(point_input))

    point_quantity += 1

#print(point_arr)

# Создание массива граней
len_point_arr = len(point_arr)
for i in range(len_point_arr):
    edge_arr.append(Edge(point_arr[i - len_point_arr], point_arr[i - len_point_arr + 1]))
#print(edge_arr)

# p = Point([1, 2])
# P = Point([2, 4])
# e = Edge(p,P)
# print(e)
