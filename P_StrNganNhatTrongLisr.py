def find_shortest_string(lst):
    # Hàm này nhận vào một danh sách chuỗi và trả về chuỗi có độ dài ngắn nhất trong danh sách.
    return min(lst, key=len)  # Sử dụng hàm min() với key=len để trực tiếp trả về chuỗi có độ dài ngắn nhất

def main():
    lst = [input(f"Nhập chuỗi thứ {i+1}: ") for i in range(int(input("Nhập số lượng chuỗi: ")))]  
   
    shortest_string = find_shortest_string(lst)  # Gọi hàm find_shortest_string() để tìm chuỗi ngắn nhất
    print("Chuỗi ngắn nhất trong danh sách là:", shortest_string)

if __name__ == "__main__":
    main()
 