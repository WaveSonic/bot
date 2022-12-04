import json
import telebot
from telebot import types
import random
import datetime
text_chat_user_data = {}
id = 0
#330937061
bot = telebot.TeleBot("5726407828:AAElJ8Ytdy_zdWWidIMLv7P1rwDCeqm0mAY")
lifehacks = ["Ніхто нікого не кидає, просто хтось іде вперед. Той, хто відстав, вважає, що його кинули.",
             "Якщо людина дорікнула тобі в невдячності, з'ясуй, скільки коштує її послуга, розрахуйся і "
             "більше не май з нею справи.",
             "Гризи граніт науки, а не горло своєму ближньому, якщо вже хочеться щось гризти.",
             "Депресія для того й дана людині, щоби подумати про себе.",
             "Якщо людина нічого доброго не може сказати про себе, а сказати хочеться, вона починає говорити погане "
             "про інших.",
             "Якщо ви добре думаєте про себе, навіщо ж вам потрібно, щоб ще хтось добре думав про вас.",
             "Роби, що хочеш, і не питай дозволів. Раптом відмовлять.",
             "Краще спілкуватися з гарною книгою, ніж з порожньою людиною.",
             "Здатність любити і добре переносити самотність - показник духовної зрілості. "
             "Все найкраще ми робимо, коли знаходимося на самоті.",
             "Я не знаю шляху до успіху. Але я знаю шлях до невдачі - це бажання сподобатися всім.",
             "Немає чоловічої чи жіночої логіки, є вміння чи невміння грамотно мислити.",
             "Хочеш дізнатися свого головного ворога? Подивися в дзеркало. Розберися з ним - інші втечуть.",
             "З друзями спілкуватися приємно, а з ворогами - корисно.",
             "Є єдина поважна причина для розриву відносин і звільнення з роботи - неможливість особистісного "
             "зростання в умовах, що склалися.",
             "Незріла особистість часто знає, але не вміє. Зріла не лише знає, але і вміє. "
             "Тому незріла особистість критикує, а зріла робить.",
             "Ділися тільки радістю і з друзями, і з ворогами. Друг порадіє, ворог засмутиться.",
             "Не женися за щастям, а знайди те місце, де воно буває. І щастя саме тебе знайде. Можу підказати те місце,"
             "де є твоє щастя, - це ти сам. А шлях до нього - максимальний розвиток всіх своїх здібностей.",
             "Щастя - це 'побічний продукт' правильно організованої діяльності.",
             "Якщо ти комусь хочеш щось довести - значить, ти живеш заради того, кому хочеш це довести. Якщо ти живеш "
             "заради себе, то тоді немає необхідності комусь щось доводити.",
             "Мрії - це голоси наших здібностей. Ось я не мрію співати в опері. Немає ні голосу, ні слуху. "
             "А якби мріяв, то, отже, цю мрію підігрівали б мої здібності. Отже, спробував би потрапити в оперу. "
             "Просто потрібно подумати, як цю мрію здійснити. Тут головне - не поспішати, тоді вийде досить швидко. "
             "Добре, коли людина може про себе сказати наступне: 'Я тільки тим і займаюся, що намагаюся здійснити "
             "свої мрії'.",
             "Досягни успіху - зникнуть образи."]

def data_open():
    with open('data.json') as file:
        data = json.load(file)
        return data

def data_ps():
    with open('PS_data.json') as file:
        data = json.load(file)
        return data

def save_ps(data):
    with open('PS_data.json', 'w') as file:
        json.dump(data, file, indent=4)

