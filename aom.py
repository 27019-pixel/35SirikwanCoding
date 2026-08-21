import tkinter as tk
from tkinter import messagebox

def calculate_budget():
    try:
        monthly_income = float(entry_income.get())
        if monthly_income <= 0:
            messagebox.showwarning("แจ้งเตือน", "กรุณากรอกจำนวนเงินที่มากกว่า 0")
            return
        
        needs = monthly_income * 0.50
        wants = monthly_income * 0.30
        savings = monthly_income * 0.20

        label_needs_val.config(text=f"{needs:,.2f} บาท")
        label_wants_val.config(text=f"{wants:,.2f} บาท")
        label_savings_val.config(text=f"{savings:,.2f} บาท")
        
    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกตัวเลขที่ถูกต้อง")

root = tk.Tk()
root.title("Budget Planner - จัดสรรเงินรายเดือน")
root.geometry("380x500")
root.configure(bg="#f0f3f6")
root.resizable(False, False)

# Header
tk.Label(root, text="📊 จัดสรรเงินรายเดือน", font=("Helvetica", 16, "bold"), bg="#f0f3f6", fg="#2c3e50").pack(pady=15)

# Input
frame_input = tk.Frame(root, bg="#f0f3f6")
frame_input.pack(pady=5)
tk.Label(frame_input, text="กรอกรายได้ต่อเดือน (บาท):", font=("Helvetica", 11), bg="#f0f3f6").pack(anchor="w")
entry_income = tk.Entry(frame_input, font=("Helvetica", 13), width=22, justify="center")
entry_income.pack(pady=5)
entry_income.focus()

# Button
btn_calc = tk.Button(root, text="คำนวณงบประมาณ", font=("Helvetica", 11, "bold"), bg="#3498db", fg="white", 
                     padx=15, pady=6, relief="flat", cursor="hand2", command=calculate_budget)
btn_calc.pack(pady=10)

# Results
frame_results = tk.Frame(root, bg="#f0f3f6")
frame_results.pack(pady=10, fill="x", padx=25)
# Needs
card1 = tk.Frame(frame_results, bg="#2e86de", padx=12, pady=8)
card1.pack(fill="x", pady=4)
tk.Label(card1, text="🏠 ค่าใช้จ่ายจำเป็น (Needs 50%)", font=("Helvetica", 10), bg="#2e86de", fg="white").pack(anchor="w")
label_needs_val = tk.Label(card1, text="0.00 บาท", font=("Helvetica", 14, "bold"), bg="#2e86de", fg="white")
label_needs_val.pack(anchor="e")

# Wants
card2 = tk.Frame(frame_results, bg="#ff9f43", padx=12, pady=8)
card2.pack(fill="x", pady=4)
tk.Label(card2, text="🛍️ ค่าใช้จ่ายส่วนตัว (Wants 30%)", font=("Helvetica", 10), bg="#ff9f43", fg="white").pack(anchor="w")
label_wants_val = tk.Label(card2, text="0.00 บาท", font=("Helvetica", 14, "bold"), bg="#ff9f43", fg="white")
label_wants_val.pack(anchor="e")

# Savings
card3 = tk.Frame(frame_results, bg="#10ac84", padx=12, pady=8)
card3.pack(fill="x", pady=4)
tk.Label(card3, text="💰 เงินออม / ลงทุน (Savings 20%)", font=("Helvetica", 10), bg="#10ac84", fg="white").pack(anchor="w")
label_savings_val = tk.Label(card3, text="0.00 บาท", font=("Helvetica", 14, "bold"), bg="#10ac84", fg="white")
label_savings_val.pack(anchor="e")

root.mainloop()