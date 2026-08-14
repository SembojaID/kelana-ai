# backend/services/trip_service.py

def get_trip_category(budget):
    # Menentukan kategori berdasarkan anggaran (budget)
    if budget < 1000:
        return "Backpacker"
    elif budget <= 3000:
        return "Standard"
    else:
        return "Luxury"

def get_travel_session(month):
    # Menentukan kategori berdasarkan bulan (month)
    if month.lower() == "december":
        return "Peak Season"
    elif month.lower() == "june":
        return "Holiday Season"
    else:
        return "Regular Season"

def calculate_daily_budget(budget, days):
    # Menghitung pembagian anggaran dengan hari
    if days <= 0:
        return 0
    return budget / days

def get_recommended_places(destination):
    # Menggunakan tipe data list untuk menyimpan daftar tempat tujuan
    if destination.lower() == "japan":
        return ["Tokyo Tower", "Shibuya", "Mount Fuji"]
    else:
        return [f"City Center of {destination}", f"Museum of {destination}", f"National Park of {destination}"]