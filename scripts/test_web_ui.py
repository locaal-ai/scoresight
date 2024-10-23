# server.py
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import uvicorn
from pathlib import Path
import json
from typing import Optional, Dict, Any

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your actual domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (your React build)
static_files_path = Path(__file__).parent / "frontend" / "dist"
app.mount("/static", StaticFiles(directory=static_files_path), name="static")

# API Routes
@app.get("/api/sources")
async def get_sources():
    # Example function to list available video sources
    return {
        "sources": [
            {"id": "webcam", "name": "Webcam"},
            {"id": "screen", "name": "Screen Capture"},
            # Add more sources as needed
        ]
    }

@app.post("/api/settings")
async def update_settings(settings: Dict[str, Any]):
    # Handle settings updates
    try:
        # Update your application settings here
        return {"status": "success", "message": "Settings updated"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Serve index.html for all other routes to support client-side routing
@app.get("/{full_path:path}")
async def serve_app(full_path: str):
    index_path = static_files_path / full_path
    if not index_path.exists():
        raise HTTPException(status_code=404, detail="Application not built")
    return FileResponse(index_path)

def start_server(host: str = "localhost", port: int = 8000):
    """Start the FastAPI server"""
    uvicorn.run(app, host=host, port=port)

if __name__ == "__main__":
    start_server()