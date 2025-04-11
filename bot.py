
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler,
    ContextTypes
)
from database import Database
from messages import Messages

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if not user:
        await update.message.reply_text("Не удалось определить пользователя.")
        return
    user_id = user.id
    username = user.username
    first_name = user.first_name

    if Database.user_exists(user_id):
        await update.message.reply_text(Messages.already_registered_message(first_name), parse_mode='HTML')
        return

    if Database.register_user(user_id, username, first_name):
        await update.message.reply_text(Messages.welcome_message(first_name), parse_mode='HTML')
    else:
        await update.message.reply_text("Ошибка регистрации. Попробуйте позже.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(Messages.help_message(), parse_mode='HTML')

def main():
    app = ApplicationBuilder().token("YOUR_BOT_TOKEN_HERE").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    logger.info("Бот запущен...")
    app.run_polling()
