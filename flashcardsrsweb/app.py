from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from flashcardsrsweb.cards.router import router as cards_router
from flashcardsrsweb.db.setup import setup_database

setup_result = setup_database()
print(f'Database initialization: {setup_result}')
# Create FastAPI app
app = FastAPI(
    title="FlashCards SRS Web",
    description="High customizability and low friction system to memorize anything!",
    version="0.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development - restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(cards_router)

# Optional root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to FlashCards SRS Web API"}
