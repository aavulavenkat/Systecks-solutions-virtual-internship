import tkinter as tk
from fpdf import FPDF

def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    pdf.cell(200, 10, txt = "Student Registration Form", ln = True, align = 'C')
    pdf.cell(200, 10, txt = "Name: " + name.get() + "\n", ln = True)
    pdf.cell(200, 10, txt = "AICTE ID: " + aicteid.get() + "\n", ln = True)
    pdf.cell(200, 10, txt = "Email: " + email.get() + "\n", ln = True)
    pdf.cell(200, 10, txt = "Phone Number: " + phone_number.get() + "\n", ln = True)
    pdf.cell(200, 10, txt = "College Name: " + college_name.get() + "\n", ln = True)
    pdf.output("Student_Details.pdf")
    status.set("PDF has been generated successfully!")

root = tk.Tk()
root.geometry("400x400")

name = tk.StringVar()
aicteid = tk.StringVar()
email = tk.StringVar()
phone_number = tk.StringVar()
college_name = tk.StringVar()
status = tk.StringVar()

tk.Label(root, text = "Name:").pack()
tk.Entry(root, textvariable = name).pack()

tk.Label(root, text = "AICTE ID:").pack()
tk.Entry(root, textvariable = aicteid).pack()

tk.Label(root, text = "Email:").pack()
tk.Entry(root, textvariable = email).pack()

tk.Label(root, text = "Phone Number:").pack()
tk.Entry(root, textvariable = phone_number).pack()

tk.Label(root, text = "College Name:").pack()
tk.Entry(root, textvariable = college_name).pack()

tk.Button(root, text = "Submit", command = generate_pdf).pack()

tk.Label(root, textvariable = status).pack()

root.mainloop()