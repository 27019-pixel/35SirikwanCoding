print("โปรแกรมคำนวณคะแนน")

eng= int(input("คะแนนรวมวิชาอังกฤษ"))
math = int(input("คะแนนรวมวิชาคณิตศาสตร์"))
science = int(input("คะแนนรวมวิชาวิทยาศาสตร์"))
totle_print = eng + math + science
average = totle_print / 3 
if average <60:
    print("ดีเยี่ยม")
elif average <80:
    print("ดีมาก")    
elif average <40:
    print("ผ่าน")    
print(" by aom 4/4")
print(" thank you")