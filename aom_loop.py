import random

secret_number = random.randint(1-100)
count = 0

print("ยินดีต้อนรับ ใส่เลข 1-100")

while True:
    guess = int(input("ทายเลข: "))
    count = count + 1

    if guess < number:
        print("ต่ำเกินไป")
    elif guess > number:
        print("สูงเกินไป") 
    elif:
        print("ยินดีด้วยคุณตอบถูกแล้ว") 
        print("คำตอบที่ถูกต้อง คือ , count")      
        break