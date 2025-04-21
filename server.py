from fastapi import FastAPI, Request
from chat import get_response
from fastapi.middleware.cors import CORSMiddleware
app =FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","http://mentiq.xyz","http://app.mentiq.xyz"],  # your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post('/')
async def main(req: Request):
    data = await req.json()
    user_input = data.get("client_input", "")
    res = get_response(user_input)
    print(res)
    return {"response": res}