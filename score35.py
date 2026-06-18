point1 = int(input("enter your score"))
point2 = int(input("enter your score"))
point3 = int(input("enter your score"))

totlo_point = point1 + point2 + point3
average = totle_point/3
if average < 60:
    print ("คะแนนรวมของคุณ   =  ", totle_point)
    print ("คะแนนเฉลี่ย 3 วิชา = ", average)
    print("ควรปรับปรุง")
 elif average < 80:
    print("ผ่าน")
 else:
      print("ดีเยี่ยม") 