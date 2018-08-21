# -*- coding: UTF-8 -*-

sendTime = input('請輸入送件時間(小時)：')
processTime = input('請輸入處理時間(小時數)')
int(sendTime)
int(processTime)
hours = processTime//24
remainingHours = processTime%24
print (hours, '天，', remainingHours, '小時')
receiveTime = sendTime + remainingHours
print ('完成時間: ', receiveTime, '點')
