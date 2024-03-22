from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import customtkinter
import customtkinter as CTk
from PIL import Image
import password
import tkinter as tk


class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("460x400")  # Увеличил высоту для новой кнопки
        self.title("Генератор паролей от 100kwt")
        self.resizable(False, False)

        self.logo = CTk.CTkImage(dark_image=Image.open("img.png"), size=(460, 150))
        self.logo_label = CTk.CTkLabel(master=self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0)

        self.password_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.password_frame.grid(row=1, column=0, padx=(20, 20), sticky="nsew")

        self.entry_password = CTk.CTkEntry(master=self.password_frame, width=300)
        self.entry_password.grid(row=0, column=0, padx=(0, 20))

        self.btn_generate = CTk.CTkButton(
            master=self.password_frame,
            text="Сгенерировать",
            width=100,
            command=self.set_password,
        )
        self.btn_generate.grid(row=0, column=1)

        # Добавляем кнопку "Copy"
        self.btn_copy = CTk.CTkButton(
            master=self.password_frame,
            text="Копировать",
            width=100,
            command=self.copy_password,
        )
        self.btn_copy.grid(row=0, column=2)

        self.settings_frame = CTk.CTkFrame(master=self)
        self.settings_frame.grid(
            row=2, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew"
        )

        self.password_length_slider = CTk.CTkSlider(
            master=self.settings_frame,
            from_=0,
            to=100,
            number_of_steps=100,
            command=self.slider_event,
        )

        self.password_length_slider.grid(
            row=1, column=0, columnspan=3, pady=(20, 20), sticky="ew"
        )

        self.password_length_entry = CTk.CTkEntry(master=self.settings_frame, width=50)
        self.password_length_entry.grid(row=1, column=3, padx=(20, 10), sticky="we")

        self.cb_digits_var = CTk.StringVar()
        self.cb_digits = CTk.CTkCheckBox(
            master=self.settings_frame,
            text="0-9",
            variable=self.cb_digits_var,
            onvalue=digits,
            offvalue="",
        )
        self.cb_digits.grid(row=2, column=0, padx=10)

        self.cb_lower_var = CTk.StringVar()
        self.cb_lower = CTk.CTkCheckBox(
            master=self.settings_frame,
            text="a-z",
            variable=self.cb_lower_var,
            onvalue=ascii_lowercase,
            offvalue="",
        )
        self.cb_lower.grid(row=2, column=1)

        self.cb_upper_var = CTk.StringVar()
        self.cb_upper = CTk.CTkCheckBox(
            master=self.settings_frame,
            text="A-Z",
            variable=self.cb_upper_var,
            onvalue=ascii_uppercase,
            offvalue="",
        )
        self.cb_upper.grid(row=2, column=2)

        self.cb_symbol_var = CTk.StringVar()
        self.cb_symbol = CTk.CTkCheckBox(
            master=self.settings_frame,
            text="@#$%",
            variable=self.cb_symbol_var,
            onvalue=punctuation,
            offvalue="",
        )
        self.cb_symbol.grid(row=2, column=3)

        self.appearance_mode_option_menu = CTk.CTkOptionMenu(
            master=self.settings_frame,
            values=["Светлый", "Тёмный", "Системный"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_option_menu.grid(
            row=3, column=0, columnspan=4, pady=(10, 10)
        )

        self.password_length_slider.set(12)
        self.password_length_entry.insert(0, 12)

    def change_appearance_mode_event(self, new_appearance_mode):
        CTk.set_appearance_mode(new_appearance_mode)

    def slider_event(self, value):
        self.password_length_entry.delete(0, "end")
        self.password_length_entry.insert(0, int(value))

    def get_characters(self):
        chars = "".join(
            self.cb_digits_var.get()
            + self.cb_lower_var.get()
            + self.cb_upper_var.get()
            + self.cb_symbol_var.get()
        )
        return chars

    def set_password(self):
        self.entry_password.delete(0, "end")
        generated_password = password.create_new(
            length=int(self.password_length_slider.get()),
            characters=self.get_characters(),
        )
        self.entry_password.insert(0, generated_password)

    def copy_password(self):
        generated_password = self.entry_password.get()
        self.clipboard_clear()
        self.clipboard_append(generated_password)


if __name__=="__main__":
    app = App()
    app.mainloop()
