import os
from dotenv import load_dotenv 
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from bs import login_to_website  # Assuming you have a function to handle the login logic
load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

# Dictionary to hold user states and data
user_states = {}

# Possible states
STATE_WAITING_EMAIL = 1
STATE_WAITING_PASSWORD = 2

print("Bot is running...")

@bot.message_handler(commands=['start'])
def send_signal_message(message):
    # Create inline keyboard
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("🎁  Log in", callback_data="log_in"),
    )
    bot.send_message(
        message.chat.id,
        "Welcome to my testing bot!",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "log_in":
        bot.answer_callback_query(call.id, "Please enter your email:")
        user_states[call.from_user.id] = {'state': STATE_WAITING_EMAIL}
        bot.send_message(call.message.chat.id, "Please enter your email:")

@bot.message_handler(func=lambda message: message.from_user.id in user_states)
def handle_login_steps(message):
    user_id = message.from_user.id
    user_data = user_states.get(user_id, {})

    if user_data.get('state') == STATE_WAITING_EMAIL:
        # Save email and ask for password
        user_data['email'] = message.text
        user_data['state'] = STATE_WAITING_PASSWORD
        user_states[user_id] = user_data
        bot.send_message(message.chat.id, "Thanks! Now please enter your password:")

    elif user_data.get('state') == STATE_WAITING_PASSWORD:
        # Save password and perform login
        user_data['password'] = message.text

        email = user_data['email']
        password = user_data['password']

        # Clear user state after collecting credentials
        user_states.pop(user_id)

        # Here, add your login logic to the website with email & password
        # For example, call a function login_to_website(email, password)
        success = login_to_website(email, password)

        if success:
            bot.send_message(message.chat.id, "Login successful! 🎉")
        else:
            bot.send_message(message.chat.id, "Login failed. Please check your credentials and try again.")

bot.infinity_polling()
