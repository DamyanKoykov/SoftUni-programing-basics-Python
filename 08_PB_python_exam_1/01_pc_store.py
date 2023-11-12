cpu_price_dollars = float(input())
gpu_price_dollars = float(input())
ram_price_dollars = float(input())
ram_quantity_ordered = int(input())
percent_discount_for_cpu_and_gpu = float(input())

# converting from dollars to BGN and applying the discount for CPU and GPU
cpu_price_bgn = (cpu_price_dollars * 1.57) * (1 - percent_discount_for_cpu_and_gpu)
gpu_price_bgn = (gpu_price_dollars * 1.57) * (1 - percent_discount_for_cpu_and_gpu)
ram_price_bgn = ram_price_dollars * 1.57

total_cost = cpu_price_bgn + gpu_price_bgn + (ram_price_bgn * ram_quantity_ordered)

print(f"Money needed - {total_cost :.2f} leva.")
