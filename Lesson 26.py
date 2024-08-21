




import requests
import json
import os
import tkinter as tk
from tkinter import messagebox

class JSONPlaceholderClient:
    def __init__(self, base_url="https://jsonplaceholder.typicode.com/posts/"):
        self.base_url = base_url

    def fetch_data(self, post_id):
        """Получение данных с сайта по заданному ID."""
        url = f"{self.base_url}{post_id}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None

    def save_data(self, post_id, data, folder="json_data"):
        """Сохранение данных в файл с указанием ID."""
        if data:
            os.makedirs(folder, exist_ok=True)
            file_path = os.path.join(folder, f"post_{post_id}.json")
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            return file_path
        return None


class JSONPlaceholderApp:
    def __init__(self, root):
        self.client = JSONPlaceholderClient()
        self.root = root
        self.root.title("JSONPlaceholder Fetcher")

        self.create_widgets()

    def create_widgets(self):
        """Создание виджетов интерфейса."""
        frame = tk.Frame(self.root)
        frame.pack(pady=20, padx=20)

        self.label_id = tk.Label(frame, text="Введите ID поста:")
        self.label_id.grid(row=0, column=0, padx=5, pady=5)

        self.entry_id = tk.Entry(frame)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)

        self.btn_fetch = tk.Button(frame, text="Получить данные", command=self.on_fetch_click)
        self.btn_fetch.grid(row=1, column=0, columnspan=2, pady=10)

    def on_fetch_click(self):
        """Обработка нажатия на кнопку для получения и сохранения данных."""
        post_id = self.entry_id.get()
        if post_id.isdigit():
            post_id = int(post_id)
            data = self.client.fetch_data(post_id)
            if data:
                file_path = self.client.save_data(post_id, data)
                if file_path:
                    messagebox.showinfo("Успех", f"Данные сохранены в {file_path}")
                else:
                    messagebox.showerror("Ошибка", "Не удалось сохранить данные.")
            else:
                messagebox.showerror("Ошибка", "Не удалось получить данные.")
        else:
            messagebox.showerror("Ошибка", "Введите корректный ID.")


if __name__ == "__main__":
    root = tk.Tk()
    app = JSONPlaceholderApp(root)
    root.mainloop()

















