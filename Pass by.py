def konversi_suhu(nilai, satuan):
    if satuan == 'C':
        # Mengubah Celcius ke Fahrenheit
        fahrenheit = (nilai * 9/5) + 32
        return f"{nilai}°C = {fahrenheit}°F"
    elif satuan == 'F':
        # Mengubah Fahrenheit ke Celcius
        celcius = (nilai - 32) * 5/9
        return f"{nilai}°F = {celcius}°C"
    else:
        return "Satuan tidak valid. Gunakan 'C' untuk Celcius atau 'F' untuk Fahrenheit."

# Contoh penggunaan
print(konversi_suhu(100, 'C'))  # Output: 212.0
print(konversi_suhu(32, 'F'))    # Output: 0.0
