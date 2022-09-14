import os
os.system('cls||clear')

msi_rtxa5000_price = 4199.35
gigabyte_aero_price = 4295.54
razer_blade15_price = 3696.99
asus_zeypherus_m16_price = 1849.79

computers = [msi_rtxa5000_price, gigabyte_aero_price, razer_blade15_price, asus_zeypherus_m16_price]

print(f"The most expensive price: ${max(computers)}")
print(f"The least expensive price ${min(computers)}")

compvge = msi_rtxa5000_price + gigabyte_aero_price + razer_blade15_price + asus_zeypherus_m16_price
average = compvge / 4

print(f"The rounded price of MSI RTX 5000 is: ${round(msi_rtxa5000_price)}")
print(f"The rounded price of Gigabyte Aero is: ${round(gigabyte_aero_price)}")
print(f"The rounded price of Razer Blade 15 is: ${round(razer_blade15_price)}")
print(f"The rounded price of Asus Zeypherus M16 is: ${round(asus_zeypherus_m16_price)}")
print(f"The average price: ${round(average, 2)}")