def data_save(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

for x in data_ps():
    id_ps = x

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    but_1 = types.KeyboardButton("Опитування")
    but_2 = types.KeyboardButton("Лайфхак від психолога")
    but_3 = types.KeyboardButton("Підтримка через чат")
    but_4 = types.KeyboardButton("Підтримка через відео зв’язок")
    but_5 = types.KeyboardButton("Про психолога")
    but_6 = types.KeyboardButton("Відгук")
    but_7 = types.KeyboardButton("Вихід")
    markup.add(but_1, but_2, but_3, but_4, but_5, but_6, but_7)
    return markup

def markup_ps():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    but_1 = types.KeyboardButton("Підтримка через чат")
    but_2 = types.KeyboardButton("Підтримка через відео зв’язок")
    but_3 = types.KeyboardButton("Про психолога")
    but_4 = types.KeyboardButton("Відгуки")
    but_5 = types.KeyboardButton("Вихід")
    markup.add(but_1, but_2, but_3, but_4, but_5)
    return markup


def starting(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    but_1 = types.KeyboardButton("Студент")
    but_2 = types.KeyboardButton("Психолог")
    markup.add(but_1, but_2)
    text = bot.send_message(message.chat.id, f"<b>Хто ви?</b>", parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(text, role)
    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")


user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    but_1 = types.KeyboardButton("Студент")
    but_2 = types.KeyboardButton("Психолог")
    markup.add(but_1, but_2)
    text = bot.send_message(message.chat.id, f"<b>Хто ви?</b>", parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(text, role)
    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")

def role(message):
    if message.text == "Студент":
        if str(message.from_user.id) not in data_open():
            text = bot.send_message(message.chat.id, f'<b>Як вас звати?</b>', parse_mode='html',
                                    reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(text, age)
        else:
            text = bot.send_message(message.chat.id, "<b>Ласкаво просимо</b>" , parse_mode="html",
                                    reply_markup=main_menu())
            bot.register_next_step_handler(text, menu)

    elif message.text == "Психолог":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        but_1 = types.KeyboardButton("Вихід")
        markup.add(but_1)
        text = bot.send_message(message.chat.id, '<b>Авторизуйтеся\nЛогін:</b>', parse_mode='html',
                                reply_markup=markup)
        bot.register_next_step_handler(text, password)

    elif message.text == '/start':
        starting(message)

    else:
        text = bot.send_message(message.chat.id, 'Упс. Щось пішло не так. Виберіть будь-ласка кнопку')
        bot.register_next_step_handler(text, role)

    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")

################################### USER ############################
def age(message):
    if message.text == '/start':
        starting(message)
    else:
        user_data.update({message.from_user.id: {"Імя": message.text, "Номер": "Немає", "Відгук": "Немає", "chat":False,
                                                 "Опитування":{"Опитування": "Не пройдено"}, "in_chat": False, "video_chat_b": False,
                                                 "video_chat": False}})
        text = bot.send_message(message.chat.id, f'<b>Скільки вам років?</b>', parse_mode='html')
        bot.register_next_step_handler(text, group)
    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")


def group(message):
    if message.text == '/start':
        starting(message)
    elif not message.text.isdigit():
        text = bot.send_message(message.chat.id, 'Упс. Щось пішло не так. Введіть будь-ласка число')
        bot.register_next_step_handler(text, group)
    else:
        user_data[message.from_user.id].update({"Вік":message.text})
        text = bot.send_message(message.chat.id, f'<b>Ваша група?</b>', parse_mode='html')
        bot.register_next_step_handler(text, kurs)
    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")


def kurs(message):
    if message.text == '/start':
        starting(message)
    else:
        user_data[message.from_user.id].update({"Група": message.text})
        text = bot.send_message(message.chat.id, f'<b>Ваш курс</b>', parse_mode='html')
        bot.register_next_step_handler(text, sex)
    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")


def sex(message):
    if message.text == '/start':
        starting(message)
    elif not message.text.isdigit():
        text = bot.send_message(message.chat.id, 'Упс. Щось пішло не так. Введіть будь-ласка число')
        bot.register_next_step_handler(text, sex)
    else:
        user_data[message.from_user.id].update({"Курс": message.text})
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        but_1 = types.KeyboardButton('Чоловіча')
        but_2 = types.KeyboardButton('Жіноча')
        markup.add(but_1, but_2)
        text = bot.send_message(message.chat.id, f'<b>Ваша стать</b>', parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(text, fin_reg)
    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")


def fin_reg(message):
    if message.text == '/start':
        starting(message)
    elif message.text not in ['Чоловіча', 'Жіноча']:
        text = bot.send_message(message.chat.id, 'Упс. Щось пішло не так. Виберіть будь-ласка кнопку')
        bot.register_next_step_handler(text, fin_reg)
    else:
        user_data[message.from_user.id].update({"Стать": message.text})
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        but_1 = types.KeyboardButton('Вірно')
        but_2 = types.KeyboardButton('Не вірно')
        markup.add(but_1, but_2)
        text = bot.send_message(message.chat.id, f'<b>Ваc звати: {user_data[message.from_user.id]["Імя"]}\n'
                                                 f'Ваш вік: {user_data[message.from_user.id]["Вік"]}\n'
                                                 f'Група: {user_data[message.from_user.id]["Група"]}\n'
                                                 f'Курс:{user_data[message.from_user.id]["Курс"]}\n'
                                                 f'Ваша стать: {user_data[message.from_user.id]["Стать"]}\n</b>',
                                parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(text, confirm)
    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")

def confirm(message):
    if message.text == 'Вірно':
        data = data_open()
        data.update(user_data)
        data_save(data)
        text = bot.send_message(message.chat.id, "<b>Ви успішно зареєстровані</b>", parse_mode='html', reply_markup=main_menu())
        bot.register_next_step_handler(text, menu)
    elif message.text == 'Не вірно' or message.text == '/start':
        starting(message)
    else:
        text = bot.send_message(message.chat.id, 'Упс. Щось пішло не так. Виберіть будь-ласка кнопку')
        bot.register_next_step_handler(text, confirm)
    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")

####################################################################################################################
def pre_menu(message):
    text = bot.send_message(message.chat.id, "<b>Вітаємо в меню</b>", parse_mode='html',
                            reply_markup=main_menu())
    bot.register_next_step_handler(text, menu)
    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")


def menu(message):
    if message.text == 'Вихід':
        starting(message)

    elif message.text == "Опитування":
        global user_data
        user_data = data_open()
        user_data[str(message.from_user.id)].update({"Опитування":{}})
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        but_1 = types.KeyboardButton("Ніколи")
        but_2 = types.KeyboardButton("В окремі дні")
        but_3 = types.KeyboardButton("У більш як половину днів")
        but_4 = types.KeyboardButton("Майже кожен день")
        markup.add(but_1, but_2, but_3, but_4)
        text = bot.send_message(message.chat.id, "<b>Пройдіть будь-ласка дане опитування, для більш детальної оцінки "
                                                 "вашого психічного здоровя</b>", parse_mode='html')
        bot.send_message(message.chat.id, "<b>1. Протягом останніх двох тижнів, як часто ви почувалися знервовано, "
                                          "тривожно або на межі?</b>", parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(text, q1)

    elif message.text == 'Лайфхак від психолога':
        text = bot.send_message(message.chat.id, f"<b>{random.choice(lifehacks)}</b>", parse_mode='html')
        bot.register_next_step_handler(text, menu)

    elif message.text == "Підтримка через чат":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        but_1 = types.KeyboardButton('Так')
        but_2 = types.KeyboardButton('Ні')
        markup.add(but_1, but_2)
        text = bot.send_message(message.chat.id, "<b>Бажаєте отримати підтримку від психолога?</b>",
                                parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(text, chat)


    elif message.text == "Підтримка через відео зв’язок":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        but_1 = types.KeyboardButton('Так')
        but_2 = types.KeyboardButton('Ні')
        markup.add(but_1, but_2)
        text = bot.send_message(message.chat.id, "<b>Бажаєте отримати підтримку від психолога через відео-чат?</b>",
                                parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(text, video_chat)

    elif message.text == "Про психолога":
        text = bot.send_message(message.chat.id, f"<b>{data_ps()[id_ps]['O_PS']}</b>", parse_mode="html")
        bot.register_next_step_handler(text, menu)

    elif message.text == "Відгук":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        but = types.KeyboardButton("Назад")
        markup.add(but)
        text = bot.send_message(message.chat.id, '<b>Напишіть будь-ласка про ваші враження, '
                                                 'та оцініть роботу психолога</b>', parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(text, rep)


    print(data_open())
    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")

def chat(message):
    if message.text.lower() == "так":
        user_data = data_open()
        user_data[str(message.from_user.id)]["chat"] = True
        data_save(user_data)
        bot.send_message(id_ps, f"<b>Студент {data_open()[str(message.from_user.id)]['Імя']} відправив заявку на "
                                    f"чат-консультацію</b>", parse_mode='html')
        text = bot.send_message(message.chat.id, "<b>Психолог невдовзі зв'яжеться з вами</b>",
                                parse_mode='html', reply_markup=main_menu())
        bot.register_next_step_handler(text, menu)
    elif message.text.lower() == 'ні':
        text = bot.send_message(message.chat.id, "<b>Вітаємо в меню</b>", parse_mode='html', reply_markup=main_menu())
        bot.register_next_step_handler(text, menu)
    else:
        text = bot.send_message(message.chat.id, "Упс. Щось пішло не так. Виберіть будь-ласка кнопку")
        bot.register_next_step_handler(text, chat)
    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")

def video_chat(message):
    if message.text.lower() == "так":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        b = types.KeyboardButton("Назад")
        markup.add(b)
        text = bot.send_message(message.chat.id, "Напишіть дату та час коли ви бажаєте провести відео конференцію у форматі '01.01 20:00'", reply_markup=markup)
        bot.register_next_step_handler(text, conf)

    elif message.text.lower() == 'ні':
        text = bot.send_message(message.chat.id, "<b>Вітаємо в меню</b>", parse_mode='html', reply_markup=main_menu())
        bot.register_next_step_handler(text, menu)
    else:
        text = bot.send_message(message.chat.id, "Упс. Щось пішло не так. Виберіть будь-ласка кнопку")
        bot.register_next_step_handler(text, chat)
    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")

def conf(message):
    t = message.text
    if message.text == 'Назад':
        text = bot.send_message(message.chat.id, "<b>Вітаємо в меню</b>", parse_mode='html', reply_markup=main_menu())
        bot.register_next_step_handler(text, menu)
    elif len(t) < 11:
        text = bot.send_message(message.chat.id, "<b>Не вірний формат, введіть ще раз\nФормат: '01.01 20:00'</b>",
                                parse_mode='html')
        bot.register_next_step_handler(text, conf)
    elif not t[0].isdigit() or not t[1].isdigit() or t[2] != "." or not t[3].isdigit() or not t[4].isdigit() or not t[6].isdigit() or not t[7].isdigit() or t[8] != ":" or not t[9].isdigit() or not t[10].isdigit() or int(t[0])>3 or int(t[3])>1 or (int(t[3])==1 and  int(t[4])>2) or int(t[6])>2 or (int(t[6])==2 and  int(t[7])>4) or int(t[9])>6:
        text = bot.send_message(message.chat.id, "<b>Не вірний формат, введіть ще раз\nФормат: '01.01 20:00'</b>",
                                    parse_mode='html')
        bot.register_next_step_handler(text, conf)
    else:
        user_data = data_open()
        user_data[str(message.from_user.id)]["video_chat"] = message.text
        data_save(user_data)
        text = bot.send_message(message.chat.id, "<b>Введіть будь-ласка свій номер телефону у форматі '+380XXXXXXXXX'</b>", parse_mode="html")
        bot.register_next_step_handler(text, conf_num)

def conf_num(message):
    if message.text == 'Назад':
        text = bot.send_message(message.chat.id, "<b>Вітаємо в меню</b>", parse_mode='html', reply_markup=main_menu())
        bot.register_next_step_handler(text, menu)
    elif len(message.text) != 13:
        text = bot.send_message(message.chat.id, "<b>Не вірний формат, введіть ще раз\nФормат: '+380XXXXXXXXX'</b>",
                                parse_mode='html')
        bot.register_next_step_handler(text, conf_num)

    elif message.text[0] == "+":
        if message.text[1:].isdigit():
            bot.send_message(id_ps, f"<b>Студент {data_open()[str(message.from_user.id)]['Імя']} відправив заявку на "
                                    f"відео-консультацію о {data_open()[str(message.from_user.id)]['video_chat']}</b>",
                             parse_mode='html')
            text = bot.send_message(message.chat.id, "<b>Психолог зв'яжеться з вами у зазначений час</b>",
                                    parse_mode='html', reply_markup=main_menu())
            user_data = data_open()
            user_data[str(message.from_user.id)]["Номер"] = message.text
            data_save(user_data)
            bot.register_next_step_handler(text, menu)
        else:
            text = bot.send_message(message.chat.id,
                                    "<b>Не вірний формат, введіть ще раз\nФормат: '+380XXXXXXXXX'</b>",
                                    parse_mode='html')
            bot.register_next_step_handler(text, conf_num)



def q1(message):
    q = "1.Протягом останніх двох тижнів, як часто ви почувалися знервовано, тривожно або на межі?"
    user_data[str(message.from_user.id)]["Опитування"].update({q:message.text})
    text = bot.send_message(message.chat.id, "<b>2.Протягом останніх двох тижнів, як часто ви не могли позбавитись "
                                             "або контролювати хвилювання</b>", parse_mode="html")
    bot.register_next_step_handler(text, q2)
    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")

def q2(message):
    q = "2.Протягом останніх двох тижнів, як часто ви не могли позбавитись або контролювати хвилювання?"
    user_data[str(message.from_user.id)]["Опитування"].update({q: message.text})
    text = bot.send_message(message.chat.id, "<b>3.Протягом останніх двох тижнів, як часто ви xвилювалися надто сильно "
                                             "про різні речі</b>", parse_mode="html")
    bot.register_next_step_handler(text, q3)
    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")

def q3(message):
    q = "3.Протягом останніх двох тижнів, як часто ви xвилювалися надто сильно про різні речі"
    user_data[str(message.from_user.id)]["Опитування"].update({q: message.text})
    text = bot.send_message(message.chat.id, "<b>4.Протягом останніх двох тижнів, як часто "
                                             "вам було складно розслабитись</b>", parse_mode="html")
    bot.register_next_step_handler(text, q4)
    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")

def q4(message):
    q = "4.Протягом останніх двох тижнів, як часто вам було складно розслабитись"
    user_data[str(message.from_user.id)]["Опитування"].update({q: message.text})
    text = bot.send_message(message.chat.id, "<b>5.Протягом останніх двох тижнів, як часто були неспокійні настільки, "
                                             "що не могли всидіти на місці</b>", parse_mode="html")
    bot.register_next_step_handler(text, q5)
    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")

def q5(message):
    q = "5.Протягом останніх двох тижнів, як часто були неспокійні настільки, що не могли всидіти на місці"
    user_data[str(message.from_user.id)]["Опитування"].update({q: message.text})
    text = bot.send_message(message.chat.id, "<b>6.Протягом останніх двох тижнів, як часто "
                                             "легко дратувалися чи нервувалися</b>", parse_mode="html")
    bot.register_next_step_handler(text, q6)
    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")

def q6(message):
    q = "6.Протягом останніх двох тижнів, як часто легко дратувалися чи нервувалися"
    user_data[str(message.from_user.id)]["Опитування"].update({q: message.text})
    text = bot.send_message(message.chat.id, "<b>7.Протягом останніх двох тижнів, як часто "
                                             "відчували страх, що може статися щось жахливе</b>", parse_mode="html")
    bot.register_next_step_handler(text, q7)
    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")

def q7(message):
    q = "7.Протягом останніх двох тижнів, як часто відчували страх, що може статися щось жахливе"
    user_data[str(message.from_user.id)]["Опитування"].update({q: message.text})
    data = data_open()
    data.update(user_data)
    data_save(data)
    text = bot.send_message(message.chat.id, "<b>Дякуємо за ваші відповіді</b>", parse_mode='html',
                            reply_markup=main_menu())
    bot.register_next_step_handler(text, menu)
    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")

def rep(message):
    if message.text == 'Назад':
        text = bot.send_message(message.chat.id, "<b>Вітаємо в меню</b>", parse_mode='html', reply_markup=main_menu())
        bot.register_next_step_handler(text, menu)
    else:
        data = data_open()
        data[str(message.from_user.id)].update({"Відгук":message.text})
        data_save(data)
        bot.send_message(id_ps, "<b>Вам залишили відгук</b>", parse_mode='html')
        text = bot.send_message(message.chat.id, "<b>Дякуємо за відгук</b>", parse_mode='html', reply_markup=main_menu())
        bot.register_next_step_handler(text, menu)
    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")


########################## PS ####################################
def password(message):
    try:
        if message.text == 'Вихід':
            starting(message)
        elif message.text != data_ps()[str(message.from_user.id)]["login"]:
            text = bot.send_message(message.chat.id, "<b>Не вірний логін\nВведіль логін:</b>", parse_mode="html")
            bot.register_next_step_handler(text, password)
        else:
            text = bot.send_message(message.chat.id, "<b>Введіть пароль:</b>", parse_mode="html")
            bot.register_next_step_handler(text, fin_reg_ps)
    except:
        bot.send_message(message.chat.id, "<b>Нажаль ви не можете здійснити вхід</b>", parse_mode="html")
        starting(message)
    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")

def fin_reg_ps(message):
    if message.text == 'Вихід':
        starting(message)
    elif message.text != data_ps()[str(message.from_user.id)]["password"]:
        text = bot.send_message(message.chat.id, "<b>Не вірний пароль\nВведіль логін:</b>", parse_mode="html")
        bot.register_next_step_handler(text, password)
    else:
        text = bot.send_message(message.chat.id, "<b>Ви успішно авторизовані</b>", parse_mode='html',
                                reply_markup=markup_ps())
        bot.register_next_step_handler(text, menu_ps)
    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")

def menu_ps(message):
    if message.text == 'Вихід':
        starting(message)
    elif message.text == 'Відгуки':
        try:
            text = ""
            for x in data_open():
                text += f"<b>{data_open()[x]['Імя']}: {data_open()[x]['Відгук']}</b>\n"
            text = bot.send_message(message.chat.id, text, parse_mode='html')
            bot.register_next_step_handler(text, menu_ps)
        except:
            text = bot.send_message(message.chat.id, "<b>Відгуків ще немає</b>", parse_mode='html')
            bot.register_next_step_handler(text, menu_ps)

    elif message.text == 'Про психолога':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        but = types.KeyboardButton("Назад")
        markup.add(but)
        text = bot.send_message(message.chat.id, f"<b>Напишіть будь-ласка, що ви бажаєте аби користувачі "
                                                 f"узнали про вас.\nВи завжди можете це змінити.\nНа даний момент "
                                                 f"користувачі бачать: {data_ps()[str(message.from_user.id)]['O_PS']}"
                                                 f"</b>", parse_mode='html',
                                reply_markup=markup)
        bot.register_next_step_handler(text, o_ps)

    elif message.text == "Підтримка через чат":
        data = data_open()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        for x in data:
            if data[x]["chat"] == True:
                but = types.KeyboardButton(f"{data[x]['Імя']}")
                markup.add(but)
        but = types.KeyboardButton("Назад")
        markup.add(but)
        text = bot.send_message(message.chat.id, "Виберіть клієнта", reply_markup=markup)
        bot.register_next_step_handler(text, text_chat)

    elif message.text == "Підтримка через відео зв’язок":
        data = data_open()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        for x in data:
            if data[x]["video_chat"] != False:
                but = types.KeyboardButton(f"{data[x]['Імя']}")
                markup.add(but)
        but = types.KeyboardButton("Назад")
        markup.add(but)
        text = bot.send_message(message.chat.id, "Виберіть клієнта", reply_markup=markup)
        bot.register_next_step_handler(text, text_chat_2)


    else:
        text = bot.send_message(message.chat.id, "<b>Я тебе не розумію</b>", parse_mode='html')
        bot.register_next_step_handler(text, menu_ps)

    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")


def o_ps(message):
    if message.text == "Назад":
        text = bot.send_message(message.chat.id, "<b>Вітаємо в меню</b>", parse_mode='html', reply_markup=markup_ps())
        bot.register_next_step_handler(text, menu_ps)
    else:
        data = data_ps()
        data[str(message.from_user.id)].update({"O_PS": message.text})
        text = bot.send_message(message.chat.id, "<b>Дані успішно змінено</b>", parse_mode='html', reply_markup=markup_ps())
        bot.register_next_step_handler(text, menu_ps)
        save_ps(data)
    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")

def text_chat(message):
    print(message.text)
    global text_chat_user_data, id
    if message.text == "Назад":
        text = bot.send_message(message.chat.id, "<b>Вітаємо в меню</b>", parse_mode='html', reply_markup=markup_ps())
        bot.register_next_step_handler(text, menu_ps)
    elif message.text == "Дані про клієнта":
        text = bot.send_message(message.chat.id, f"<b>Імя: {text_chat_user_data['Імя']}\n"
                                                 f"Вік: {text_chat_user_data['Вік']}\n"
                                                 f"Група: {text_chat_user_data['Група']}\n"
                                                 f"Курс: {text_chat_user_data['Курс']}\n"
                                                 f"Стать: {text_chat_user_data['Стать']}</b>", parse_mode='html')
        bot.register_next_step_handler(text, text_chat)
    elif message.text == "Результати опитування":
        t = ""
        for k, v in text_chat_user_data["Опитування"].items():
            t += f"<b>{k}: {v}</b>\n"
        text = bot.send_message(message.chat.id, t, parse_mode='html')
        bot.register_next_step_handler(text, text_chat)
    elif message.text == "Начати чат":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        but = types.KeyboardButton("Закрити чат")
        markup.add(but)
        bot.send_message(message.chat.id, "<b>Всі наступні повідомлення будуть відправлятися клієнту, "
                                                 "допоки ви не закриєте чат</b>", parse_mode="html",
                                reply_markup=markup)
        bot.send_message(id, "Психолог на зв'язку")
        data = data_open()
        data[str(id)]['in_chat'] = True
        data_save(data)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        but_1 = types.KeyboardButton("Дані про клієнта")
        but_2 = types.KeyboardButton("Результати опитування")
        but_3 = types.KeyboardButton("Начати чат")
        but_4 = types.KeyboardButton("Назад")
        markup.add(but_1, but_2, but_3, but_4)
        text = bot.send_message(message.chat.id, "<b>Узнайте детальніше про клієнта перед тим як зв'язатися з ним</b>",
                                parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(text, text_chat)
        for x in data_open():
            if data_open()[x]['Імя'] == message.text:
                text_chat_user_data = data_open()[x]
                id = x
                break
    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")

def text_chat_2(message):
    global text_chat_user_data, id
    if message.text == "Назад":
        text = bot.send_message(message.chat.id, "<b>Вітаємо в меню</b>", parse_mode='html', reply_markup=markup_ps())
        bot.register_next_step_handler(text, menu_ps)
    elif message.text == "Дані про клієнта":
        text = bot.send_message(message.chat.id, f"<b>Імя: {text_chat_user_data['Імя']}\n"
                                                 f"Вік: {text_chat_user_data['Вік']}\n"
                                                 f"Група: {text_chat_user_data['Група']}\n"
                                                 f"Курс: {text_chat_user_data['Курс']}\n"
                                                 f"Стать: {text_chat_user_data['Стать']}</b>", parse_mode='html')
        bot.register_next_step_handler(text, text_chat_2)
    elif message.text == "Результати опитування":
        t = ""
        for k, v in text_chat_user_data["Опитування"].items():
            t += f"<b>{k}: {v}</b>\n"
        text = bot.send_message(message.chat.id, t, parse_mode='html')
        bot.register_next_step_handler(text, text_chat_2)
    elif message.text == "Номер телефону":
        text = bot.send_message(message.chat.id, f"{text_chat_user_data['Номер']}\nЗв'язок запланований на {text_chat_user_data['video_chat']}")
        bot.register_next_step_handler(text, text_chat_2)
    elif message.text == "Закрити замовлення":
        data = data_open()
        data[str(id)]['video_chat'] = False
        data_save(data)
        text = bot.send_message(message.chat.id, "Замовлення закрите", reply_markup=markup_ps())
        bot.register_next_step_handler(text, menu_ps)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        but_1 = types.KeyboardButton("Дані про клієнта")
        but_2 = types.KeyboardButton("Результати опитування")
        but_3 = types.KeyboardButton("Номер телефону")
        but_4 = types.KeyboardButton("Закрити замовлення")
        but_5 = types.KeyboardButton("Назад")
        markup.add(but_1, but_2, but_3, but_4, but_5)
        text = bot.send_message(message.chat.id, "<b>Узнайте детальніше про клієнта перед тим як зв'язатися з ним</b>",
                                parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(text, text_chat_2)
        for x in data_open():
            if data_open()[x]['Імя'] == message.text:
                text_chat_user_data = data_open()[x]
                id = x
                break
    print(f"{datetime.datetime.now()}: {message.from_user.id}, {message.text}")

@bot.message_handler()
def mes(message):
    global id
    try:
        if message.text == "Вихід" or message.text == "Назад":
            starting(message)
        elif message.text == "Закрити чат":
            text = bot.send_message(message.chat.id, "Чат закритий", reply_markup=markup_ps())
            text_2 = bot.send_message(id, "Ласкаво просимо в меню")
            bot.send_message(id, "Психолог закрив чат")
            data = data_open()
            data[str(id)]['in_chat'] = False
            data[str(id)]['chat'] = False
            data_save(data)
            bot.register_next_step_handler(text_2, menu)
            print("Закрив чат юзера")
            bot.register_next_step_handler(text, menu_ps)
            print("Закрив чат психолога")
            id = 0
        elif str(message.from_user.id) == id_ps:
            bot.send_message(id, message.text)
        elif str(message.from_user.id) == id and data_open()[str(message.from_user.id)]['in_chat'] == True:
            bot.send_message(id_ps, message.text)
        elif data_open()[str(message.from_user.id)]['in_chat'] == False:
            text = bot.send_message(message.chat.id, "Ласкаво просимо в меню")
            bot.register_next_step_handler(text, menu)
            print("Зараз я тут")
        elif message.text == 'data.json':
            text = bot.send_message(message.chat.id, f"{data_open()}")
            bot.register_next_step_handler(text, menu)
            print(data_open())
    except:
        pass


bot.polling(none_stop=True, timeout=1)
