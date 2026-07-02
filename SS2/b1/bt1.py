# PHÂN TÍCH LỖI

# 1. Endpoint đang là /getStudents.
# - Theo em, tên này chưa đúng chuẩn RESTful.
# - Vì đã dùng phương thức GET nên không cần thêm chữ "get" trong URL.
# - Nên đổi thành /students.

# 2. Hàm đang trả về một chuỗi (String).
# - Code dùng:
#   return "Danh sach sinh vien: " + str(students)
# - Kết quả trả về là một chuỗi ký tự.
# - Frontend cần dữ liệu JSON để hiển thị danh sách nên sẽ khó xử lý.

# 3. Không nên nối chuỗi để trả dữ liệu.
# - FastAPI có thể tự chuyển List sang JSON.
# - Chỉ cần return students là đủ.

# - Đổi endpoint từ /getStudents thành /students.
# - Trả về trực tiếp danh sách students.
# - Không dùng phép nối chuỗi.


from fastapi import FastAPI
app = FastAPI()
students = ["An", "Binh", "Cuong"]

@app.get("/students")
def get_students():
    return students