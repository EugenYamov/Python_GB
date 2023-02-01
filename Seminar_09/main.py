from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import*

app = ApplicationBuilder().token("6040734300:AAHVPVRHctHQq4S5wQK7nLnDs7g8FZzBcjw").build()

print('start')

app.add_handler(CommandHandler("hi", hello_command))
app.add_handler(CommandHandler("sum", sum_command))


app.run_polling()