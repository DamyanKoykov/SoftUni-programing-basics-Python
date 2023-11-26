parcel_count = int(input())

bus_price_per_ton = 200
lorry_price_per_ton = 175
train_price_per_ton = 120

total_price = 0
total_weight = 0
bus_delivered_tons = 0
lorry_delivered_tons = 0
train_delivered_tons = 0
for _ in range(1, parcel_count + 1):
    weight_current_parcel_ton = int(input())
    if weight_current_parcel_ton <= 3:
        total_price += (bus_price_per_ton * weight_current_parcel_ton)
        bus_delivered_tons += weight_current_parcel_ton
    elif 4 <= weight_current_parcel_ton <= 11:
        total_price += (lorry_price_per_ton * weight_current_parcel_ton)
        lorry_delivered_tons += weight_current_parcel_ton
    elif 12 <= weight_current_parcel_ton:
        total_price += (train_price_per_ton * weight_current_parcel_ton)
        train_delivered_tons += weight_current_parcel_ton
    total_weight += weight_current_parcel_ton

average_price_per_ton = total_price / total_weight
bus_delivery_percent = (100 / total_weight) * bus_delivered_tons
lorry_delivery_percent = (100 / total_weight) * lorry_delivered_tons
train_delivery_percent = (100 / total_weight) * train_delivered_tons
print(f"{average_price_per_ton :.2f}")
print(f"{bus_delivery_percent :.2f}%")
print(f"{lorry_delivery_percent :.2f}%")
print(f"{train_delivery_percent :.2f}%")
