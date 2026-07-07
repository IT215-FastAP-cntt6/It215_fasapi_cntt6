from fastapi import FastAPI
app = FastAPI(
    title="E-commerce",
    description="He thong Phan tich Don hang"
)

mock_orders = [
    {"id": 1, "customer_name": "Nguyen Van A", "total_amount": 500000, "status": "delivered"},
    {"id": 2, "customer_name": "Nguyen Van B", "total_amount": 200000, "status": "pending"},
    {"id": 3, "customer_name": "Nguyen Van A", "total_amount": 350000, "status": "delivered"},
    {"id": 4, "customer_name": "Nguyen Van C", "total_amount": 350000, "status": "delivered"},
    {"id": 5, "customer_name": "Nguyen Van B", "total_amount": 500000, "status": "delivered"},
    {"id": 6, "customer_name": "Nguyen Van D", "total_amount": 150000, "status": "cancelled"},
]

@app.get("/orders/revenue-report")
def get_orders():
    total_revenue = 0
    successful_revenue = 0
    for order in mock_orders:
        total_revenue += order.get("total_amount")
        if order.get("status") == "delivered":
            successful_revenue += order.get("total_amount")
    average_order_value = total_revenue / len(mock_orders)
    return {
        "total_revenue": total_revenue,
        "successful_revenue": successful_revenue,
        "average_order_value": average_order_value
    }