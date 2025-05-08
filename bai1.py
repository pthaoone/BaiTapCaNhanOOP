import math
class Point:
    __x = int
    __y = int

    #Phuong phap ghi de (constructor Method Overloadoadingg)
    def __init__ (self,x=0,y=1):
        self.__x = x
        self.__y = y

    def read(self):
        tap = input("nhap vao diem: ")
        self.__x = int(tap.split()[0]) #split dùng để tách chuỗi thành một danh sách phần tử -> lấy phần tử đầu tiên
        self.__y = int(tap.split()[1]) #tap.split()[1] lấy phần tử thức 2 trong danh sách phần tử
    
    def __str__(self):
        return f"({self.__x},{self.__y})\n" #__str__ dùng để định dạng lại chuỗi
    
    def move(self, dx = 0, dy = 0):
        self.__x += dx
        self.__y += dy

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    #Phương thức Method Overloading
    def distance(self, *args):
        if len(args) == 0:
            return math.sqrt(self.__x**2 + self.__y**2)
        if len(args) == 1 and isinstance(args[0], Point):
            return math.sqrt((self.__x - args[0].getX())**2 + (self.__y - args[0].getY())**2)

class PointTest:
    def main(self):
        diemA = Point(3,4)
        print(diemA)

        diemB = Point()
        diemB.read()
        print(diemB)

        diemC = Point(-diemB.getX(), -diemB.getY())
        print(diemC)
            
        print(diemB.distance())
        print(diemA.distance(diemB))
        
PointTest().main()
