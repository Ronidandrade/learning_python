from fastapi import FastAPI;

app = FastAPI();

@app.get("/")
async def root():
    return {"messenge": "Hello World!", "Name":"Ronivaldo D. Andrade"}
