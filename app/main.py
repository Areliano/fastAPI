from fastapi import FastAPI
from app.routes import items


app = FastAPI(title="Fatma Hussein's Application")


# Include API router
app.include_router(items.router)


#root path
@app.get("/")
async def read_root():
    return {"message": "Welcome to My FastAPI Application! We are learning today"}