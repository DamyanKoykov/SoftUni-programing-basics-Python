skumriq_price_kg = float(input())
caca_price_kg = float(input())
palamud_quantity_ordered = float(input())
safrid_quantity_ordered = float(input())
midi_quantity_ordered = int(input())

palamud_price_kg = skumriq_price_kg * 1.60
safrid_price_kg = caca_price_kg * 1.80
midi_price_kg = 7.50

total_cost = (palamud_quantity_ordered * palamud_price_kg + safrid_quantity_ordered *
              safrid_price_kg + midi_quantity_ordered * midi_price_kg)

print(f"{total_cost :.2f}")
