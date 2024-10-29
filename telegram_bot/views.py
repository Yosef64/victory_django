# telegram_bot/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import json

TOKEN = '7897490261:AAFMKWSSK0wHuSHlROpQH5WW9v4VsSTlkoA'
WEBHOOK_URL = 'https://victorydjango.vercel.app/api/index'
bot = Bot(token=TOKEN)

application = Application.builder().token(TOKEN).build()
application.bot.set_webhook(url=WEBHOOK_URL)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [[InlineKeyboardButton("Visit Web App", web_app={"url": "https://josialex.vercel.app/"})]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome! Click the button below to visit our web app.", reply_markup=reply_markup)

application.add_handler(CommandHandler("start", start))

@csrf_exempt
async def webhook(request):
    if request.method == 'POST':
        update = Update.de_json(json.loads(request.body), bot)
        await application.update_queue.put(update)
        
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "Bot is running on Django."})
