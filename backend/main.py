# backend/main.py

# Mengimpor fungsi logika bisnis dari modul services.trip_service
from services.trip_service import (
    get_trip_category, 
    get_travel_session, 
    calculate_daily_budget, 
    get_recommended_places
)

def main():
    # Menangani interaksi I/O pengguna
    destination = input("Masukkan Destination: ")
    days = int(input("Masukkan Days: "))
    budget = float(input("Masukkan Budget: "))
    currency = input("Masukkan Currency (contoh: USD): ")
    travel_month = input("Masukkan Travel Month: ")

    # Memproses data menggunakan fungsi dari trip_service
    category = get_trip_category(budget)
    season = get_travel_session(travel_month)
    daily_budget = calculate_daily_budget(budget, days)
    places = get_recommended_places(destination)

    # Menampilkan hasil akhir
    print("\n==================================")
    print("KelanaAI")
    print("==================================")
    print(f"Destination  : {destination}")
    print(f"Days         : {days}")
    print(f"Budget       : {budget:g} {currency}")
    print(f"Category     : {category}")
    print(f"Daily Budget : {daily_budget:g} {currency}/Day")
    print(f"Travel Month : {travel_month}")
    print(f"Season       : {season}")
    print("Recommended Places")
    
    # Iterasi menggunakan Loop for untuk menampilkan tempat
    for place in places:
        print(place)

if __name__ == "__main__":
    main()c