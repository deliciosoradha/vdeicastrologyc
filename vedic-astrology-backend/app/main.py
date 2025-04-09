from app import app
from fastapi.middleware.cors import CORSMiddleware
from app.database import init_db

# Initialize database
init_db()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all route modules
from app.routes import form, astrology, pdf, chat

# Register routes
app.include_router(form.router)
app.include_router(astrology.router)
app.include_router(pdf.router)
app.include_router(chat.router)

# TODO: Add payment routes when implemented

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
