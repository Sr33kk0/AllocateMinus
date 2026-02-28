from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import os
import arrow

from core_engine import find_group_free_time

def get_resource_path(relative_path):
    """
    Get the absolute path to a resource.
    """
    return os.path.join(os.path.abspath("."), relative_path)

app = FastAPI(title="AllocateMinus Backend API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.get("/", response_class=HTMLResponse)
def read_root():
    index_path = get_resource_path("index.html")
    
    try:
        with open(index_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "<h1>Welcome to AllocateMinus API</h1><p>index.html was not found alongside the executable.</p>"

class CalculateRequest(BaseModel):
    urls: List[str]
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    start_hour: Optional[int] = 8
    end_hour: Optional[int] = 18
    min_duration: int = 30

@app.post("/api/calculate")
def calculate_free_time(request_data: CalculateRequest):
    try:
        start_arrow = None
        end_arrow = None
        if request_data.start_date:
            start_arrow = arrow.get(request_data.start_date).to('local').floor('day')
        if request_data.end_date:
            end_arrow = arrow.get(request_data.end_date).to('local').ceil('day')

        raw_free_slots, all_events_count = find_group_free_time(
            urls=request_data.urls,
            start_date=start_arrow,
            end_date=end_arrow,
            start_hour=request_data.start_hour,
            end_hour=request_data.end_hour,
            min_duration_minutes=request_data.min_duration
        )
        
        formatted_slots = []
        for start, end in raw_free_slots:
            formatted_slots.append({
                "start": start.format('YYYY-MM-DD HH:mm'),
                "end": end.format('YYYY-MM-DD HH:mm'),
                "start_iso": start.isoformat(),
                "end_iso": end.isoformat()
            })
            
        return {
            "status": "success",
            "events_processed": all_events_count,
            "free_slots": formatted_slots
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.on_event("startup")
async def startup_event():
    print("\n" + "="*50)
    print("🚀 AllocateMinus API Server started successfully!")
    print("👉 👉 Access the application at: http://localhost:8000 👈 👈")
    print("="*50 + "\n")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
