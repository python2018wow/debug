# -*- coding: UTF-8 -*-

sendTime = input('請輸入送件時間(小時)：')
processTime = input('請輸入處理時間(小時)：'
sendTime = int(sendTime)
processTime = int(processTime)
receiveTime = (sendTime + processTime) % 24
print(receiveTime)