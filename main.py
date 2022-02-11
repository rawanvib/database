from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "hello world!!!"}
    
    
# renamed file from hello_world.py to main.py

