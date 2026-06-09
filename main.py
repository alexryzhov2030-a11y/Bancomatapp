import tkinter as tk
from styles import AppStyles
from dialogs import Dialogs
from storage import Storage
from tkinter import messagebox

class ATMAPP:
    def __init__(self, root):
        self.root = root
        self.root.title("Bankomat")
        self.root.configure(bg=AppStyles.COLORS['bg'])
        self.root.geometry("700x700")
        self.root.resizable(False, False)
        self.storage = Storage()
        self.balance = self.storage.load_balance()
        self.create_widgets()
        self.dialogs = Dialogs(self.root, self.storage, self.upedate_balance, self.upedate_status)

    def create_widgets(self):
        Title_label = tk.Label(
            text="💵 ДОБРО ПОЖАЛОВАТЬ В БАНКОМАТ 💵",
            font=AppStyles.get_font('title'),
            bg=AppStyles.COLORS['bg'],
            fg=AppStyles.COLORS['fg']
        )
        Title_label.pack(pady=20)

        Money_frame = tk.Frame(
            bg=AppStyles.COLORS['balance_bg'],
            relief=tk.RAISED,
            bd=2
        )
        self.Money_label = tk.Label(
            Money_frame,
            text="💰 ТЕКУЩИЙ БАЛАНС 💰",
            font=AppStyles.get_font('label'),
            bg=AppStyles.COLORS['balance_bg'],
            fg=AppStyles.COLORS['fg']
        )
        self.Money_balance_label = tk.Label(
            Money_frame,
            text=f"{self.balance:,.2f} руб.",
            font=AppStyles.get_font('title'),
            bg=AppStyles.COLORS['balance_bg'],
            fg=AppStyles.COLORS['balance_text']
        )
        Money_frame.pack(pady=(0, 20), padx=(10, 10), fill=tk.X)
        self.Money_label.pack(pady=5)
        self.Money_balance_label.pack(pady=10)

        buttons_frame = tk.Frame(bg=AppStyles.COLORS['bg'])
        buttons_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        buttons = [
            ("💵 ПОПОЛНИТЬ", AppStyles.COLORS['deposit'], self.diposit),
            ("💸 СНЯТЬ", AppStyles.COLORS['withdraw'], self.withdraw),
            ("📜 ИСТОРИЯ ОПЕРАЦИЙ", AppStyles.COLORS['history'], self.history),
            ("🔄 СБРОСИТЬ БАЛАНС", AppStyles.COLORS['reset'], self.reset),
            ("🚪 ВЫХОД", AppStyles.COLORS['exit'], self.exit)
        ]

        for text, color, comand in buttons:
            btn = tk.Button(
                buttons_frame,
                text=text,
                font=AppStyles.get_font('button'),
                bg=color,
                command=comand,
                fg=AppStyles.COLORS['fg'],
                relief=tk.RAISED,
                bd=2,
                cursor="hand2",
                height=2
            )
            btn.pack(pady=8, fill=tk.X, padx=20)

        status_frame = tk.Frame(
            bg=AppStyles.COLORS['balance_bg'],
            relief=tk.SUNKEN,
            bd=1,
            height=35
        )
        status_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=(10, 10), pady=(0, 10))
        status_frame.pack_propagate(False)

        self.status_label = tk.Label(
            status_frame,
            text="✅ ГОТОВ К РАБОТЕ",
            font=AppStyles.get_font('label'),
            bg=AppStyles.COLORS['balance_bg'],
            fg=AppStyles.COLORS['fg']
        )
        self.status_label.pack(side=tk.LEFT, padx=10, pady=5)

    def diposit(self):
        self.dialogs.diposit_dialogs(self.balance)

    def withdraw(self):
        self.dialogs.withdraw_dialogs(self.balance)

    def history(self):
        self.dialogs.history_dialogs()

    def reset(self):
        self.dialogs.reset_balance_dialog(self.balance)

    def exit(self):
        if messagebox.askyesno("Выход", "Вы уверены, что хотите выйти?"):
            self.storage.save_balance(self.balance)
            self.upedate_status("🫠 Выход из приложения")
            self.root.after(1000, self.root.destroy)

    def upedate_balance(self, new_balance):
        self.balance = new_balance
        self.update_balance_display()

    def upedate_status(self, status):
        self.status_label.config(text=status)

    def update_balance_display(self):
        """Обновление отображения баланса"""
        self.Money_balance_label.config(text=f"{self.balance:,.2f} руб.")



def main():
    root = tk.Tk()
    app = ATMAPP(root)
    root.mainloop()


if __name__ == "__main__":
    main()