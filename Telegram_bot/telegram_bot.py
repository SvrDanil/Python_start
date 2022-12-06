from sympy import Symbol,collect
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def sum(update: Update, context:ContextTypes.DEFAULT_TYPE)-> None:
    user_text = update.message.text
    user_text = user_text.replace("/add",'')
    user_text = user_text.replace('^','**').replace("x",'*x').replace('-0', '')
    first = user_text.split()[0]
    second = user_text.split()[1]
    x = Symbol('x')
    result = str(collect(first + ' + '+ second, x))
    await update.message.reply_text(f'Первое слагаемое : {first}')
    await update.message.reply_text(f'Второе слагаемое : {second}')
    await update.message.reply_text(result)

async def help(update: Update, context:ContextTypes.DEFAULT_TYPE)-> None:
    await update.message.reply_text('''Это Telegram бот для вычесления суммы 2 многочленов 
                                    \n Введите /sum и два многочлена через пробел (переменная x)''')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name} достпные функции:\n /help \n /start')


updater = ApplicationBuilder().token("").build()
updater.add_handler(CommandHandler("sum", sum))
updater.add_handler(CommandHandler("help", help))
updater.add_handler(CommandHandler("start", start))
print("Server Started ")
updater.run_polling()
