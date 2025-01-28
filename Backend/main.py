from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def hi_message():
    return "<<<HI STUDENT>>>"

if __name__ == "__main__":
    uvicorn.run(app)