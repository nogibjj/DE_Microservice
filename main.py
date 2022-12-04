""" import neccessary libs"""
from fastapi import FastAPI
import uvicorn
from mylib import user_request
from mylib import tools


api = FastAPI()
db_handle = tools.db_setup()


@api.get("/")
async def root():
    """Root page"""
    return {"message": "Hello, this is an api to query info about World Cup!"}


@api.get("/query/getAuthor")
async def get_author(request: user_request.AuthorRequest):
    """Do Query"""
    likes = request.likes if request.likes else 0
    shares = request.shares if request.shares else 0
    comments = request.comments if request.comments else 0
    plays = request.plays if request.plays else 0
    sql = tools.get_author_query(likes, shares, comments, plays)
    query_result = db_handle.execute(sql)
    result_str = tools.query_to_str(query_result)
    return tools.gen_response(sql, result_str)


@api.get("/query/getTrendingVideo")
async def get_trending_video(request: user_request.TrendingVideoRequest):
    """Do Query"""
    likes = request.likes if request.likes else 0
    shares = request.shares if request.shares else 0
    comments = request.comments if request.comments else 0
    plays = request.plays if request.plays else 0
    sql = tools.get_trending_video_query(likes, shares, comments, plays)
    query_result = db_handle.execute(sql)
    result_str = tools.query_to_str(query_result)
    return tools.gen_response(sql, result_str)


@api.get("/query/filterVideo")
async def get_video_filter(request: user_request.FilterVideoRequest):
    """Do Query"""
    description = request.desc if request.desc else ""
    sql = tools.get_video_filter(description)
    query_result = db_handle.execute(sql)
    result_str = tools.query_to_str(query_result)
    return tools.gen_response(sql, result_str)


if __name__ == "__main__":
    uvicorn.run(api, port=8080, host="0.0.0.0")
