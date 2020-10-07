class Point:
    def __init__(self, x, y):  # конструктор класса с параметрами
        self.x, self.y = (x, y)

    def __repr__(self):
        return "Point(%s, %s)" % (self.x, self.y)


class Figure:
    # переменная класса. сколько всего элементов создано
    count = 0

    # конструктор класса. вызывается при создании экземпляра
    def __init__(self, name):
        # переменные экземпляра класса. их значения доступны только объекту
        self.list_of_coords = []
        self.name = name

        # увеличиваем значение переменной класса
        Figure.count += 1

        def push(self, p):
            list_of_coords.append(p)

        def info(self):
            print('Имя: ', self.name,
                  '\nВсего фигур: ', Figure.count)


class Edge:
    def __init__(self, p1, p2):
        # переменные экземпляра класса. их значения доступны только объекту
        self.p1, self.p2 = (p1, p2)

    def __repr__(self):
        return "Edge(%s, %s)" % (self.p1, self.p2)

    def info(self):
        print("Edge(%s, %s; %s, %s)" % (self.p1.x, self.p1.y, self.p2.x, self.p2.y))

    def on_edge(self, x, y):
        if (x <= max(p1.x, p2.x)) and (x >= min(p1.x, p2.x)) and (y <= max(p1.y, p2.y)) and (y >= min(p1.y, p2.y)):
            return True
        else:
            return False

    def move_first(self, p):
        self.p1 = p

    def move_second(self, p):
        self.p2 = p

p = Point(1, 2)
P = Point(2, 4)
e = Edge(p, P)
print(e)
#t = input()
p3= Point(13,2)
e.move_first(p3)
print(e)