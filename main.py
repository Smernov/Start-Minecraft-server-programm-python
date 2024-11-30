import tkinter as tk
from tkinter import scrolledtext
import subprocess
import threading

# Функция для запуска сервера
def start_server():
    command = "java -Xmx1G -XX:MaxPermSize=256M -Dfile.encoding=UTF-8 -jar Magma-1.16.5-36.2.39-c1c5a946-server.jar nogui"  # Замените на вашу команду
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Чтение вывода сервера и отображение его в текстовом поле
    def read_output():
        while True:
            output = process.stdout.readline()
            if output == b'' and process.poll() is not None:
                break
            if output:
                log_output(output.decode('utf-8'))

    threading.Thread(target=read_output, daemon=True).start()

# Функция для вывода текста в поле
def log_output(message):
    text_area.insert(tk.END, message)
    text_area.yview(tk.END)  # Прокрутка вниз, чтобы показывать последний вывод

# Создание главного окна
root = tk.Tk()
root.title("Серверный интерфейс")

# Создание кнопки для запуска сервера
start_button = tk.Button(root, text="Запустить сервер", command=start_server, font=("Arial", 14))
start_button.pack(pady=10)

# Создание текстового поля для отображения логов
text_area = scrolledtext.ScrolledText(root, width=80, height=20, font=("Arial", 12))
text_area.pack(padx=10, pady=10)

# Запуск главного цикла приложения
root.mainloop()
