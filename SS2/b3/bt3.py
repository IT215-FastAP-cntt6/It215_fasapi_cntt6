# Input
# Là danh sách students gồm id, name và status.

# Output
# API trả về danh sách các sinh viên có status là "active".
# Nếu không có sinh viên đang học thì trả về:

# {
#     "message": "Không có sinh viên đang học",
#     "data": []
# }


# Điều kiện xác định sinh viên đang học
# Sinh viên có status bằng "active".

# Các bước xử lý
# Bước 1: Tạo endpoint GET /students/active.
# Bước 2: Duyệt từng sinh viên trong danh sách.
# Bước 3: Nếu status bằng "active" thì thêm vào danh sách kết quả.
# Bước 4: Nếu danh sách kết quả rỗng thì trả về thông báo "Không có sinh viên đang học".
# Bước 5: Nếu có dữ liệu thì trả về thông báo và danh sách sinh viên đang học.

from fastapi import FastAPI
app = FastAPI()

students = [
    {"id": 1, "name": "An", "status": "active"},
    {"id": 2, "name": "Binh", "status": "inactive"},
    {"id": 3, "name": "Cuong", "status": "active"},
    {"id": 4, "name": "Dung", "status": "pending"}
]

@app.get("/students/active")
def get_active_students():
    active_students = []
    for student in students:
        if student["status"] == "active":
            active_students.append(student)
    if len(active_students) == 0:
        return {
            "message": "Không có sinh viên đang học",
            "data": []
        }
    return {
        "message": "Danh sách sinh viên đang học",
        "data": active_students
    }