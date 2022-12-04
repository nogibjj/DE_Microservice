""" import neccessary libs"""
from fastapi import FastAPI
import uvicorn
from mylib import user_request


api = FastAPI()


@api.get("/")
async def root():
    """Root page"""
    return {"message": "Hello, this is an api to query info about World Cup!"}


@api.get("/query/")
def preprocess(request: user_request.QueryRequest):
    """Do preprocessing"""
    sql = request.query
    print(sql)


if __name__ == "__main__":
    uvicorn.run(api, port=8080, host="0.0.0.0")

