from fastapi import FastAPI
import asyncio
 
app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "hello world!!!"}
    
if __name__ == '__main__':
    asyncio.run(hello_world)    
