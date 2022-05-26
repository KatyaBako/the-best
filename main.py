import telebot  # импортирую библиотеку
from telebot import types  # types импортируем для создания кнопок-ссылок

bot = telebot.TeleBot('5379026642:AAHiwq5a6esIdIqr1FSjNW1UwTpXoqJKOmY')  # устанавливаем API ключ


@bot.message_handler(commands=['start'])  # отслеживание команды 'start' и 'info'
def start(message):
    """"
    function used for tracking commands start and info
    commands: what commands we are going to track
    start, info: commands we are tracking
    types: imported buttons with links
    InlineKeyboardMarkup: choose the format of marking
    InlineKeyboardButton: making buttons
    markup.add: adding buttons
    bot.send_message: message the bot will send to the user
    text: words that will be written on the buttons
    callback_data: what will these words return
    parse_mode: sets the conditions parse for the bot's messages
    reply_markup=markup: attach the keyboard to the message
    :param message:
    """
    markup = types.InlineKeyboardMarkup()  # Добавляем интерактивные кнопки
    btn1 = types.InlineKeyboardButton(text='ШКОЛА ШПАГАТА', callback_data='stretching')
    btn2 = types.InlineKeyboardButton(text='AEROSTRETCHING', callback_data='aero')
    btn3 = types.InlineKeyboardButton(text='STRIP DANCE', callback_data='strip')
    btn4 = types.InlineKeyboardButton(text='TXR', callback_data='txr')
    btn5 = types.InlineKeyboardButton(text='BODY BALLET', callback_data='ballet')
    btn6 = types.InlineKeyboardButton(text='TOP BODY', callback_data='top')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    send_mess = f"Здравствуйте, <b>{message.from_user.first_name}</b>!\nКакое направление вас интересует?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    """"
    function take anonymous func lambda returning True
    call: what is returned when one of the buttons are clicked
    resize_keyboard=True: it makes the buttons smaller
    text: words that will be written on the buttons
    ReplyKeyBoardMarkup: choose the format of making buttons(buttons located at the bottom)
    KeyBoardButtons: create buttons
    markup.add: adding buttons
    bot.send_message: message the bot will send to the user
    parse_mode: sets the conditions parse for the bot's messages
    reply_markup=markup: attach the keyboard to the message
    """
    if call.data == 'stretching':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Как будут проходить занятия и какую пользу я смогу получить?')
        btn2 = types.KeyboardButton(text='Посмотреть расписание')
        btn3 = types.KeyboardButton(text='Абонементы')
        markup.add(btn1, btn2, btn3)
        final_mess = "Что бы вы хотели узнать о выбранном направлении?"
        bot.send_message(call.message.chat.id, final_mess, parse_mode='html', reply_markup=markup)
    elif call.data == 'aero':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton(text='Что это такое?')
        btn2 = types.KeyboardButton(text='Посмотреть расписание')
        btn3 = types.KeyboardButton(text='Абонементы')
        markup.add(btn1, btn2, btn3)
        final_mess = "Что бы вы хотели узнать о выбранном направлении?"
        bot.send_message(call.message.chat.id, final_mess, parse_mode='html', reply_markup=markup)
    elif call.data == 'strip':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton(text='Посмотреть расписание')
        btn2 = types.KeyboardButton(text='Абонементы')
        btn3 = types.KeyboardButton(text='Stripdance - это стриптиз??')
        markup.add(btn1, btn2, btn3)
        final_mess = "Что бы вы хотели узнать о выбранном направлении??"
        bot.send_message(call.message.chat.id, final_mess, parse_mode='html', reply_markup=markup)
    elif call.data == 'txr':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton(text='Посмотреть расписание')
        btn2 = types.KeyboardButton(text='Абонементы')
        btn3 = types.KeyboardButton(text='Кому подходит и для чего необходимы тренировки?')
        markup.add(btn1, btn2, btn3)
        final_mess = "Что бы вы хотели узнать о выбранном направлении?"
        bot.send_message(call.message.chat.id, final_mess, parse_mode='html', reply_markup=markup)
    elif call.data == 'ballet':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton(text='Посмотреть расписание')
        btn2 = types.KeyboardButton(text='Абонементы')
        btn3 = types.KeyboardButton(text='Чему я смогу научиться?')
        markup.add(btn1, btn2, btn3)
        final_mess = "Что бы вы хотели узнать о выбранном направлении?"
        bot.send_message(call.message.chat.id, final_mess, parse_mode='html', reply_markup=markup)
    elif call.data == 'top':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton(text='Посмотреть расписание')
        btn2 = types.KeyboardButton(text='Абонементы')
        btn3 = types.KeyboardButton(text='Кому подойдут занятия?')
        markup.add(btn1, btn2, btn3)
        final_mess = "Что бы вы хотели узнать о выбранном направлении?"
        bot.send_message(call.message.chat.id, final_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])   # отслеживаем определенный текст от пользователя
