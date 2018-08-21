# -*- coding: UTF-8 -*-
#展示如何發生 ValueError
#輸入時故意輸入非數字或者都不輸入直接 Enter，可以看到 ValueError

sendTime = input("請輸入送件時間('小時')：")
processTime = input('請輸入處理時間(小時)：')
sendTime = int(sendTime)
processTime = int(processTime)
receiveTime = (sendTime + processTime) % 24
print(receiveTime)
