class MyBigNumber:
    def sum(self, str1, str2):
        result = []
        temp = 0  # Biến để lưu giá trị nhớ, khởi tạo ban đầu bằng 0 vì chưa có giá trị nhớ


        # Tìm max length của 2 string làm điều kiện dừng cho vòng for
        max_length = max(len(str1), len(str2))

        for i in range(1, max_length+1):
            # Lấy kí số từng chuỗi số, nếu không có thì lấy 0
            digit1 = int(str1[-i]) if i <= len(str1) else 0
            digit2 = int(str2[-i]) if i <= len(str2) else 0

            # Tính tổng của hai kí số và giá trị nhớ
            sum_str1_and_str2 = digit1 + digit2 + temp

            # Dùng phép chia cho 10 lấy số dư sau đó lấy số dư đó insert vào vị trí cuối cùng bên phải của tổng vào kết quả
            result.insert(0, str(sum_str1_and_str2 % 10))

            # Ghi nhận lịch sử phép toán và in ra
            print(f"Bước {len(result)}: Lấy {digit1} cộng với {digit2} nhớ {temp} được {sum_str1_and_str2}. Lưu {sum_str1_and_str2 % 10} vào kết quả và nhớ {sum_str1_and_str2 // 10}")

            # Cập nhật giá trị nhớ cho lần cộng tiếp theo
            temp = sum_str1_and_str2 // 10


        # Nếu sau khi cộng hết các kí số mà vẫn còn giá trị nhớ
        if temp > 0:
            result.insert(0, str(temp))

            # Ghi nhận lịch sử phép toán
            print(f"Bước {len(result)}: Nhớ {temp} cuối cùng. Thêm {temp} vào kết quả")

        return ''.join(result)

# Tạo đối tượng my_big_number thuộc class MyBigNumber
my_big_number = MyBigNumber()
result = my_big_number.sum("334", "897")
print("Kết quả:", result)
