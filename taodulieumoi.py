import pandas as pd

# Tạo một dòng dữ liệu mới về đơn hàng
def create_new_data():
    # Nhập dữ liệu từ người dùng
    order_id = input("Nhap Order ID: ")
    amount = float(input("Nhap so tien (Amount): "))
    profit = float(input("Nhap loi nhuan (Profit): "))
    quantity = int(input("Nhap so luong (Quantity): "))
    category = input("Nhap danh muc (Category): ")
    sub_category = input("Nhap phan loai (Sub-Category): ")
    payment_mode = input("Nhap phuong thuc thanh toan (PaymentMode): ")

    # Nhập thêm thông tin bổ sung
    order_date = input("Nhap ngay dat hang (Order Date - dd/mm/yyyy): ")
    customer_name = input("Nhap ten khach hang (CustomerName): ")
    state = input("Nhap bang/tinh (State): ")
    city = input("Nhap thanh pho (City): ")

    # Tạo dữ liệu mới dưới dạng dictionary
    new_data = {
        "Order ID": order_id,
        "Amount": amount,
        "Profit": profit,
        "Quantity": quantity,
        "Category": category,
        "Sub-Category": sub_category,
        "PaymentMode": payment_mode,
        "Order Date": order_date,
        "CustomerName": customer_name,
        "State": state,
        "City": city
    }

    return new_data

# Tạo dữ liệu mới và lưu vào DataFrame
new_data = create_new_data()
df = pd.DataFrame([new_data])

# Lưu vào file CSV
df.to_csv('onlinesales_sorted.csv', mode='a', header=False, index=False)

print("Du lieu moi da duoc tao va luu vao file.")
