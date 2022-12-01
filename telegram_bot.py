import random
import time

import conf
import telebot
from telebot import types


bot = telebot.TeleBot(conf.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_welcome = types.KeyboardButton('Привет, Бадди! Приятно познакомиться)')

    markup.add(button_welcome)

    bot.send_message(message.chat.id, "Привет, <b>{0.first_name}!</b>\nМеня зовут Бадди, я твой цифровой психолог.".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_message(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('да, здорово 😊')

    markup.add(button)

    if message.chat.type == 'private':
        if message.text == 'Привет, Бадди! Приятно познакомиться)':

            bot.send_message(message.chat.id, 'Я задам тебе несколько вопросов о том, как ты себя чувствуешь.\n'
                                              'Мы вернемся к ним по завершению процесса, чтобы посмотреть, что измениться.'.format(message.from_user, bot.get_me()),
                             parse_mode='html', reply_markup=markup)

    if message.chat.type == 'private':
        if message.text == 'да, здорово 😊':

            markup2 = types.InlineKeyboardMarkup(row_width=2)
            button_yes = types.InlineKeyboardButton("Да", callback_data='yes')
            button_no = types.InlineKeyboardButton("Нет", callback_data='no')

            markup2.add(button_yes, button_no)

            bot.send_message(message.chat.id, 'Я чувствую себя эмоционально опустошенным.', reply_markup=markup2)
            time.sleep(5)
            bot.send_message(message.chat.id, 'После работы я чувствую себя как «выжатый лимон».', reply_markup=markup2)
            time.sleep(5)
            bot.send_message(message.chat.id, 'Утром я чувствую усталость и нежелание идти на работу.', reply_markup=markup2)
            time.sleep(5)
            bot.send_message(message.chat.id, 'Я хорошо понимаю, что чувствуют мои подчиненные и коллеги, и стараюсь учитывать это в интересах дела.', reply_markup=markup2)
            time.sleep(5)
            bot.send_message(message.chat.id, 'Я чувствую, что общаюсь с некоторыми подчиненными и коллегами как с предметами (без теплоты и расположения к ним).', reply_markup=markup2)
            time.sleep(5)
            bot.send_message(message.chat.id, 'После работы на некоторое время хочется уединиться от всех и всего.', reply_markup=markup2)
            time.sleep(5)
            bot.send_message(message.chat.id, 'Я умею находить правильное решение в конфликтных ситуациях, возникающих при общении с коллегами.', reply_markup=markup2)
            time.sleep(5)
            bot.send_message(message.chat.id, 'Я чувствую угнетенность и апатию.', reply_markup=markup2)
            time.sleep(5)
            bot.send_message(message.chat.id, 'Я уверен, что моя работа нужна людям.', reply_markup=markup2)
            time.sleep(5)
            bot.send_message(message.chat.id, 'В последнее время я стал более «черствым» по отношению к тем, с кем работаю.', reply_markup=markup2)
            time.sleep(5)
            bot.send_message(message.chat.id, 'Я замечаю, что моя работа ожесточает меня.', reply_markup=markup2)


            markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button = types.KeyboardButton('Узнать результаты теста!')

            markup5.add(button)

            bot.send_message(message.chat.id, 'Нажми на кнопку, чтобы узнать результаты'.format(
                message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup5)


yes_list = []
no_list = []
answer = '*'


@bot.message_handler(content_types=['text'])
def get_results(message):

    if message.chat.type == 'private':
        if message.text == 'Узнать результаты теста!':

            bad_answer_list = [
                'Эмоциональное истощение рассматривается как основная составляющая выгорания и проявляется в '
                'переживаниях сниженного эмоционального тонуса, повышенной психической истощаемости'
                ' и аффективной лабильности, утраты интереса и позитивных чувств к окружающим, ощущении '
                '«пресыщенности» работой, неудовлетворенностью жизнью в целом.',

                'Деперсонализация проявляется в эмоциональном отстранении и безразличии, формальном выполнении '
                'профессиональных обязанностей без личностной включенности и сопереживания, а в отдельных случаях – '
                'в негативизме и циничном отношении. В контексте синдрома перегорания «деперсонализация» предполагает '
                'формирование особых, деструктивных взаимоотношений с окружающими людьми.',

                'Редукция профессиональных достижений отражает степень удовлетворенности человека собой как личностью '
                'и как профессионалом. Неудовлетворительное значение этого показателя отражает тенденцию к негативной оценке '
                'своей компетентности и продуктивности и, как следствие, – снижение профессиональной мотивации, нарастание '
                'негативизма в отношении служебных обязанностей, тенденцию к снятию с себя ответственности, к изоляции от '
                'окружающих, отстраненность и неучастие, избегание работы сначала психологически, а затем физически.'
            ]

            if len(yes_list) >= len(no_list):
                bot.send_message(message.chat.id, random.choice(bad_answer_list))

            good_anwer_list = [
                'Отдохните. Кто это ещё не слышал? Но что люди делают со своим отдыхом — они утыкаются в экран. '
                'Сериалы, соц. сети, ютюб — всё, что зачастую делает более дёрганным, а мозг уставшим. Учитесь отдыхать.'
                ' Отдохнуть, а не устать ещё больше можно лишь на том, что «обновляет» ваши эмоции, даёт вам ПРОЖИВАНИЕ '
                'чего-то свежего. Художественная литература, хорошие истории.',

                'Поддержка окружающих. Не всегда стоит сразу бежать к психологу. Как ни странно, люди редко делятся своим '
                'состоянием даже с самыми близкими людьми, считая это недостойным/показывающим их с плохой стороны. '
                'Попробуйте рассказать, какие у вас трудности внутри, с чем вы сталкиваетесь. Не жалуйтесь, попробуйте '
                'просто описать вашу ситуацию, эмоции, которые она у вас вызывает, будь вы сценаристом, который описывает '
                'внутренние состояния своих героев.',

                'Найдите то, что любите вы. Тоже вещь, которую люди игнорируют или отвечают «Да-да, все говорят найти хобби.'
                ' Ну вот я вяжу, отстаньте». Но ведь как важно в дне иметь 1-2 часа, когда вы не просто «тупите перед любимым '
                'сериалом», но занимаетесь вещью, которая, как сладость, которую вы вот-вот достанете из полки, вызывает у вас '
                'приливы эндорфинов. Подумайте хорошенько прямо сейчас, чем это может стать для вас? И делайте это хотя бы 30 '
                'минут в день.',

                'Посмотрите видео Франца Вертфоллена. Это видео смотрит в корень. Там вы не услышите всех слов о том, что вы '
                '«перетрудились», «вам нужно сменить деятельность», «вас угнетает начальник». В видео автор раскладывает механизмы, '
                'которыми могут пользоваться топ-менеджеры и СЕО компаний, чтобы не выгорать. Даёт вам инструменты и понимания, '
                'которые вы можете применить уже сегодня.'
            ]

            if len(no_list) >= len(yes_list):
                bot.send_message(message.chat.id,
                                 f'Все отлично! У вас хорошие результаты, но на всякий случай вот тебе совет как избежать эмоционального выгорания:'
                                 f'{random.choice(good_anwer_list)}')


@bot.callback_query_handler(func=lambda call: True)
def callback_buttons(call):
    try:
        if call.message:
            if call.data == 'yes':
                yes_list.append(answer)

            if call.data == 'no':
                no_list.append(answer)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Ответ принят',
                                  reply_markup=None)

    except Exception as e:
        print(repr(e))

    return f'{len(yes_list)} --- {no_list}'



bot.polling(none_stop=True)





