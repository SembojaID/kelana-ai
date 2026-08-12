def print_trip_summary(destination, country, days, budget, currency, travel_month):
    print("\n========================")
    print("KelanaAI")
    print("========================")
    print(f"Destination  : {destination}")
    print(f"Country      : {country}")
    print(f"Days         : {days}")
    # Format :g digunakan agar angka desimal .0 tidak muncul jika budget berupa bilangan bulat
    print(f"Budget       : {budget:g} {currency}") 
    print(f"Currency     : {currency}")
    print(f"Travel Month : {travel_month}")

def main():
    # Meminta input interaktif dari pengguna
    destination = input("Masukkan Destination: ")
    country = input("Masukkan Country: ")
    days = int(input("Masukkan Days: "))
    budget = float(input("Masukkan Budget: "))
    currency = input("Masukkan Currency: ")
    travel_month = input("Masukkan Travel Month: ")

    # Memanggil fungsi untuk menampilkan ringkasan
    print_trip_summary(destination, country, days, budget, currency, travel_month)

if __name__ == "__main__":
    main()