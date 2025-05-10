import json

class TuLanh:
    def __init__(self, nhanhieu="Elextrolux", maso="UNKNOWN", nuocsx="Việt Nam", tkdien=True, dungtich=256, gia=7000000):
        self.__nhanhieu = nhanhieu
        self.__maso = maso
        self.__nuocsx = nuocsx
        self.__tkdien = tkdien
        self.__dungtich = dungtich
        self.__gia = gia

    def makeCopy(self, tl: 'TuLanh'):
        self.__nhanhieu = tl.__nhanhieu
        self.__maso = tl.__maso
        self.__nuocsx = tl.__nuocsx
        self.__tkdien = tl.__tkdien
        self.__dungtich = tl.__dungtich
        self.__gia = tl.__gia

    def nhapThongTin(self):
        self.__nhanhieu = input("Nhập nhãn hiệu: ").strip()
        self.__maso = input("Nhập mã số: ").strip()
        self.__nuocsx = input("Nhập nước sản xuất: ").strip()
        self.__tkdien = input("Tiết kiệm điện (Có/Không): ").strip().lower() == "Có"
        self.__dungtich = int(input("Nhập dung tích (lít): ").strip())
        self.__gia = int(input("Nhập giá (VNĐ): ").strip())

    def hienThi(self):
        print(f"Nhà sản xuất: {self.__nhanhieu}")
        print(f"Mã số: {self.__maso}")
        print(f"Nước sản xuất: {self.__nuocsx}")
        print(f"Tiết kiệm điện: {'Có' if self.__tkdien else 'Không'}")
        print(f"Dung tích: {self.__dungtich} lít")
        print(f"Giá: {self.__gia} VNĐ")

    def layNhanHieu(self):
        return self.__nhanhieu

    def layGia(self):
        return self.__gia

    def soNguoiSD(self):
        return self.__dungtich // 100

    def cungNhanHieu(self, tl: 'TuLanh'):
        return self.__nhanhieu == tl.__nhanhieu

    def nhHon(self, tl: 'TuLanh'):
        return self.__dungtich < tl.__dungtich
    
class C002454:
    def testCase1():
        tl1 = TuLanh()
        print("Nhập thông tin cho tủ lạnh tl1:")
        tl1.nhapThongTin()

        tl2 = TuLanh("LG", "LG-28382", "Hàn Quốc", True, 600, 43000000)
        print("\nThông tin tủ lạnh tl2:")
        tl2.hienThi()

        tl3 = TuLanh()
        tl3.makeCopy(tl1)
        print("\nThông tin tủ lạnh tl3 (sao chép từ tl1):")
        tl3.hienThi()

    def testCase2():
        n = int(input("Nhập số lượng tủ lạnh (0 < n < 100): "))
        ds_tulanh = []

        for i in range(n):
            print(f"\nNhập thông tin cho tủ lạnh thứ {i + 1}:")
            tl = TuLanh()
            tl.nhapThongTin()
            ds_tulanh.append(tl)

        print("\nDanh sách tủ lạnh theo thứ tự ngược lại:")
        for tl in reversed(ds_tulanh):
            tl.hienThi()

    def testCase3():
        n = int(input("Nhập số lượng tủ lạnh (0 < n < 100): "))
        ds_tulanh = []

        for i in range(n):
            print(f"\nNhập thông tin cho tủ lạnh thứ {i + 1}:")
            tl = TuLanh()
            tl.nhapThongTin()
            ds_tulanh.append(tl)

        # Sắp xếp danh sách theo giá giảm dần
        ds_tulanh.sort(key=lambda x: x.layGia(), reverse = True)

        print("\nDanh sách tủ lạnh sắp xếp theo giá giảm dần:")
        for tl in ds_tulanh:
            tl.hienThi()

    def testCase4():
        n = int(input("Nhập số lượng tủ lạnh (0 < n < 100): "))
        ds_tulanh = []

        for i in range(n):
            print(f"\nNhập thông tin cho tủ lạnh thứ {i + 1}:")
            tl = TuLanh()
            tl.nhapThongTin()
            ds_tulanh.append(tl)

        # Lưu danh sách vào file JSON
        with open("DsTuLanh.json", "w", encoding = "utf-8") as f:
            json.dump([{
                "nhanhieu": tl.layNhanHieu(),
                "maso": tl._TuLanh__maso,
                "nuocsx": tl._TuLanh__nuocsx,
                "tkdien": tl._TuLanh__tkdien,
                "dungtich": tl._TuLanh__dungtich,
                "gia": tl.layGia()
            } 
            for tl in ds_tulanh], f, ensure_ascii = False, indent = 4)
        print("\nDanh sách tủ lạnh đã được lưu vào DsTuLanh.json")

    def testCase5():
        n = int(input("Nhập số lượng tủ lạnh (0 < n < 100): "))
        ds_tulanh = []

        for i in range(n):
            print(f"\nNhập thông tin cho tủ lạnh thứ {i + 1}:")
            tl = TuLanh()
            tl.nhapThongTin()
            ds_tulanh.append(tl)

        # Thống kê số lượng tủ lạnh theo nhãn hiệu
        thong_ke = {}
        for tl in ds_tulanh:
            nhanhieu = tl.layNhanHieu()
            thong_ke[nhanhieu] = thong_ke.get(nhanhieu, 0) + 1

        # Hiển thị thống kê theo thứ tự ABC
        print("\nThống kê số lượng tủ lạnh theo nhãn hiệu:")
        for nhanhieu in sorted(thong_ke.keys()):
            print(f"{nhanhieu} ({thong_ke[nhanhieu]})")

    def main():
        """Kịch bản tổng hợp: Chọn và chạy các kịch bản"""
        while True:
            print("\nChọn kịch bản muốn chạy:")
            print("1. Kịch bản 1")
            print("2. Kịch bản 2")
            print("3. Kịch bản 3")
            print("4. Kịch bản 4")
            print("5. Kịch bản 5")
            print("0. Thoát")
            choice = input("Nhập lựa chọn: ").strip()
            if choice == "1":
                C002454.testCase1()
            elif choice == "2":
                C002454.testCase2()
            elif choice == "3":
                C002454.testCase3()
            elif choice == "4":
                C002454.testCase4()
            elif choice == "5":
                C002454.testCase5()
            elif choice == "0":
                print("Thoát chương trình.")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    C002454.main()
    