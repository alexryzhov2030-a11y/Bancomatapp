import json
import os
from datetime import datetime


class Storage:
    """Класс для работы с хранением данных"""

    def __init__(self, balance_file="balance.json", history_file="history.txt"):
        self.balance_file = balance_file
        self.history_file = history_file
        self.init_files()

    def init_files(self):
        """Инициализация файлов"""
        # Проверка файла баланса
        if not os.path.exists(self.balance_file):
            self.save_balance(0)

        # Проверка файла истории
        if not os.path.exists(self.history_file):
            with open(self.history_file, "w", encoding="utf-8") as file:
                pass

    def load_balance(self):
        """Загрузка баланса из файла"""
        try:
            if os.path.exists(self.balance_file):
                with open(self.balance_file, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    balance = data.get("balance", 0)
                    if isinstance(balance, (int, float)) and balance >= 0:
                        return balance
            return 0
        except (json.JSONDecodeError, FileNotFoundError, KeyError, ValueError):
            self.save_balance(0)
            return 0

    def save_balance(self, balance):
        """Сохранение баланса в файл"""
        try:
            with open(self.balance_file, "w", encoding="utf-8") as file:
                json.dump({
                    "balance": balance,
                    "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }, file, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Ошибка при сохранении баланса: {e}")
            return False

    def log_transaction(self, operation, amount, balance):
        """Запись операции в историю"""
        try:
            with open(self.history_file, "a", encoding="utf-8") as file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{timestamp} | {operation} | {amount:,.2f} руб. | Баланс: {balance:,.2f} руб.\n")
            return True
        except Exception as e:
            print(f"Ошибка при записи в историю: {e}")
            return False

    def load_history(self):
        """Загрузка истории операций"""
        try:
            with open(self.history_file, "r", encoding="utf-8") as file:
                return file.readlines()
        except FileNotFoundError:
            return []

    def clear_history(self):
        """Очистка истории операций"""
        try:
            with open(self.history_file, "w", encoding="utf-8") as file:
                file.write("")
            return True
        except Exception as e:
            print(f"Ошибка при очистке истории: {e}")
            return False