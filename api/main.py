# -*- coding:utf-8 -*-
# @Author: flow2000
import requests
import json
import random
import sys
import os
import time

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import asyncio
import aiohttp
from colorama import init
init(autoreset=True)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from bing_wallpaper_api import settings 
from bing_wallpaper_api.utils import util
from api.mongodbapi import *
from weibo_api import weibo_api
from sixty_api import sixty_api
from api import FlowResponse


app = FastAPI()

# 设置CORS
origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/",tags=["INFO"], summary="获取部署成功信息")
async def index():
    '''
    响应字段说明：
    - code:状态码
    - msg:部署信息
    - current_version:当前版本
    - latest_version:最新版本
    '''
    latest_version=""
    try:
        async with aiohttp.ClientSession() as session:
            version_links=[
                "https://blog.aqcoder.cn/code/txt/version/flow2000-api.txt",
                "https://static.aqcoder.cn/txt/version/flow2000-api.txt",
            ]
            tasks = [asyncio.create_task(fetch(session, link)) for link in version_links]
            done, pending = await asyncio.wait(tasks)
            for d in done:
                if len(d.result())<10:
                    latest_version = d.result()
                    break
            if latest_version=="":
                raise Exception("无法请求文件")
    except Exception as e:
        print(e)
        data={
            "current_version":settings.VERSION
        }
        return FlowResponse.error(msg="BingAPI 获取不到最新版本，但仍可使用，请联系：https://github.com/flow2000/flow2000-api",data=data)
    data={
        "current_version":settings.VERSION,
        "latest_version":latest_version
    }
    return FlowResponse.success(msg="Flow2000API 部署成功，查看接口文档：https://api.aqcoder.cn/docs",data=data)

async def fetch(session, url):
    async with session.get(url, verify_ssl=False) as response:
        return await response.text()

@app.get("/favicon.ico",tags=["INFO"], summary="获取图标")
async def favicon():
    '''
    - 获取图标
    '''
    return StreamingResponse(open('favicon.ico', mode="rb"), media_type="image/jpg")

@app.get("/today",tags=["壁纸API"], summary="获取今日壁纸")
async def latest(w: str = "1920", h: str = "1080", uhd: bool = False, mkt: str = "zh-CN"):
    '''
    请求字段说明：
    - w:图片宽度,默认1920
    - h:图片长度,默认1080
    - uhd:是否4k,默认False,为True时请求参数w和h无效。目前支持的分辨率:1920x1200, 1920x1080, 1366x768, 1280x768, 1024x768, 800x600, 800x480, 768x1280, 720x1280, 640x480, 480x800, 400x240, 320x240, 240x320
    - mkt:地区，默认zh-CN。目前支持的地区码：zh-CN, de-DE, en-CA, en-GB, en-IN, en-US, fr-FR, it-IT, ja-JP
    '''
    return latest_one(w,h,uhd,mkt)

@app.get("/random",tags=["壁纸API"], summary="获取随机壁纸")
async def random(w: str = "1920", h: str = "1080", uhd: bool = False, mkt: str = "zh-CN"):
    '''
    请求字段说明：
    - w:图片宽度,默认1920
    - h:图片长度,默认1080
    - uhd:是否4k,默认False,为True时请求参数w和h无效。目前支持的分辨率:1920x1200, 1920x1080, 1366x768, 1280x768, 1024x768, 800x600, 800x480, 768x1280, 720x1280, 640x480, 480x800, 400x240, 320x240, 240x320
    - mkt:地区，默认zh-CN。目前支持的地区码：zh-CN, de-DE, en-CA, en-GB, en-IN, en-US, fr-FR, it-IT, ja-JP
    '''
    return random_one(w,h,uhd,mkt)

@app.get("/all",tags=["壁纸API"], summary="获取分页数据")
async def all(page: int = 1, limit: int = 10, order: str="desc", w: int = 1920, h: int = 1080, uhd: bool = False, mkt: str = "zh-CN"):
    '''
    请求字段说明：
    - page:页码,默认1
    - limit:页数,默认10
    - w:图片宽度,默认1920
    - h:图片长度,默认1080
    - uhd:是否4k,默认False,为True时请求参数w和h无效。目前支持的分辨率:1920x1200, 1920x1080, 1366x768, 1280x768, 1024x768, 800x600, 800x480, 768x1280, 720x1280, 640x480, 480x800, 400x240, 320x240, 240x320
    - mkt:地区，默认zh-CN。目前支持的地区码：zh-CN, de-DE, en-CA, en-GB, en-IN, en-US, fr-FR, it-IT, ja-JP
    '''
    if util.check_params(page,limit,order,w,h,uhd,mkt)==False:
        return FlowResponse.error('请求参数错误')
    return query_all(page,limit,order,w,h,uhd,mkt)

@app.get("/total",tags=["壁纸API"], summary="获取数据总数")
async def total(mkt: str = "zh-CN"):
    '''
    请求字段说明：
    - mkt:地区，默认zh-CN。目前支持的地区码：zh-CN, de-DE, en-CA, en-GB, en-IN, en-US, fr-FR, it-IT, ja-JP
    '''
    if settings.LOCATION.count(mkt)==0:
        return FlowResponse.error('请求参数错误')
    return query_total_num(mkt)

@app.get("/weibo",tags=["微博热搜API"], summary="获取热搜json数据")
async def weibo():
    '''
    微博热搜API
    '''
    res=weibo_api.get_topic()
    if res!=None:
        return FlowResponse.success(data=res)
    else:
        return FlowResponse.error('系统发生错误')


@app.get("/60s",tags=["60秒新闻API"], summary="获取今日新闻json数据")
async def sixty(offset: int = 0):
    '''
    请求字段说明：
    - offset:偏移量（可选参数：0,1,2,3），默认0表示今天，1表示昨天，2表示前天，3表示大前天。
    '''
    res=sixty_api.get_topic(offset)
    if res!=None:
        return FlowResponse.success(data=res)
    else:
        return FlowResponse.error('系统发生错误')

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8888)
