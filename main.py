import telebot
import time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Import loader and bot starter
from utils.env_loader import load_env
from utils.bot_starter import iniciar_bot

# Load API key
API_KEY = load_env()

# Initialize API key
bot = telebot.TeleBot(API_KEY)

# /start
@bot.message_handler(commands=["start"])
def start_command(message):
    text = (
        "Hello! I'm [Telegram_Interactive_Button](https://t.me/GitHub_v1_bot), created to demonstrate button functions!\n\n"
        "I'm here to make your experience with cloud logs more accessible and powerful.\n\n"
        "Explore my interactive features and see how I can help you manage information and log queries simply and efficiently.\n\n"
        "🚀 **What can I do for you?**\n"
        "- **Quick Queries**: Access logs with one click\n"
        "- **Flexible Plans**: Choose the right plan for you\n"
        "- **Security**: Manage your info safely and responsibly.\n\n"
        "👨‍💻 Proudly created by [MozzieGM!](https://github.com/MozzieGM) for the GitHub community!"
    )

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Subscribe to Plans [Examples]", callback_data="choose_plan"))
    markup.add(InlineKeyboardButton("About", callback_data="about"))
    markup.add(InlineKeyboardButton("Commands", callback_data="commands"))
    markup.add(InlineKeyboardButton("Official GitHub", url="https://github.com/MozzieGM"), InlineKeyboardButton("Support", url="https://t.me/Ricky_1337"))

    bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode='Markdown')


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "choose_plan":
        plans_markup = InlineKeyboardMarkup()
        plans_markup.add(InlineKeyboardButton("Basic [Free]", callback_data="plan_basic"))
        plans_markup.add(InlineKeyboardButton("Premium", callback_data="plan_premium"))
        plans_markup.add(InlineKeyboardButton("Pro", callback_data="plan_pro"))
        plans_markup.add(InlineKeyboardButton("Elite", callback_data="plan_elite"))
        plans_markup.add(InlineKeyboardButton("Back", callback_data="back"))
        bot.edit_message_text("Choose the plan that suits your needs:", chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=plans_markup)

    elif call.data == "plan_basic":
        basic_text = (
            "*Basic Plan [Free]*\n\n"
            "🔍 *Queries:* Up to 5 per day\n"
            "⏳ *Time Window:* 4 hours\n"
            "📊 *Result Limit:* 25 per query\n"
            "💵 *Cost:* Free\n\n"
            "🚀 Start with the basics to get a feel for how our system works!"
        )
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Back", callback_data="choose_plan"))
        bot.edit_message_text(basic_text, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup, parse_mode='Markdown')

    elif call.data == "plan_premium":
        premium_text = (
            "*Premium Plan*\n\n"
            "🔍 *Queries:* Up to 10 per day\n"
            "⏳ *Time Window:* 1 hour\n"
            "📊 *Result Limit:* 100 per query\n"
            "💵 *Cost:* $70\n\n"
            "💼 Perfect for those who want to optimize their use and have more control over queries!"
        )
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Back", callback_data="choose_plan"))
        bot.edit_message_text(premium_text, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup, parse_mode='Markdown')

    elif call.data == "plan_pro":
        pro_text = (
            "*Pro Plan*\n\n"
            "🔍 *Queries:* Up to 40 per day\n"
            "⏳ *Time Window:* 40 minutes\n"
            "📊 *Result Limit:* 150 per query\n"
            "💵 *Cost:* $150\n\n"
            "💼 Recommended for advanced users with a high volume of data."
        )
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Back", callback_data="choose_plan"))
        bot.edit_message_text(pro_text, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup, parse_mode='Markdown')

    elif call.data == "plan_elite":
        elite_text = (
            "*Elite Plan*\n\n"
            "🔍 *Queries:* Up to 100 per day\n"
            "⏳ *Time Window:* 20 minutes\n"
            "📊 *Result Limit:* 200 per query\n"
            "💵 *Cost:* $250\n\n"
            "🎩 The best plan for those who want maximum performance and flexibility."
        )
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Back", callback_data="choose_plan"))
        bot.edit_message_text(elite_text, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup, parse_mode='Markdown')

    elif call.data == "about":
        about_markup = InlineKeyboardMarkup()
        about_markup.add(InlineKeyboardButton("Back", callback_data="back"))
        about_text = (
            "With this bot, you have the freedom to create and personalize your own experience. 🔧\n\n"
            "🎯 **Main Features**:\n"
            "- Add new functions as needed.\n"
            "- Create and customize interactive buttons.\n"
            "- Change texts, messages, and create unique responses for users.\n\n"
            "💡 This bot is highly flexible, allowing you to tailor interactions and features to your liking!\n"
            "Whether to automate processes, facilitate queries, or create custom commands, Telegram_Interactive_Button can do all that and more!\n\n"
            "🚀 **Why choose Telegram_Interactive_Button?**\n"
            "- Fast and efficient in log and information retrieval.\n"
            "- Easy to customize and expand.\n"
            "- Perfect for integrating cloud functions into daily tasks.\n\n"
            "Proudly created by [MozzieGM!](https://github.com/MozzieGM). Explore and discover the power of personalization!"
        )
        bot.edit_message_text(about_text, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=about_markup, parse_mode='Markdown')

    elif call.data == "commands":
        commands_markup = InlineKeyboardMarkup()
        commands_markup.add(InlineKeyboardButton("/start", callback_data="start_command"))
        commands_markup.add(InlineKeyboardButton("/commands", callback_data="commands_command"))
        commands_markup.add(InlineKeyboardButton("Back", callback_data="back"))
        bot.edit_message_text("Here are the available commands:", chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=commands_markup)

    elif call.data == "start_command":
        start_markup = InlineKeyboardMarkup()
        start_markup.add(InlineKeyboardButton("Back", callback_data="commands"))
        bot.edit_message_text("The /start command allows you to start the bot.", chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=start_markup)

    elif call.data == "commands_command":
        commands_comand_markup = InlineKeyboardMarkup()
        commands_comand_markup.add(InlineKeyboardButton("Back", callback_data="commands"))
        bot.edit_message_text("The /commands command shows the available commands.", chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=commands_comand_markup)

    elif call.data == "back":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        start_command(call.message)

# /commands
@bot.message_handler(commands=['commands'])
def list_commands(message):
    response = (
        "📋 *Available Commands:*\n\n"
        "`/start` - Starts the bot and shows available modules.\n"
        "`/commands` - Displays this list of commands.\n"
    )
    bot.reply_to(message, response, parse_mode='Markdown')

# Valid commands list
valid_commands = [
    "/start", "/commands"
]

# Capture invalid commands
@bot.message_handler(func=lambda message: message.text.startswith('/') and not message.text.split()[0] in valid_commands)
def invalid_command(message):
    response = bot.reply_to(message, "This command does not exist. Type /commands to see which commands you can use. This message will be deleted in 10 seconds.")
    time.sleep(10)

    try:
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        bot.delete_message(chat_id=response.chat.id, message_id=response.message_id)
    except Exception as e:
        print(f"Error while trying to delete messages: {e}")

if __name__ == '__main__':
    iniciar_bot(bot)
