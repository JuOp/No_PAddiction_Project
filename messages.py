
class Messages:
    @staticmethod
    def welcome_message(first_name):
        return f"Привет, {first_name}! Добро пожаловать в бота!"

    @staticmethod
    def already_registered_message(first_name):
        return f"{first_name}, вы уже зарегистрированы!"

    @staticmethod
    def help_message():
        return "Доступные команды: /start /help"
