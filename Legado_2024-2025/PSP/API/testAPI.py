import fastapi
import uvicorn

app = fastapi.FastAPI()

@app.get("/localidad")
def getLocalidad():
    return {"Localidad":"madrid"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=1000)