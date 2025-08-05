from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from handlers import start,stop,handler_phone,handler_menu,handler_setting,handler_language,handler_about,handler_menu02,handler_idea,handler_order
from config import TOKEN

def main()->None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    #Command Handler 
    dispatcher.add_handler(CommandHandler("start",start))
    dispatcher.add_handler(CommandHandler("stop",stop))

    #Message Handler
   # dispatcher.add_handler(MessageHandler(Filters.text("start"),handler_start))
    dispatcher.add_handler(MessageHandler(Filters.text("🇺🇿 O'zbekiston"),handler_phone))
    dispatcher.add_handler(MessageHandler(Filters.contact,handler_menu))
    dispatcher.add_handler(MessageHandler(Filters.text("📦 Buyurtmalarim"),handler_order))
    dispatcher.add_handler(MessageHandler(Filters.text("⚙️ Sozlamalar"),handler_setting))
    dispatcher.add_handler(MessageHandler(Filters.text("🌐 Tilni o'zgartirish"),handler_language))
    dispatcher.add_handler(MessageHandler(Filters.text("⬅️ Orqaga"),handler_menu02))
    dispatcher.add_handler(MessageHandler(Filters.text("ℹ️ Biz haqimizda"),handler_about))
    dispatcher.add_handler(MessageHandler(Filters.text("🖊️ Fikr qoldirish"),handler_idea))
    


    updater.start_polling()
    updater.idle()
if __name__=="__main__":
    main()