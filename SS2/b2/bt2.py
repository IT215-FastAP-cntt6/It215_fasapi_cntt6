# Phân tích lỗi
# 1. Endpoint hiện tại trong source code là gì?
# Endpoint hiện tại là /student.

# 2. Vì sao khi gọi GET /students bị lỗi 404 Not Found?
# Vì trong chương trình chưa có endpoint /students, chỉ có /student nên FastAPI báo lỗi 404.

# 3. Vì sao tên endpoint /student chưa phù hợp?
# Vì API này dùng để lấy danh sách nhiều sinh viên nên nên đặt là /students.

# 4. Vì sao return students[0] chưa đúng?
# Vì chỉ trả về sinh viên đầu tiên, không trả về toàn bộ danh sách như đề yêu cầu.

# 5. API đúng theo yêu cầu khách hàng là gì?
# GET /students


from fastapi import FastAPI
app = FastAPI()
students = [
    {"id": 1, "name": "An"},
    {"id": 2, "name": "Binh"},
    {"id": 3, "name": "Cuong"}
]
# Sửa endpoint từ /student thành /students.
# Trả về toàn bộ danh sách sinh viên.
# Đặt tên hàm rõ nghĩa.

@app.get("/students")
def get_students():
    return students