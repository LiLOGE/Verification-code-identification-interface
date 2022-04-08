# Verification-code-identification-interface
一个简单易用的验证码识别接口，基于Python以及ddddocr。

# 部署
1. 安装python、web.py以及ddddocr。
2. 把main.py拷贝至服务器任意目录 。
3. 在该目录下执行命令`nohup python main.py 1111`，其中1111为端口号，可修改。 

# 使用
示例1
``` python
# -*- coding: utf-8 -*-
# filename: main.py

import requests

url = "https://ocr.qianlimu.tk"
file = {
    "img": ("img", open("test.png", "rb"))
}


def getCode():
    request = requests.post(url, files=file, verify=False)
    return request.text


if __name__ == '__main__':
    print(getCode())

```
