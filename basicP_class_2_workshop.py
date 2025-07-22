R = int(input("ใส่ระทางมา : "))
if R < 5 :
    print("ฟรีค่าส่ง")
elif R < 51 :
    print("ค่าส่งราคา 10 บาท")
elif R < 101 :
    print("ค่าส่งราคา 15 บาท")
elif R < 301 :
    print("ค่าส่งราคา 25 บาท")
elif R < 500:
    print("ค่าส่งราคา 35 บาท")
else :
    print("ค่าส่งราคา 45 บาท")