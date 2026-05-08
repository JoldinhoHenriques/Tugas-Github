total_transaction = int(input("Masukkan jumlah transaksi: "))

buyer_name_list = []
item_name_list = []
item_price_list = []

for index in range(total_transaction):
    print(f"\nTransaksi ke-{index + 1}:")
    buyer_name = input("Masukkan Nama Pembeli: ")
    item_name = input("Masukkan Nama Barang: ")
    item_price = float(input("Masukkan Harga Barang: "))

    buyer_name_list.append(buyer_name)
    item_name_list.append(item_name)
    item_price_list.append(item_price)

total_revenue = 0
for price in item_price_list:
    total_revenue += price

for index in range(total_transaction):
    print(f"Pembeli   : {buyer_name_list[index]}")
    print(f"Barang    : {item_name_list[index]}")
    print(f"Harga     : Rp {item_price_list[index]:,.0f}")
print(f"\nTOTAL PENDAPATAN: Rp {total_revenue:,.0f}")
