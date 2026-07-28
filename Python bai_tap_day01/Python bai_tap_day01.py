raw_cart = [
    {"id": "SP1", "ten": " Áo sơ mi nam ", "gia": 150000, "sl": 2, "danh_muc": "Thời trang"},
    {"id": "SP2", "ten": "Quần tây ", "gia": 250000, "sl": 1, "danh_muc": "Thời trang"},
    {"id": "SP3", "ten": " Giày thể thao ", "gia": 450000, "sl": 1, "danh_muc": "Giày dép"},
    {"id": "SP4", "ten": "Tất cổ ngắn ", "gia": 30000, "sl": 5, "danh_muc": "Phụ kiện"}
]

# BÀI 1
for item in raw_cart:
    item["ten"] = item["ten"].strip()
    item["tong_tien"] = item["gia"] * item["sl"]

sp5 = {"id": "SP5", "ten": "Áo khoác", "gia": 320000, "sl": 1, "danh_muc": "Thời trang", "tong_tien": 320000}
raw_cart.append(sp5)

raw_cart = [item for item in raw_cart if item["id"] != "SP4"]

print("Kết quả Bài 1:")
for item in raw_cart:
    print(item)

# BÀI 2
danh_muc_set = set(item["danh_muc"] for item in raw_cart)
sp_cao_cap = [
    item["ten"]
    for item in raw_cart
    if item["tong_tien"] > 200000
]
print("\nKết quả Bài 2:")
print("Danh mục duy nhất (Set):", danh_muc_set)
print("Sản phẩm > 200k (List Comprehension):", sp_cao_cap)