from typing import Tuple
import requests
def teenstudy(cookie: str)->Tuple[bool, str]:
    '''
    创建一个函数，用于提交青少年学习平台的学习记录
    input: cookie
    output: (True, "已提交") or (True, "本周已完成") or (False, Exception)
    '''
    header={
        "Host":"api.lngqt.shechem.cn",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "http://websecond.lngqt.shechem.cn",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.26(0x18001a22) NetType/4G Language/zh_CN",
        "Connection": "keep-alive",
        "Content-Length": "6",
        "Referer": "http://websecond.lngqt.shechem.cn/",
        "Cookie": cookie
    }
    response = requests.post("http://api.lngqt.shechem.cn/webapi/learn/getnowlearn", headers=header, data={"token":""})
    try:
        video_id=response.json()["data"]["id"]
        if not response.json()["data"]["is_learn"]:
            header["Content-Length"]= "14"
            response2=requests.post("http://api.lngqt.shechem.cn/webapi/learn/addlearnlog", headers=header, data={"lid":str(video_id),"token":""})
            if response2.json()["msg"]=="计数成功":
                return (True, "已提交")
            else:
                return (False, Exception(response2))
        else:
            return (True, "本周已完成")
    except requests.exceptions.JSONDecodeError:
        return (False, Exception(response))

