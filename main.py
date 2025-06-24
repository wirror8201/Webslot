from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
import logging

import config
from handlers import start, menu, signup, bookings, about, language

# Логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

def main():
    updater = Updater(token=config.BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Команда /start
    dp.add_handler(CommandHandler('start', start.start_command))

    # Выбор языка и главное меню
    dp.add_handler(CallbackQueryHandler(start.language_callback, pattern='^LANG_'))
    dp.add_handler(CallbackQueryHandler(menu.menu_handler, pattern='^MENU_'))

    # Flow “Записаться”
    dp.add_handler(CallbackQueryHandler(signup.service_selected, pattern='^SERVICE_'))
    dp.add_handler(CallbackQueryHandler(signup.date_selected, pattern='^DATE_'))
    dp.add_handler(CallbackQueryHandler(signup.master_selected, pattern='^MASTER_'))
    dp.add_handler(CallbackQueryHandler(signup.slot_selected, pattern='^SLOT_'))
    dp.add_handler(MessageHandler(Filters.contact, signup.phone_received))
    dp.add_handler(MessageHandler(Filters.regex(r'^\+?\d+$'), signup.phone_received))

    # Мои брони и отмена
    dp.add_handler(CallbackQueryHandler(bookings.my_bookings, pattern='^BOOKINGS_'))
    dp.add_handler(CallbackQueryHandler(bookings.cancel_booking, pattern='^CANCEL_'))

    # О нас
    dp.add_handler(CallbackQueryHandler(about.about_handler, pattern='^ABOUT$'))

    # Смена языка
    dp.add_handler(CallbackQueryHandler(language.change_language, pattern='^CHANGE_LANG$'))

    # Ловим всё остальное
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, menu.unknown))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
