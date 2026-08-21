from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from backend.database import SessionLocal, init_db
from backend.models.trip import Trip
from backend.services.trip_service import calculate_daily_budget, get_trip_category

app = FastAPI(title="KelanaAI API")

# Inisialisasi database saat aplikasi berjalan
init_db()

class TripRequest(BaseModel):
    destination: str
    days: int
    budget: float

class TripUpdate(BaseModel):
    budget: float

# ==========================================
# ENDPOINT GET (READ) & POST (CREATE)
# ==========================================

@app.post("/api/v1/trips")
def create_trip(request: TripRequest):
    daily_budget = calculate_daily_budget(request.budget, request.days)
    category = get_trip_category(request.budget)
    
    trip = Trip(
        destination=request.destination,
        days=request.days,
        budget=request.budget,
        category=category,
        daily_budget=daily_budget
    )
    
    db = SessionLocal()
    db.add(trip)
    db.commit()
    db.refresh(trip)
    db.close()
    
    return trip

@app.get("/api/v1/trips")
def list_trips():
    db = SessionLocal()
    trips = db.query(Trip).all()
    db.close()
    return trips

@app.get("/api/v1/trips/{trip_id}")
def get_trip(trip_id: int):
    db = SessionLocal()
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    db.close()
    
    if trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip

# ==========================================
# HOMEWORK - TUGAS SESI 4 (PUT & DELETE)
# ==========================================

@app.put("/api/v1/trips/{trip_id}")
def update_trip(trip_id: int, request: TripUpdate):
    db = SessionLocal()
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    
    if trip is None:
        db.close()
        raise HTTPException(status_code=404, detail="Trip not found")
    
    # Memperbarui budget
    trip.budget = request.budget
    
    # Menghitung ulang category dan daily_budget berdasarkan budget baru
    trip.category = get_trip_category(request.budget)
    trip.daily_budget = calculate_daily_budget(request.budget, trip.days)
    
    db.commit()
    db.refresh(trip)
    db.close()
    
    return trip

@app.delete("/api/v1/trips/{trip_id}")
def delete_trip(trip_id: int):
    db = SessionLocal()
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    
    if trip is None:
        db.close()
        # Mengembalikan status 404 jika ID tidak ditemukan sesuai aturan tugas
        raise HTTPException(status_code=404, detail="Trip not found")
        
    db.delete(trip)
    db.commit()
    db.close()
    
    return {"message": f"Trip with id {trip_id} has been deleted"}