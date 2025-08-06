from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,WebAppInfo,ReplyKeyboardRemove
from telegram.ext import CallbackContext

def start(update:Update,context:CallbackContext):
      bot = context.bot
      user_date = update.effective_user
      user = f"Assalomu alykum {user_date.full_name}"
      bot.send_message(
             chat_id = user_date.id,
             text = user,
             reply_markup = ReplyKeyboardMarkup(
                        keyboard=[
                                [KeyboardButton("🛍️ Buyurtma berish",web_app = WebAppInfo("https://eats.yandex.com/"))],
                                [KeyboardButton("📦 Buyurtmalarim"),KeyboardButton("⚙️ Sozlamalar")],
                                [KeyboardButton("ℹ️ Biz haqimizda"),KeyboardButton("🖊️ Fikr qoldirish")]
                        ],resize_keyboard=True,
                        one_time_keyboard=True
                )

      )

def handler_start(update:Update,context:CallbackContext):
      bot = context.bot
      bot.send_message(
            reply_markup = ReplyKeyboardMarkup(
                  keyboard=[
                        [KeyboardButton("🇺🇿 O'zbekiston"), KeyboardButton("🇷🇺 Rossiya")],
                        [KeyboardButton("🇬🇧 Angliya")]
                  ],resize_keyboard=True,
                  one_time_keyboard=True
            )
      )
def handler_phone(update:Update,context:CallbackContext):
            bot = context.bot 
            user = update.effective_user
            bot.send_message(
                  chat_id = user.id,
                  text = "Iltimos Telefon raqamingizni tashlang ",
                  reply_markup=ReplyKeyboardMarkup(
                        keyboard=[
                              [KeyboardButton("📞 Raqamni yuborish",request_contact=True)]
                        ],resize_keyboard=True,
                        one_time_keyboard=True
                        )
                  )
# def handler_contact(update:Update,context:callbackcontext):
#      update.message.reply_text("✅ Raqamingiz saqlandi!")

def handler_menu(update:Update,context:CallbackContext):
        bot = context.bot
        user = update.effective_user
        bot.send_message(
                chat_id = user.id,
                text = "✅ Raqamingiz saqlandi!",
                reply_markup = ReplyKeyboardMarkup(
                        keyboard=[
                                [KeyboardButton("🛍️ Buyurtma berish",web_app = WebAppInfo("https://eats.yandex.com/"))],
                                [KeyboardButton("📦 Buyurtmalarim"),KeyboardButton("⚙️ Sozlamalar")],
                                [KeyboardButton("ℹ️ Biz haqimizda"),KeyboardButton("🖊️ Fikr qoldirish")]
                        ],resize_keyboard=True,
                        one_time_keyboard=True
                )
                
        )
def handler_menu02(update:Update,context:CallbackContext):
      bot = context.bot
      user = update.effective_user
      bot.send_message(
            chat_id = user.id,
            text = "🏠 Bosh menyu",
            reply_markup = ReplyKeyboardMarkup(
                  keyboard=[
                              [KeyboardButton("🛍️ Buyurtma berish",web_app = WebAppInfo("https://eats.yandex.com/"))],
                              [KeyboardButton("📦 Buyurtmalarim"),KeyboardButton("⚙️ Sozlamalar")],
                              [KeyboardButton("ℹ️ Biz haqimizda"),KeyboardButton("🖊️ Fikr qoldirish")]
                  ],resize_keyboard=True,
                  one_time_keyboard=True
            )
            
      )
def handler_setting(update:Update,context:CallbackContext):
        bot = context.bot
        user = update.effective_user
        bot.send_message(
                chat_id = user.id,
                text = "⚙️ Sozlamalar",
                reply_markup = ReplyKeyboardMarkup(
                        keyboard=[
                                [KeyboardButton("🌐 Tilni o'zgartirish")],
                                [KeyboardButton("📞 Telefon raqamingizni o'zgartiring")],
                                [KeyboardButton("⬅️ Orqaga")]
                        ],resize_keyboard=True,
                        one_time_keyboard=True
                )
      )
def handler_language(update:Update,context:CallbackContext):
      bot = context.bot
      user = update.effective_user
      bot.send_message(
            chat_id = user.id,
            text = "Tilni Tanlang",
            reply_markup = ReplyKeyboardMarkup(
                  keyboard=[
                        [KeyboardButton("🇺🇿 O'zbekiston"), KeyboardButton("🇷🇺 Rossiya")],
                        [KeyboardButton("🇬🇧 Angliya")],
                        [KeyboardButton("⬅️ Orqaga")]
                  ],resize_keyboard=True,
                  one_time_keyboard=True
            )
      )
def handler_about(update:Update,context:CallbackContext):
      update.message.reply_text("Biz shu yerda Joylashganmz")
      update.message.reply_markdown_v2(
            text = "*Elektron pochta:* aloxiddinyogmirov651\\@gmail\\.com",
            )

def handler_idea(update:Update,context:CallbackContext):
      update.message.reply_markdown(
            "*Buyurtma berish uchun asosiy menyudagi “Buyurtma” tugmasidan foydalaning.*")
      bot = context.bot
      user = update.effective_user
      bot.send_message(
            chat_id = user.id,
            text = "Biz sizning fikr-mulohazalaringizni juda qadrlaymiz! Buyurtma berganingizdan so'ng, o'z fikr va mulohazalaringizni shu yerda qoldirishingiz mumkin.",
            reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                  [KeyboardButton("⬅️ Orqaga")]
            ],resize_keyboard=True,
            one_time_keyboard=True,)
      )
      
      
def handler_order(update:Update,context:CallbackContext):
       update.message.reply_text(
              "Sizda hali birorta ham buyurtma yo`q"
       )
      
def stop(update:Update,context:CallbackContext):
       update.message.reply_text(
              f"Tashrifingz uchun minnaddormiz. Tugmalar o'chirildi.\n Botni qayta ishga tuwirish uchun /start bosing ",
      reply_markup = ReplyKeyboardRemove()
       )

    