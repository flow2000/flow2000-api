import requests
import json
import time
import ddddocr
API='https://app.bilibili.com/x/v2/search/trending/ranking'
headers={
    'Access-Control-Allow-Origin':'*',
    'Access-Control-Allow-Headers':'Content-Type',
    'Access-Control-Allow-Methods':'*',
    'Content-Type':'application/json;charset=utf-8'
}
ocr = ddddocr.DdddOcr(show_ad=False)

def get_topic():
    try:
        dataList=[]
        data=requests.get(API,headers=headers)
        data=json.loads(data.text)
        data_json=data['data']['list']
        for i in range(0,len(data_json)):
            hot=''
            icon_url=icon_url=data_json[i].get('icon','')
            if icon_url!="":
                img_bytes=requests.get(icon_url).content
                hot = ocr.classification(img_bytes)
            dic = {
                'title': data_json[i].get('show_name',''),
                'keyword': data_json[i].get('keyword',''),
                'url': 'https://search.bilibili.com/all?keyword=' + data_json[i].get('keyword',''),
                'hot': hot
            }
            dataList.append(dic)
        return dataList
    except Exception as e:
        print(str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())),e)
        return None