import fastapi
import uvicorn

app = fastapi.FastAPI()

@app.get("/localidad")
def getLocalidad():
    return {"Localidad":"madrid"}

if __name__ == "__main__":
    uvicorn.run(app, host="2.138.207.76", port=1000)