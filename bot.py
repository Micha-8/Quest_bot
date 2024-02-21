from game import (
    classes_show, choice_your_character, make_keyboard, send_question, check_first_answer,
    send_aftereffect_room_answer, add_variants_for_second_answer, send_aftereffect_cell_answer,
    add_variants_for_fourth_answer,
    send_aftereffect_door_answer, send_aftereffect_helpers_answer,
    get_answers_in_answers_and_aftereffects,
    send_aftereffect_final_answer, check_user_character, send_photo
)
from info import say_start, rules, storyline, commands, Cool_sticker, Not_understand_media, Not_understand_text
from data import save_user_data, data_path, user_data
import telebot
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('token')
bot = telebot.TeleBot(token)

main_markup = make_keyboard(list(commands.keys()))
help_commands_send = '\n'.join(commands.values())


def filter_hello(message):
    return 'привет' in message.text.lower()


def filter_bye(message):
    return 'пока' in message.text.lower()


@bot.message_handler(commands=['start'])
def handle_start(message):
    global user_data
    user_data[message.chat.id] = {
        'name': message.from_user.first_name,
        'id': message.from_user.id,
        'location': ''}  # хотел еще персонажа грузить, но как бы не пробовал не получалось
    save_user_data(user_data, data_path)

    bot.send_message(
        message.chat.id,
        f'<b>Привет, {message.chat.first_name}!</b>\n\n'
        f'{say_start}',
        parse_mode='HTML',
        reply_markup=main_markup)


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, f'<b>Список команд:</b>\n'
                                      f'{help_commands_send}',
                     parse_mode='HTML',
                     reply_markup=main_markup
                     )


@bot.message_handler(commands=['quest_rules'])
def handle_help(message):
    bot.send_message(message.chat.id, f'{rules}',
                     parse_mode='HTML',
                     reply_markup=main_markup
                     )


@bot.message_handler(commands=['choise_character'])
def handle_choise(message):
    classes_show(bot, message)
    bot.register_next_step_handler(message, character_choicen)


def character_choicen(message):
    try:
        global user_character  # знаю что глобал это не оч, но как без него здесь обойтись не знаю
        # ну можно вынести эту команду в сам квест, но я хочу ее отдельно
        user_character = choice_your_character(message)
        bot.send_message(message.chat.id, f'<b>Твой персонаж: {user_character.name}</b>\n'
                                          f'Его атрибуты: \n'
                                          f'Ловкость: {user_character.agility}\n'
                                          f'Сила: {user_character.strength}\n'
                                          f'Интеллект: {user_character.intellect}\n',
                         parse_mode='HTML',
                         reply_markup=main_markup
                         )
        user_data[message.chat.id] = {
            'name': message.from_user.first_name,
            'id': message.from_user.id,
            'location': ''}
        save_user_data(user_data, data_path)
    except UnboundLocalError:
        bot.send_message(message.chat.id, 'Выбери существующего персонажа ',
                         parse_mode="HTML",
                         reply_markup=main_markup)


@bot.message_handler(commands=['start_quest'])
def check_user_start(message):
    try:
        check_user_character(message, user_character, error_func, handle_start_quest)
    except:
        bot.send_message(message.chat.id, 'Сначала выбери персонажа',
                         parse_mode='HTML',
                         reply_markup=main_markup
                         )


def handle_start_quest(message):
    send_photo(bot, message, 'game_media/cell.photo.jpg')
    markup = make_keyboard(storyline['1']['answers'].values())
    send_question(bot, message, '1', markup)

    user_data[message.chat.id] = {
        'name': message.from_user.first_name,
        'id': message.from_user.id,
        'location': 'cell'}
    save_user_data(user_data, data_path)
    bot.register_next_step_handler(message, cell_find)


def cell_find(message):
    check_first_answer(bot, message, user_character, deal_with_the_guard, error_func)


def deal_with_the_guard(message):
    markup_names = []
    add_variants_for_second_answer(user_character, markup_names)
    markup = make_keyboard(markup_names)
    send_question(bot, message, '2', markup)
    bot.register_next_step_handler(message, win_guard_send)


def win_guard_send(message):
    send_aftereffect_cell_answer(bot, message, error_func, in_house)


def in_house(message):
    markup_names = get_answers_in_answers_and_aftereffects('3')
    markup = make_keyboard(markup_names)
    send_question(bot, message, '3', markup)

    user_data[message.chat.id] = {
        'name': message.from_user.first_name,
        'id': message.from_user.id,
        'location': 'house'}
    save_user_data(user_data, data_path)
    bot.register_next_step_handler(message, which_room_you_go_check)


def which_room_you_go_check(message):
    send_aftereffect_room_answer(bot, message, user_character, error_func, near_the_door)


def near_the_door(message):
    markup_names = []
    add_variants_for_fourth_answer(user_character, markup_names)
    markup = make_keyboard(markup_names)
    send_question(bot, message, '4', markup)
    bot.register_next_step_handler(message, after_door_check)


# не объединяю эти функции тк если пользователь введёт что-то не то, след вопрос не выводится
def after_door_check(message):
    send_aftereffect_door_answer(bot, message, main_markup, error_func, in_forest)


def in_forest(message):
    markup_names = get_answers_in_answers_and_aftereffects('5')
    markup = make_keyboard(markup_names)
    send_question(bot, message, '5', markup)
    user_data[message.chat.id] = {
        'name': message.from_user.first_name,
        'id': message.from_user.id,
        'location': 'forest'}
    bot.register_next_step_handler(message, which_helper_you_go)


def which_helper_you_go(message):
    send_aftereffect_helpers_answer(bot, message, user_character, error_func, last_fight)


def last_fight(message):
    markup_names = get_answers_in_answers_and_aftereffects('6')
    markup = make_keyboard(markup_names)
    send_question(bot, message, '6', markup)
    bot.register_next_step_handler(message, end_of_game)


def end_of_game(message):
    send_aftereffect_final_answer(bot, message, user_character, error_func)
    bot.send_message(message.chat.id, 'Это конец игры, спасибо за прохождение',
                     parse_mode='HTML',
                     reply_markup=main_markup
                     )


def error_func(message):
    bot.send_message(message.chat.id, 'Внимательно изучи правила.\n'
                                      'Ты сделал что-то не так',
                     parse_mode='HTML',
                     reply_markup=main_markup
                     )


@bot.message_handler(content_types=['text'], func=filter_hello)
def say_hello(message):
    bot.send_message(message.chat.id, 'Привет!',
                     reply_markup=main_markup)


@bot.message_handler(content_types=['text'], func=filter_bye)
def say_goodbye(message):
    bot.send_message(message.chat.id, 'До свидания!',
                     reply_markup=main_markup)


@bot.message_handler(content_types=['sticker'])
def sticker_answer(message):
    bot.send_message(message.chat.id, f'{Cool_sticker}',
                     reply_markup=main_markup)


@bot.message_handler(content_types=['text'])
def text_answer(message):
    bot.send_message(message.chat.id,
                     f'{Not_understand_text}',
                     reply_markup=main_markup)


@bot.message_handler(content_types=['audio', 'video', 'voice', 'photo', 'document'])
def media_answer(message):
    bot.send_message(message.chat.id, f'{Not_understand_media}',
                     reply_markup=main_markup)


bot.infinity_polling()
