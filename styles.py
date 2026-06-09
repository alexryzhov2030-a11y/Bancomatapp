from tkinter.font import Font


class AppStyles:
    """Класс для хранения стилей и цветовой схемы приложения"""

    # Цветовая схема
    COLORS = {
        'bg': "#2c3e50",  # Основной фон
        'fg': "#ecf0f1",  # Цвет текста
        'button': "#3498db",  # Стандартная кнопка
        'button_hover': "#2980b9",  # Кнопка при наведении
        'deposit': "#27ae60",  # Пополнение
        'withdraw': "#e74c3c",  # Снятие
        'history': "#f39c12",  # История
        'reset': "#8e44ad",  # Сброс баланса
        'exit': "#95a5a6",  # Выход
        'balance_bg': "#34495e",  # Фон блока баланса
        'balance_text': "#f1c40f"  # Цвет суммы баланса
    }

    # Шрифты
    FONTS = {
        'title': ('Helvetica', 24, 'bold'),
        'button': ('Helvetica', 12, 'bold'),
        'label': ('Helvetica', 14),
        'history': ('Consolas', 10)
    }

    @classmethod
    def get_font(cls, name):
        """Получить объект шрифта по имени"""
        return Font(family=cls.FONTS[name][0],
                    size=cls.FONTS[name][1],
                    weight=cls.FONTS[name][2] if len(cls.FONTS[name]) > 2 else 'normal')

    @classmethod
    def darken_color(cls, color_name):
        """Затемнение цвета для эффекта наведения"""
        dark_colors = {
            cls.COLORS['deposit']: "#1e8449",
            cls.COLORS['withdraw']: "#c0392b",
            cls.COLORS['history']: "#e67e22",
            cls.COLORS['exit']: "#7f8c8d",
            cls.COLORS['reset']: "#6c3483"
        }
        return dark_colors.get(color_name, "#7f8c8d")