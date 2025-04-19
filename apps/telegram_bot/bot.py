import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, CallbackContext


BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_text(
        f"Salom, {user.first_name}! Toyxona qidirish botiga xush kelibsiz. "
        f"Toyxona qidirish uchun /search komandasi orqali boshang."
    )
    
    main_menu(update, context)


def main_menu(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("🔍 Toyxona qidirish", callback_data='search')],
        [InlineKeyboardButton("📋 Mening buyurtmalarim", callback_data='my_bookings')],
        [InlineKeyboardButton("⚙️ Sozlamalar", callback_data='settings')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.message:
        update.message.reply_text("Kerakli bo'limni tanlang:", reply_markup=reply_markup)
    else:
        update.callback_query.answer()
        update.callback_query.edit_message_text("Kerakli bo'limni tanlang:", reply_markup=reply_markup)


def search_region(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    regions = [
        ["Toshkent shahri", "Toshkent viloyati"],
        ["Andijon", "Farg'ona", "Namangan"],
        ["Samarqand", "Buxoro", "Navoiy"],
        ["Qashqadaryo", "Surxondaryo"],
        ["Xorazm", "Qoraqalpog'iston"],
        ["Jizzax", "Sirdaryo"],
        ["⬅️ Orqaga"]
    ]
    
    keyboard = []
    for row in regions:
        keyboard_row = []
        for region in row:
            if region == "⬅️ Orqaga":
                keyboard_row.append(InlineKeyboardButton(region, callback_data='main_menu'))
            else:
                keyboard_row.append(InlineKeyboardButton(region, callback_data=f'region_{region}'))
        keyboard.append(keyboard_row)
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text("Viloyatni tanlang:", reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    
    if query.data == 'search':
        search_region(update, context)
    elif query.data == 'main_menu':
        main_menu(update, context)
    elif query.data.startswith('region_'):
        region = query.data.replace('region_', '')
        query.answer(f"Siz {region} ni tanladingiz")
        query.edit_message_text(f"{region} bo'yicha toyxonalar ro'yxati hozircha mavjud emas.")
    elif query.data == 'my_bookings':
        query.answer("Sizning buyurtmalaringiz")
        query.edit_message_text("Sizning buyurtmalaringiz hozircha mavjud emas.")
    elif query.data == 'settings':
        query.answer("Sozlamalar")
        query.edit_message_text("Sozlamalar bo'limi hozircha mavjud emas.")

def main() -> None:
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("search", search_region))
    dispatcher.add_handler(CallbackQueryHandler(button))
    

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()