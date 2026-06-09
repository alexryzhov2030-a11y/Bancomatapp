import tkinter as tk 
from tkinter import messagebox
from styles import AppStyles 

class Dialogs:
    def __init__(self, parent, storage, update_balance, update_status):
        self.parent = parent
        self.storage = storage
        self.update_balance = update_balance
        self.update_status = update_status
        

                
    def diposit_dialogs(self, current_balance):
        dialog = tk.Toplevel(self.parent)
        dialog.title("Пополнение счёта")
        dialog.geometry("400x300")
        dialog.configure(bg=AppStyles.COLORS['bg'])
        dialog.resizable(False, False)
        dialog.grab_set()

        tk.Label(
            dialog,
            text="💵 ПОПОЛНЕНИЕ СЧЕТА 💵",
            font=AppStyles.get_font('title'),
            bg=AppStyles.COLORS['bg'],
            fg=AppStyles.COLORS['fg']
        ).pack(pady=20)

        tk.Label(
            dialog,
            text=f"Текущий баланс: {current_balance:.2f} руб.",
            font=AppStyles.get_font('label'),
            bg=AppStyles.COLORS['bg'],
            fg=AppStyles.COLORS['fg']
        ).pack(pady=(0, 15))

        tk.Label(
            dialog,
            text="Введите сумму (кратную 100 руб.):",
            font=AppStyles.get_font('label'),
            bg=AppStyles.COLORS['bg'],
            fg=AppStyles.COLORS['fg']
        ).pack(pady=(0, 10))

        amount_entry = tk.Entry(
            dialog,
            font=AppStyles.get_font('label'),
            justify='center',
            bg='white',
            fg='black',
            bd=2,
            relief=tk.RAISED,
            width=25
        )
        amount_entry.pack(pady=(0, 20), padx=60, fill=tk.X)
        amount_entry.focus()

        tk.Button(
            dialog,
            text="💵 ПОПОЛНИТЬ",
            font=AppStyles.get_font('button'),
            bg=AppStyles.COLORS['deposit'],
            fg=AppStyles.COLORS['fg'],
            relief=tk.RAISED,
            bd=2,
            cursor="hand2",
            height=2,
            width=20
        ).pack(pady=20)

    def withdraw_dialogs(self, current_balance):
        dialog = tk.Toplevel(self.parent)
        dialog.title("Снятие средств")
        dialog.geometry("400x300")
        dialog.configure(bg=AppStyles.COLORS['bg'])
        dialog.resizable(False, False)
        dialog.grab_set()

        tk.Label(
            dialog,
            text="💸 СНЯТИЕ СРЕДСТВ 💸",
            font=AppStyles.get_font('title'),
            bg=AppStyles.COLORS['bg'],
            fg=AppStyles.COLORS['fg']
        ).pack(pady=20)

        tk.Label(
            dialog,
            text=f"Доступно: {current_balance:.2f} руб.",
            font=AppStyles.get_font('label'),
            bg=AppStyles.COLORS['bg'],
            fg=AppStyles.COLORS['fg']
        ).pack(pady=(0, 15))

        tk.Label(
            dialog,
            text="Введите сумму (кратную 100 руб.):",
            font=AppStyles.get_font('label'),
            bg=AppStyles.COLORS['bg'],
            fg=AppStyles.COLORS['fg']
        ).pack(pady=(0, 10))

        amount_entry = tk.Entry(
            dialog,
            font=AppStyles.get_font('label'),
            justify='center',
            bg='white',
            fg='black',
            bd=2,
            relief=tk.RAISED,
            width=25
        )
        amount_entry.pack(pady=(0, 20), padx=60, fill=tk.X)
        amount_entry.focus()

        tk.Button(
            dialog,
            text="💸 СНЯТЬ",
            font=AppStyles.get_font('button'),
            bg=AppStyles.COLORS['withdraw'],
            fg=AppStyles.COLORS['fg'],
            relief=tk.RAISED,
            bd=2,
            cursor="hand2",
            height=2,
            width=20
        ).pack(pady=20)

    def history_dialogs(self):
        dialog = tk.Toplevel(self.parent)
        dialog.title("История операций")
        dialog.geometry("750x550")
        dialog.configure(bg=AppStyles.COLORS['bg'])
        dialog.resizable(False, False)
        dialog.grab_set()

        tk.Label(
            dialog,
            text="📜 ИСТОРИЯ ОПЕРАЦИЙ 📜",
            font=AppStyles.get_font('title'),
            bg=AppStyles.COLORS['bg'],
            fg=AppStyles.COLORS['fg']
        ).pack(pady=20)

        text_frame = tk.Frame(dialog, bg=AppStyles.COLORS['bg'])
        text_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        history_text = tk.Text(
            text_frame,
            font=AppStyles.get_font('history'),
            bg=AppStyles.COLORS['balance_bg'],
            fg=AppStyles.COLORS['fg'],
            relief=tk.SUNKEN,
            bd=2,
            yscrollcommand=scrollbar.set,
            wrap=tk.WORD
        )
        history_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=history_text.yview)

        history_text.config(state=tk.DISABLED)

        buttons_frame = tk.Frame(dialog, bg=AppStyles.COLORS['bg'])
        buttons_frame.pack(pady=20)

        tk.Button(
            buttons_frame,
            text="ЗАКРЫТЬ",
            font=AppStyles.get_font('button'),
            bg=AppStyles.COLORS['exit'],
            fg=AppStyles.COLORS['fg'],
            command=dialog.destroy,
            relief=tk.RAISED,
            bd=2,
            cursor="hand2",
            width=15,
            height=1
        ).pack(side=tk.LEFT, padx=10)

        tk.Button(
            buttons_frame,
            text="ОЧИСТИТЬ ИСТОРИЮ",
            font=AppStyles.get_font('button'),
            bg=AppStyles.COLORS['withdraw'],
            fg=AppStyles.COLORS['fg'],
            relief=tk.RAISED,
            bd=2,
            cursor="hand2",
            width=15,
            height=1,
            command=lambda: self.clear_history_with_dialog(dialog, history_text)
        ).pack(side=tk.LEFT, padx=10)
        
        
    def clear_history_with_dialog (self, dialog, history_text):
        if messagebox.askyesno("Подтверждение", "Вы уверены, что хотите очистить историю операций?"):
            if self.storage.clear_history():
                history_text.config(state=tk.NORMAL)
                history_text.delete(1.0, tk.END)
                history_text.insert(1.0, "История операций очищена.\n")
                messagebox.showinfo("Успех", "История операций очищена.")
                self.update_status("История операций очищена.")
            else:
                messagebox.showerror("Ошибка", "Не удалось очистить историю операций.")
                
    def reset_balance_dialog (self, current_balance):
        if messagebox.askyesno("Сброс баланса", f"Вы уверены, что хотите сбросить баланс на {current_balance} рублей?"):
            old_balance = current_balance
            self.storage.log_transaction("СБРОС БАЛАНСА", 0, old_balance)
            self.storage.save_balance(0)
            self.update_balance(0)
            messagebox.showinfo("Успех", "Баланс сброшен.")
            self.update_status("Баланс сброшен.")