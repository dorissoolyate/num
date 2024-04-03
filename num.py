import tkinter as tk
from tkinter import Toplevel, messagebox
from datetime import datetime
import nummodule
import email
import smtplib,ssl
from email.message import EmailMessage
from tkinter import filedialog
from tkinter import messagebox, filedialog
from http import server
results = ""
def calculate_numerological_numbers(day, month, year):
    # Helper function to reduce a number to a single digit
    def reduce_to_single_digit(number):
        while len(str(number)) > 1 and number not in [11, 22]:
            number = sum(map(int, str(number)))
        return number
    
    # Calculating the Life Path Number (First Working Number)
    life_path_number = reduce_to_single_digit(day + month + year)
    
    # Placeholder for Expression Number using birth year (Second Working Number)
    expression_number = reduce_to_single_digit(year)
    
    # Placeholder for Soul Urge Number using birth month (Third Working Number)
    soul_urge_number = reduce_to_single_digit(month)
    
    # Placeholder for Personality Number using birth day (Fourth Working Number)
    personality_number = reduce_to_single_digit(day)
    
    return life_path_number, expression_number, soul_urge_number, personality_number

# Example usage:
print(calculate_numerological_numbers(15, 7, 1990))

def calculate_and_show():
    global results
    date_str = entry_date.get()
    try:
        birth_date = datetime.strptime(date_str, "%d.%m.%Y")
        day, month, year = birth_date.day, birth_date.month, birth_date.year
        first, second, third, fourth = calculate_numerological_numbers(day, month, year)
        
        results = f"1-е рабочее число: {first}\n2-е рабочее число: {second}\n"\
                  f"3-е рабочее число: {third}\n4-е рабочее число: {fourth}"
                  
        messagebox.showinfo("Результаты", results)
    except ValueError:
        messagebox.showerror("Ошибка", "Некорректный формат даты. Используйте ДД.ММ.ГГГГ")

def open_email_window():
    global results
    if not results:
        messagebox.showerror("Ошибка", "Сначала рассчитайте результаты.")
        return

    email_window =Toplevel
    email_window.title("Отправить результаты на почту")
    email_window.geometry("300x200")
    email_window.configure(bg='light blue')

    tk.Label(email_window, text="Введите адрес электронной почты:", bg='light blue', fg='dark blue').pack(pady=10)
    email_entry = tk.Entry(email_window)
    email_entry.pack(pady=10)

    send_button = tk.Button(email_window, text="Отправить", command=lambda: saada_k(email_entry.get()), bg='dark blue', fg='white')
    send_button.pack(pady=20)

def open_email_window():
    if not results:
        messagebox.showerror("Ошибка", "Сначала рассчитайте результаты.")
        return
    
    def send_email():
        email = email_entry.get()
        saada_k(email, results)
        email_window.destroy()
    
    email_window = tk.Toplevel(root)
    email_window.title("Отправить результаты на почту")
    email_window.geometry("300x200")
    email_window.configure(bg='light blue')
    
    tk.Label(email_window, text="Введите адрес электронной почты:", bg='light blue', fg='dark blue').pack(pady=10)
    email_entry = tk.Entry(email_window)
    email_entry.pack(pady=10)
    
    send_button = tk.Button(email_window, text="Отправить", command=send_email, bg='dark blue', fg='white')
    send_button.pack(pady=20)

def saada_k(receiver_email, message_content):
    smtp_server = "smtp.gmail.com"
    port = 587 
    sender_email = "maasikmetssatoru@gmail.com"
    password = "lfvv xozu njuf bmjw" 

    msg = EmailMessage()
    msg["Subject"] = "Результаты расчёта"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content(message_content)
    
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.send_message(msg)
            messagebox.showinfo("Успех", "Результаты успешно отправлены.")
    except Exception as e:
        messagebox.showerror("Ошибка отправки", str(e))
    
def calculate_and_show():
    global results
    date_str = entry_date.get()
    try:
        birth_date = datetime.strptime(date_str, "%d.%m.%Y")
        day, month, year = birth_date.day, birth_date.month, birth_date.year
        numbers = calculate_numerological_numbers(day, month, year)  
        analysis = nummodule.analyze_numbers(numbers)
        results = f"1-е рабочее число: {numbers[0]}\n2-е рабочее число: {numbers[1]}\n"\
                  f"3-е рабочее число: {numbers[2]}\n4-е рабочее число: {numbers[3]}\n\nАнализ:\n{analysis}"   
        messagebox.showinfo("Результаты", results)
    except ValueError:
        messagebox.showerror("Ошибка", "Некорректный формат даты. Используйте ДД.ММ.ГГГГ")
        


root = tk.Tk()
root.title("Расчет по методу Пифагора")
root.geometry("300x600")
root.configure(bg='light blue')

tk.Label(root, text="Введите дату рождения (ДД.ММ.ГГГГ):", bg='light blue', fg='dark blue').pack(pady=(20, 0))
entry_date = tk.Entry(root)
entry_date.pack(pady=(0, 20))

calculate_button = tk.Button(root, text="Рассчитать", command=calculate_and_show, bg='dark blue', fg='white')
calculate_button.pack(pady=(20, 20))

email_button = tk.Button(root, text="Отправить результат", command=open_email_window, bg='dark blue', fg='white')
email_button.pack(pady=(0, 20))

root.mainloop()
