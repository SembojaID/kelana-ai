from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Mengimpor fungsi logika bisnis dari Sesi 2 tanpa mengubahnya
from services.trip_service import calculate_daily_budget, get_trip_category

# Membuat instance aplikasi FastAPI
app = FastAPI(title="KelanaAI API")

# Membuat Pydantic Model untuk memvalidasi data input JSON
class TripRequest(BaseModel):
    destination: str
    days: int
    budget: float

# ==========================================
# 1. ENDPOINT UTAMA (WAJIB)
# ==========================================

# Endpoint Welcome (Home Route)
@app.get("/")
def home():
    return {
        "message": "Welcome to KelanaAI"
    }

# Endpoint Health Check
@app.get("/health")
def health_check():
    return {
        "status": "OK"
    }

# Endpoint Membuat Rencana Perjalanan (POST)
@app.post("/api/v1/trips")
def create_trip(request: TripRequest):
    # Memproses data menggunakan fungsi dari trip_service Sesi 2
    daily_budget = calculate_daily_budget(request.budget, request.days)
    category = get_trip_category(request.budget)
    
    return {
        "destination": request.destination,
        "days": request.days,
        "budget": request.budget,
        "daily_budget": daily_budget,
        "category": category
    }

# ==========================================
# 2. HOMEWORK - TWO NEW ENDPOINTS (Halaman 21)
# ==========================================

# Endpoint Mendapatkan Daftar Rekomendasi Tempat
@app.get("/api/v1/recommendations", response_model=List[str])
def get_recommendations():
    return ["Tokyo Tower", "Mount Fuji", "Shibuya"]

# Endpoint Mendapatkan Daftar Transportasi
@app.get("/api/v1/transportations", response_model=List[str])
def get_transportations():
    return ["Bus", "Train", "Flight"]
#
#
# Endpoint 1: Mengembalikan daftar rekomendasi tempat wisata
@app.get("/api/v1/recommendations")
def get_recommendations():
    return ["Tokyo Tower", "Mount Fuji", "Shibuya"] #

# Endpoint 2: Mengembalikan daftar pilihan moda transportasi
@app.get("/api/v1/transportations")
def get_transportations():
    return ["Bus", "Train", "Flight"] #