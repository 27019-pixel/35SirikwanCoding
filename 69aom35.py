print ("โปรแกรมจำนวนค่าไฟ 1 เดือน")
def calculate_electricity_bill(units):
    if units <= 9:
        bill = 0
    elif units <= 50:
        bill = (units - 9) * 2
    elif units <= 100:
        bill = 82 + ((units - 50) * 3)
    else:
        bill = 232 + ((units - 100) * 4) 
        
    return bill

user_input = int(input("กรอกจำนวนหน่วย: "))

total_bill = calculate_electricity_bill(user_input)
print("จำนวนไฟฟ้าที่ใช้:", user_input)
print("ค่าไฟฟ้าที่ต้องจ่าย:", total_bill)
print("br aom 4/4") 
print(" thank you")   
