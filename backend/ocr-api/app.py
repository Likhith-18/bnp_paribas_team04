from app.main import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="localhost", port=3000, reload=True)
