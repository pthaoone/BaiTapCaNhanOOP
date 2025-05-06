from bai1 import Point

class ColorPoint(Point):
    def __init__(self, x=0, y=0, color="xanh"):
        super().__init__(x, y)
        self.__color = color

    @classmethod
    def from_color_point(cls, cp: 'ColorPoint'): #Phương thức thay thế cho constructor sao chép
        return cls(cp.getX(), cp.getY(), cp.get_color())

    def get_color(self): #Getter cho thuộc tính private __color
        return self.__color
    
    def read(self):
        super().read()
        self.__color = input("Nhập màu: ").strip()

    def __str__(self):
        point_str = super().__str__().strip()  # loại bỏ \n
        return f"{point_str}: {self.__color}"

    def setColor(self, color):
        self.__color = color

class C002454:
    @staticmethod
    def testCase1():
        A = ColorPoint(5, 10, "trắng")
        print(A)

    @staticmethod
    def testCase2():
        B = ColorPoint()
        print("Nhập thông tin cho điểm B (x y màu).")
        B.read()
        B.move(10, 8)
        print("Thông tin điểm B sau khi di chuyển (10, 8):", B)

    @staticmethod
    def testCase3():
        C = ColorPoint(6, 3, "đen")
        D = ColorPoint.from_color_point(C)
        print("Thông tin điểm D (sao chép từ C):", D)
        D.setColor("vàng")
        print("Thông tin điểm D sau khi đổi màu:", D)
        print("Thông tin điểm C (không đổi):", C)

    @staticmethod
    def main():
        while True:
            print("\nChọn kịch bản muốn chạy:")
            print("1. Kịch bản 1")
            print("2. Kịch bản 2")
            print("3. Kịch bản 3")
            print("0. Thoát")
            choice = input("Nhập lựa chọn: ").strip()
            if choice == "1":
                C002454.testCase1()
            elif choice == "2":
                C002454.testCase2()
            elif choice == "3":
                C002454.testCase3()
            elif choice == "0":
                print("Thoát chương trình.")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    C002454.main()