# Input
# Là danh sách books, mỗi sách gồm id, title và quantity.

# Output
# API trả về danh sách các sách có số lượng nhỏ hơn hoặc bằng 5.

# Nếu không có sách nào sắp hết hàng thì trả về:
# {
#     "message": "Không có sách nào sắp hết hàng",
#     "data": []
# }
# Điều kiện xác định sách sắp hết hàng
# Sách có quantity <= 5.

# Giải pháp 1: Dùng vòng lặp for
# Duyệt từng quyển sách trong danh sách.
# Nếu sách hợp lệ và quantity <= 5 thì thêm vào danh sách kết quả.
# Giải pháp 2: Dùng List Comprehension
# Dùng List Comprehension để lọc các sách có quantity <= 5.

+--------------------------+-------------------------------+--------------------------------+
| Tiêu chí                 | Vòng lặp for                  | List Comprehension             |
+--------------------------+-------------------------------+--------------------------------+
| Độ dễ hiểu               | Dễ hiểu, dễ đọc              | Khó hiểu hơn                   |
| Độ ngắn gọn              | Code dài hơn                 | Code ngắn gọn hơn              |
| Dễ xử lý bẫy dữ liệu     | Dễ thêm điều kiện kiểm tra   | Khó xử lý nhiều điều kiện      |
| Dễ bảo trì               | Dễ sửa, dễ bảo trì           | Khó sửa khi code phức tạp      |
+--------------------------+-------------------------------+--------------------------------+

#Em chọn dùng vòng lặp for vì dễ đọc, dễ xử lý các trường hợp thiếu dữ liệu hoặc dữ liệu không hợp lệ. Cách này cũng phù hợp với người mới học Python.

# Các bước xử lý
# Bước 1: Khởi tạo FastAPI.
# Bước 2: Khai báo danh sách books.
# Bước 3: Tạo endpoint GET /books/low-stock.
# Bước 4: Duyệt từng quyển sách.
# Bước 5: Nếu sách không có quantity thì bỏ qua.
# Bước 6: Nếu quantity < 0 thì bỏ qua.
# Bước 7: Nếu quantity <= 5 thì thêm vào danh sách kết quả.
# Bước 8: Nếu danh sách kết quả rỗng thì trả về thông báo.
# Bước 9: Nếu có dữ liệu thì trả về danh sách sách sắp hết hàng.

from fastapi import FastAPI
app = FastAPI()
books = [
    {"id": 1, "title": "Python Basic", "quantity": 12},
    {"id": 2, "title": "FastAPI Beginner", "quantity": 3},
    {"id": 3, "title": "Clean Code", "quantity": 5},
    {"id": 4, "title": "Database Design", "quantity": 0},
    {"id": 5, "title": "Web API Design", "quantity": 20},
    {"id": 6, "title": "Java Basic"},
    {"id": 7, "title": "Spring Boot", "quantity": -2}
]

@app.get("/books/low-stock")
def get_low_stock_books():
    low_stock = []
    for book in books:

    # Nếu không có quantity thì bỏ qua
        if "quantity" not in book:
            continue
        # Nếu quantity âm thì bỏ qua
        if book["quantity"] < 0:
            continue
        # Lấy các sách có số lượng <= 5
        if book["quantity"] <= 5:
            low_stock.append(book)
    if len(low_stock) == 0:
        return {
            "message": "Không có sách nào sắp hết hàng",
            "data": []
        }
    return {
        "message": "Danh sách sách sắp hết hàng",
        "data": low_stock
    }