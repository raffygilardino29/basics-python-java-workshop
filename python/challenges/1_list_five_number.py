# 1. Buat list berisi 5 angka
numbers = [29, 26, 5, 45, 12]
print("List awal:", numbers)

# 2. TODO: Tampilkan angka pertama dan terakhir
print(f"Angka pertama: {numbers[0]} ")
print(f"Angka terakhir: {numbers[-1]}")

# 3. TODO: Tambahkan angka baru (apapun) ke akhir list
numbers.append(22)
print("List setelah ditambah:", numbers )

# 4. TODO: Urutkan list secara descending
numbers.sort()
print("list setelah diurutkan :", numbers)
# 5. Tampilkan hasil akhir
numbers.sort(reverse=True)
print("List urut descending:", numbers)
