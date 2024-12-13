import tkinter as tk
from tkinter import ttk, messagebox


class BaseConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Обучающая программа: Перевод чисел между системами счисления")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        # Создаем фон
        self.create_gradient_background()

        # Основной контейнер
        self.main_frame = tk.Frame(self.root, bg="#ffffff", bd=2, relief="groove")
        self.main_frame.place(relwidth=0.9, relheight=0.75, relx=0.05, rely=0.05)

        # Описание программы
        self.create_description()

        # Поля ввода
        self.create_input_fields()

        # Результат
        self.create_result_display()

        # Кнопки действий
        self.create_buttons()

    def create_gradient_background(self):
        """Создаем градиентный фон окна."""
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)

        # Градиент от светло-голубого к белому
        for i in range(600):
            color = f"#{hex(240 - i // 10)[2:]:0>2}{hex(250 - i // 20)[2:]:0>2}{hex(255)[2:]:0>2}"
            self.canvas.create_line(0, i, 800, i, fill=color)

    def create_description(self):
        """Описание программы в верхней части интерфейса."""
        description_frame = tk.Frame(self.main_frame, bg="#eaf4fc", relief="groove", bd=2, padx=10, pady=10)
        description_frame.pack(fill="x", pady=10)

        description_text = (
            "Добро пожаловать в обучающую программу по переводу чисел между системами счисления!\n"
            "Вы можете перевести число из одной системы счисления (2-36) в другую. "
            "Программа помогает понять основы систем счисления."
        )
        description_label = tk.Label(
            description_frame, text=description_text, font=("Arial", 12), bg="#eaf4fc", wraplength=750, justify="left"
        )
        description_label.pack()

    def create_input_fields(self):
        """Поля для ввода данных."""
        input_frame = tk.Frame(self.main_frame, bg="#ffffff", padx=20, pady=10)
        input_frame.pack(fill="x", pady=10)

        # Поле ввода числа
        tk.Label(input_frame, text="Введите число:", font=("Arial", 12), bg="#ffffff").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_number = ttk.Entry(input_frame, font=("Arial", 12))
        self.entry_number.grid(row=0, column=1, padx=5, pady=5)

        # Выбор исходной системы счисления
        tk.Label(input_frame, text="Исходная система:", font=("Arial", 12), bg="#ffffff").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.source_base = ttk.Combobox(input_frame, values=list(range(2, 37)), font=("Arial", 12), state="readonly")
        self.source_base.grid(row=1, column=1, padx=5, pady=5)
        self.source_base.set(10)

        # Выбор целевой системы счисления
        tk.Label(input_frame, text="Целевая система:", font=("Arial", 12), bg="#ffffff").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.target_base = ttk.Combobox(input_frame, values=list(range(2, 37)), font=("Arial", 12), state="readonly")
        self.target_base.grid(row=2, column=1, padx=5, pady=5)
        self.target_base.set(2)

    def create_result_display(self):
        """Отображение результата перевода."""
        result_frame = tk.Frame(self.main_frame, bg="#f8f9fa", relief="groove", bd=2, padx=10, pady=10)
        result_frame.pack(fill="x", pady=10)

        self.result_label = tk.Label(
            result_frame, text="Результат перевода: ", font=("Arial", 16, "bold"), bg="#f8f9fa", fg="#333333"
        )
        self.result_label.pack()

    def create_buttons(self):
        """Кнопки внизу окна."""
        button_frame = tk.Frame(self.root, bg="#e0e4e8")
        button_frame.place(relwidth=1, y=520)

        # Кнопка перевода
        convert_button = tk.Button(
            button_frame, text="Перевести", font=("Arial", 14), bg="#4CAF50", fg="white", relief="raised", command=self.convert_number
        )
        convert_button.pack(side="left", padx=20, pady=10)

        # Кнопка очистки
        clear_button = tk.Button(
            button_frame, text="Очистить", font=("Arial", 14), bg="#2196F3", fg="white", relief="raised", command=self.clear_fields
        )
        clear_button.pack(side="left", padx=20, pady=10)

        # Кнопка выхода
        exit_button = tk.Button(
            button_frame, text="Выход", font=("Arial", 14), bg="#f44336", fg="white", relief="raised", command=self.root.quit
        )
        exit_button.pack(side="right", padx=20, pady=10)

    def convert_number(self):
        """Перевод числа между системами счисления."""
        try:
            input_number = self.entry_number.get().strip()
            source_base = int(self.source_base.get())
            target_base = int(self.target_base.get())

            if not input_number:
                raise ValueError("Введите число для перевода.")

            # Перевод из исходной системы в десятичную
            decimal_number = int(input_number, source_base)

            # Перевод из десятичной в целевую систему
            converted_number = self.decimal_to_base(decimal_number, target_base)

            # Обновление результата
            self.result_label.config(text=f"Результат перевода: {converted_number}", fg="#4CAF50")
        except ValueError as e:
            messagebox.showerror("Ошибка", f"Неверный ввод: {e}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Что-то пошло не так: {e}")

    def decimal_to_base(self, decimal_number, base):
        """Перевод числа из десятичной в указанную систему счисления."""
        if decimal_number == 0:
            return "0"
        digits = []
        while decimal_number:
            remainder = decimal_number % base
            if remainder >= 10:
                digits.append(chr(55 + remainder))
            else:
                digits.append(str(remainder))
            decimal_number //= base
        return ''.join(reversed(digits))

    def clear_fields(self):
        """Очистка всех полей ввода и результата."""
        self.entry_number.delete(0, tk.END)
        self.source_base.set(10)
        self.target_base.set(2)
        self.result_label.config(text="Результат перевода: ", fg="#333333")


if __name__ == "__main__":
    root = tk.Tk()
    app = BaseConverterApp(root)
    root.mainloop()
