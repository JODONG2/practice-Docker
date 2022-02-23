from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/") 
def print_hello()->None:
    message = "Hello Docker!!"
    return message

@app.get("/hello")
def print_hello_world()->None:
    message = "Hello world. i'm docker ;)"
    return message

if __name__=="__main__":
    uvicorn.run("app:app", host="0.0.0.0", port = 8080, reload = True)