def get_text(message, photo=None):
    """
    message: the text that our user will write or choose
    photo: the picture that the user will see after inserting text
    parse_mode: sets the conditions parse for the bot's messages
    reply_markup=markup: attach the keyboard to the message
    bot.send_message: the message the bot will send to the user
    """
    if message.text == 'Посмотреть расписание':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Расписание занятий",
                                              url="https://topstretching.by/schedule"))
        bot.send_message(message.chat.id, "расписание", parse_mode='html', reply_markup=markup)
    elif message.text == 'Абонементы':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Наши абонементы",
                                              url="https://topstretching.by/trial"))
        bot.send_message(message.chat.id, "абонементы", parse_mode='html', reply_markup=markup)
    elif message.text == 'Как будут проходить занятия и какую пользу я смогу получить?':
        # photo = open('photo.jpg', 'rb')
        # bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,
                         "<b>Школа шпагата-это</b> комплекс упражнений, направленный на развитие гибкости и растяжки. "
                         "Польза стретчинга неоспорима, ведь он помогает:\n- подтянуть тело\n - смоделировать мышечный "
                         "корсет\n - улучшить осанку и координацию\n - развить гибкость\n - продлить молодость тела\n "
                         "- улучшить кровообращение и обмен веществ\nКроме того, занятия стретчингом "
                         "<b>поднимают настроение, дарят бодрость духа, помогают бороться со стрессом"
                         " и напряжением</b>", parse_mode='html')
    elif message.text == 'Что это такое?':
        # video = open('moji.gif', 'rb')
        # bot.send_video_note(message.chat.id, video)
        bot.send_message(message.chat.id, "<b>AEROSTRETCHING - это</b> система упражнений для растяжки связок и мышц с "
                                          "подвешиванием тела в гамаке. Вместо кардио и силовых упражнений здесь – "
                                          "растяжка и укрепление мышц, связок и суставов. Занятие проходит не на полу, "
                                          "а в невесомости – это <b>снимает нагрузку с позвоночника</b>, а вместе с тем "
                                          "и <b>избавляет от зажимов, развивает координацию.</b>", parse_mode='html')
    elif message.text == 'Stripdance - это стриптиз??':
        # photo = open('strip.jpg', 'rb')
        # bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,
                         "Не путать со стриптизом! Раздеваться вам не придется (по крайней мере, на занятиях, "
                         "а там уж, как пожелаете).Стрип пластика — одно из направлений, которое предлагает наша студия."
                         " Выглядеть сексуально и соблазнительно: какая женщина об этом не мечтает?! "
                         "А чтобы стать роковой красавицей, просто необходимо красиво двигаться. "
                         "Научиться обольщать каждым движением можно, освоив Strip dance!", parse_mode='html')
    elif message.text == 'Кому подходит и для чего необходимы тренировки?':
        # photo = open('txr.jpg', 'rb')
        # bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, "Тренировки с использованием веса собственного тела <b>TRX Suspension "
                                          "Training - одна из новейших тенденций фитнес-индустрии</b>, о которой всего "
                                          "пару лет назад никто даже не слышал.Упражнения на TRX лежат в основе "
                                          "программы TRX Suspension Training – эффективной методики функционального "
                                          "тренинга с использованием собственного веса для проработки мышц всего тела."
                                          " Занятия на тренажере TRX подходят для людей с любым уровнем физической "
                                          "подготовки и эффективно <u>способствуют развитию силы, выносливости, гибкости"
                                          " и равновесия.</u>", parse_mode='html')
    elif message.text == 'Чему я смогу научиться?':
        # photo = open('ballet.jpg', 'rb')
        # bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, "<b>Bodyballet - самое нежное направление нашей студии.</b> Вы узнаете на "
                                          "занятиях,что такое арабеск, познакомитесь с позициями рук, научитесь "
                                          "правильному плие. Уже на первом занятии Вы поймете, насколько это доступно "
                                          "для Вас!", parse_mode='html')
    elif message.text == 'Кому подойдут занятия?':
        # photo = open('top.jpg', 'rb')
        # bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, "<b>Topbody</b> - тренировочный комплекс для прокачки ягодиц и всего тела с "
                                          "помощью резинок.", parse_mode='html')

    elif message.text == 'website':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посетите наш сайт", url="https://taplink.cc/topstretching.minsk"))
        bot.send_message(message.chat.id, "Нажмите на кнопку снизу", parse_mode='html', reply_markup=markup)
    elif message.text == 'instagram':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посетите наш инстаграм",
                                              url="https://instagram.com/topstretching.minsk?igshid=YmMyMTA2M2Y="))
        bot.send_message(message.chat.id, "Нажмите на кнопку ниже", parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)
