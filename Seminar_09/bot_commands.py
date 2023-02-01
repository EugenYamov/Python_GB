from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hi, {update.effective_user.first_name}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split()
    await update.message.reply_text(f'{int(items[1])} + {int(items[2])} = {int(items[1]) + int(items[2])}')