from bai1 import Point
import math

class LineSegment:
    __d1 = Point()
    __d2 = Point(0)

    def __init__(self, *args):
        if len(args) == 0:
            self.__d1 = Point(8,5)
            self.__d2 = Point(1,0)
        
        if len(args) == 2:
            if not (isinstance(args[0], Point) and isinstance(args[1], Point)):
                raise TypeError("Point should be used!")
            self.__d1 = args[0]
            self.__d2 = args[1]

        if len(args) == 4:
            if not all(isinstance(item,Point) for item in args):
                raise TypeError("only intergers can be added!")
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[1])

        if len(args) == 1:
            if not (isinstance(args[0], LineSegment)):
                raise TypeError("only a line segment can be added!")
            #sao chép sau tạo ra đối tượng mới
            self.__d1 = Point(args[0].__d1.getX(), args[0].__d1.getY())
            self.__d2 = Point(args[0].__d2.getX(), args[0].__d2.getY())

    def read(self):
        tap = input("nhập vào Đoạn thẳng: ")
        self.__d1 = Point(int(tap.split()[0]), int(tap.split()[1]))
        self.__d2 = Point(int(tap.split()[2]), int(tap.split()[1]))

    def __str__(self):
        return f"[({self.__d1.getX()}, {self.__d1.getY()});({self.__d2.getX()}, {self.__d2.getY()})]"
    
    def move(self, dx, dy):
        self.__d1.move(dx,dy)
        self.__d2.move(dx,dy)
    
    def length(self):
        return self.__d1.distance(self.__d2)
    
    def angle(self):
        return int(math.atan2(self.__d2.getY() - self.__d1.getY(), self.__d2.getX() - self.__d1.getX()))
    
class LineSegmentTest:
    def testCase1(self):
        diemA = Point(2,5)
        diemB = Point(20,35)
        doanAB = LineSegment(diemA, diemB)
        doanAB.move(35,51)
        print(doanAB)

    def testCase2(self):
        doanCD = LineSegment()
        doanCD.read()
        print("|CD| = {:2f}".format(doanCD.length())) #cách làm tròn đến 2 số lẻlẻ

    def testCase3(self):
        n = int(input("Nhập n: "))
        danhsach = [] #danh sách rỗng để lưu các đối tượng
        for i in range(n):
            l1 = LineSegment()
            l1.read()
            danhsach.append(l1)

        #hiển thị các đoạn thẳng trong danh sách
        print("Danh sách trước khi sắp xếp: ")
        for item in danhsach:
            print(item)
            print(item.length())

        #sắp xếp đoạn thẳng theo độ dài
        danhsach.sort(key = lambda dist: dist.length())
        print("Danh sách sau khi sắp xếp: ")
        for item in danhsach:
            print(item)
            print(item.length())

    def main(self):
        while True:
            s = input("nhập kịch bản muốn chạy 1/2/3/exit:")
            if s == '1':
                LineSegmentTest().testCase1()
            if s == '2':
                LineSegmentTest().testCase2()
            if s == '3':
                LineSegmentTest().testCase3()
            if s == 'exit':
                break

LineSegmentTest().main()