from fastapi import FastAPI
import asyncio
 
app = FastAPI()

@app.get("/")
sync def hello_world():
    return {"message": "hello world!!!"}
    
# if __name__ == '__main__':
#     asyncio.run(hello_world)  
# asyncio error was there becuase fastapi is supported by python 3.7+
