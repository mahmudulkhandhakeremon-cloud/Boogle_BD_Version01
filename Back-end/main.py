from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from pathlib import Path

app = FastAPI(title="Boogle API", description="API for searching top websites", version="1.0")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------------------
# CSV ফাইলের সঠিক পাথ (Path) সেটআপ
# -------------------------------------------------------------
# main.py যে ফোল্ডারে (Back-end) আছে, তার এক লেভেল উপরে গিয়ে data ফোল্ডারে খোঁজা হবে
BASE_DIR = Path(__file__).resolve().parent.parent
CSV_FILE_PATH = BASE_DIR / "data" / "top_100_websites.csv"

def load_data():
    """CSV ফাইল লোড করে Pandas DataFrame রিটার্ন করার ফাংশন"""
    if CSV_FILE_PATH.exists():
        df = pd.read_csv(CSV_FILE_PATH)
        # কলামের নামের স্পেস দূর করা
        df.columns = df.columns.str.strip()
        return df
    else:
        print(f"Error: File not found at {CSV_FILE_PATH}")
        return None

# -------------------------------------------------------------
# API Endpoints
# -------------------------------------------------------------

@app.get("/")
def home():
    return {"message": "Welcome to Boogle API!"}

# ১. সব ওয়েবসাইটের ডেটা দেখানোর জন্য
@app.get("/websites")
def get_all_websites():
    df = load_data()
    if df is None:
        return {"error": f"CSV File not found at path: {CSV_FILE_PATH}"}
    
    websites = df.to_dict(orient="records")
    return {"total": len(websites), "websites": websites}

# ২. সার্চ করার জন্য endpoint (যেমন: /search?q=google)
@app.get("/search")
def search_websites(q: str = Query(..., description="Search query for website name")):
    df = load_data()
    if df is None:
        return {"error": "CSV File not found!"}
    
    # সার্চ কুয়েরির সাথে মেলানো (Case-insensitive)
    query = q.lower().strip()
    filtered_df = df[df['Website Name'].str.lower().str.contains(query, na=False)]
    
    results = filtered_df.to_dict(orient="records")
    return {
        "query": q,
        "count": len(results),
        "results": results
    }