# -*- coding: utf-8 -*-
# filename: main.py

import web
import ddddocr

ocr = ddddocr.DdddOcr()

urls = (
    '/', 'Handle',
)

class Handle(object):
    
    def getCode(self,img):
        code = ocr.classification(img)
        return code
        
    def POST(self):
        date = web.input(img = {})
        img = date['img'].file.read()
        return self.getCode(img)
        
if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
