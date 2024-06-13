import tkinter as tk
from tkinter import ttk

import tkinter as tk
from tkinter import ttk
import psycopg2

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Работа с заказами клиентов")

        # Connect to PostgreSQL database
        self.conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="123"
        )
        self.cur = self.conn.cursor()

        # Retrieve list of clients from database
        self.cur.execute("SELECT username FROM usersall")
        self.clients = [row[0] for row in self.cur.fetchall()]

        # Create GUI components
        self.top_frame = tk.Frame(self)
        self.top_frame.pack(pady=10)

        # Dropdown menu for selecting a client
        self.client_label = tk.Label(self.top_frame, text="Выберите клиента:")
        self.client_label.pack(side=tk.LEFT)
        self.client_dropdown = ttk.Combobox(self.top_frame, values=self.clients)
        self.client_dropdown.pack(side=tk.LEFT, padx=10)



        # Выбор клиента
        self.client_label = tk.Label(self.top_frame, text="Выберите клиента:")
        self.client_label.pack(side=tk.LEFT)
        self.client_dropdown = ttk.Combobox(self.top_frame)
        self.client_dropdown.pack(side=tk.LEFT, padx=10)

        # Поиск
        self.search_label = tk.Label(self.top_frame, text="Введите строку поиска:")
        self.search_label.pack(side=tk.LEFT)
        self.search_entry = tk.Entry(self.top_frame)
        self.search_entry.pack(side=tk.LEFT, padx=10)
        self.search_button = tk.Button(self.top_frame, text="Найти")
        self.search_button.pack(side=tk.LEFT)

        # Фильтрация
        self.filter_button = tk.Button(self.top_frame, text="Фильтровать")
        self.filter_button.pack(side=tk.LEFT, padx=10)
        self.show_all_button = tk.Button(self.top_frame, text="Показать все")
        self.show_all_button.pack(side=tk.LEFT)

        # Сортировка
        self.sort_label = tk.Label(self.top_frame, text="Выберите поле для сортировки:")
        self.sort_label.pack(side=tk.RIGHT)
        self.sort_dropdown = ttk.Combobox(self.top_frame, values=["Клиент", "Дата заказа", "Вид оплаты"])
        self.sort_dropdown.pack(side=tk.RIGHT, padx=10)
        self.ascending_radio = tk.Radiobutton(self.top_frame, text="По возрастанию")
        self.ascending_radio.pack(side=tk.RIGHT)
        self.descending_radio = tk.Radiobutton(self.top_frame, text="По убыванию")
        self.descending_radio.pack(side=tk.RIGHT)

        # Таблица
        self.table_frame = tk.Frame(self)
        self.table_frame.pack(pady=10)

        # Заголовки таблицы
        self.client_header = tk.Label(self.table_frame, text="Клиент", width=15, relief=tk.RIDGE)
        self.client_header.grid(row=0, column=0, sticky="nsew")
        self.phone_header = tk.Label(self.table_frame, text="Телефон", width=15, relief=tk.RIDGE)
        self.phone_header.grid(row=0, column=1, sticky="nsew")
        self.email_header = tk.Label(self.table_frame, text="Электронная почта", width=25, relief=tk.RIDGE)
        self.email_header.grid(row=0, column=2, sticky="nsew")
        self.date_header = tk.Label(self.table_frame, text="Дата заказа", width=15, relief=tk.RIDGE)
        self.date_header.grid(row=0, column=3, sticky="nsew")
        self.payment_header = tk.Label(self.table_frame, text="Вид оплаты", width=15, relief=tk.RIDGE)
        self.payment_header.grid(row=0, column=4, sticky="nsew")

        # Кнопка "Добавить"
        self.add_button = tk.Button(self, text="Добавить", command=self.add_client)
        self.add_button.pack(pady=10)

    def add_client(self):
        # Создаем новое окно для добавления клиента
        new_client_window = tk.Toplevel(self)
        new_client_window.title("Добавить клиента")

        # Поля для ввода данных клиента
        client_name_label = tk.Label(new_client_window, text="Имя клиента:")
        client_name_label.pack()
        client_name_entry = tk.Entry(new_client_window)
        client_name_entry.pack()

        phone_label = tk.Label(new_client_window, text="Телефон:")
        phone_label.pack()
        phone_entry = tk.Entry(new_client_window)
        phone_entry.pack()

        email_label = tk.Label(new_client_window, text="Электронная почта:")
        email_label.pack()
        email_entry = tk.Entry(new_client_window)
        email_entry.pack()

        # Кнопка "Добавить"
        add_client_button = tk.Button(new_client_window, text="Добавить", command=lambda: self.save_client(new_client_window, client_name_entry.get(), phone_entry.get(), email_entry.get()))
        add_client_button.pack(pady=10)

    def save_client(self, new_client_window, name, phone, email):
        # Добавляем нового клиента в список данных
        # (здесь будет код для добавления данных в список)

        # Обновляем таблицу
        # (здесь будет код для обновления таблицы)

        # Закрываем окно добавления клиента
        new_client_window.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()