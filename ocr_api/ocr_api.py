import ddddocr
import requests
import time
from api import FlowResponse
from fastapi import HTTPException

ocr = ddddocr.DdddOcr(show_ad=False)

def ocr_image_bytes(img_bytes):
    return ocr.classification(img_bytes)

def get_max_image_size():
    return 512*1024
