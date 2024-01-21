from info import characters, storyline
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import json

class CharactersStats:
    def __init__(self, intellect, agility, strength, name, description):
        self.intellect = intellect
        self.agility = agility
        self.strength = strength
        self.name = name
        self.description = description
        self.inventory = []

    def intellect_up(self, count_new_intellect: int) -> int:
        self.intellect = self.intellect + count_new_intellect

    def agility_up(self, count_new_agility: int) -> int:
        self.agility = self.agility + count_new_agility

    def strength_up(self, count_new_strength: int) -> int:
        self.strength = self.strength + count_new_strength

    def add_to_inventory(self, item: str):
        self.inventory.append(item)


bitter_knight = CharactersStats(1, 3, 5, f'{characters['bitter_knight']['name']}',
                                f'{characters['bitter_knight']['description']}')

a_brilliant_mind = CharactersStats(5, 2, 2, f'{characters['a_brilliant_mind']['name']}',
                                   f'{characters['a_brilliant_mind']['description']}')

child_of_thieves = CharactersStats(3, 5, 2, f'{characters['child_of_thieves']['name']}',
                                   f'{characters['child_of_thieves']['description']}')


def choice_your_character(message):
    if message.text == 'Гениальный Разум':
        user_character = CharactersStats(5, 2, 2, f'{characters['a_brilliant_mind']['name']}',
                                         f'{characters['a_brilliant_mind']['description']}')

    elif message.text == 'Печальный Рыцарь':
        user_character = CharactersStats(1, 3, 5, f'{characters['bitter_knight']['name']}',
                                         f'{characters['bitter_knight']['description']}')

    elif message.text == 'Дитя Воров':
        user_character = CharactersStats(3, 5, 2, f'{characters['child_of_thieves']['name']}',
                                         f'{characters['child_of_thieves']['description']}')

    return user_character


def get_names():
    return [char['name'] for char in characters.values()]  # эту функцию написал Ygpt


def get_answers_in_answers_and_aftereffects(num: str):
    answers = []
    for key, value in storyline[num]['answers_and_aftereffects'].items():
        answers.append(value['answer'])
    return answers


def make_keyboard(items):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for item in items:
        markup.add(KeyboardButton(item))
    return markup


def send_photo(bot, message, photo):
    with open(photo, 'rb') as f:
        bot.send_photo(message.chat.id, f)


def classes_show(bot, message):
    markup = make_keyboard(get_names())

    bot.send_message(message.chat.id, f'<b>Выбери своего персонажа:</b>',
                     parse_mode="HTML")

    bot.send_message(message.chat.id, f'<b>{bitter_knight.name}</b>\n'
                                      f'{bitter_knight.description}',
                     parse_mode="HTML")
    # бот выводит всех персонажей отдельно чтобы было красиво
    bot.send_message(message.chat.id, f'<b>{a_brilliant_mind.name}</b>\n'
                                      f'{a_brilliant_mind.description}',
                     parse_mode="HTML")

    bot.send_message(message.chat.id, f'<b>{child_of_thieves.name}</b>\n'
                                      f'{child_of_thieves.description}',
                     parse_mode="HTML",
                     reply_markup=markup)
    return message


def check_user_character(message, user_character, error_func, next_step):
    if user_character.strength > 5 or user_character.intellect > 5 or user_character.agility > 5 or user_character.inventory != []:
        error_func(message)
    else:
        next_step(message)


def send_question(bot, message, num_question: str, markup):
    bot.send_message(message.chat.id, f'{storyline[num_question]['question']}',
                     parse_mode="HTML",
                     reply_markup=markup)


def check_first_answer(bot, message, user_character, next_step, error_func):
    if message.text == storyline['1']['answers']['1']:
        bot.send_message(message.chat.id, 'Там ты находишь отмычку')
        user_character.add_to_inventory('picklock')
        next_step(message)

    elif message.text == storyline['1']['answers']['2']:
        bot.send_message(message.chat.id, 'Там ты ничего не находишь')
        next_step(message)

    elif message.text == storyline['1']['answers']['3']:
        bot.send_message(message.chat.id, 'Из кусочка стекла тебе удается сделать заточку')
        user_character.add_to_inventory('sharpening')
        next_step(message)

    else:
        error_func(message)


def add_variants_for_second_answer(user_character, markup):
    if user_character.strength >= 5 and 'sharpening' in user_character.inventory:
        markup.append(storyline['2']['answers_and_aftereffects']['1']['answer'])
    if 'picklock' in user_character.inventory:
        markup.append(storyline['2']['answers_and_aftereffects']['2']['answer'])
    if user_character.agility >= 3:
        markup.append(storyline['2']['answers_and_aftereffects']['3']['answer'])
    if user_character.intellect >= 3:
        markup.append(storyline['2']['answers_and_aftereffects']['4']['answer'])


def add_variants_for_fourth_answer(user_character, markup):
    if user_character.intellect >= 8:
        markup.append(storyline['4']['answers_and_aftereffects']['1']['answer'])
    if user_character.strength >= 10:
        markup.append(storyline['4']['answers_and_aftereffects']['2']['answer'])
    if user_character.agility >= 8 and 'picklock' in user_character.inventory:
        markup.append(storyline['4']['answers_and_aftereffects']['3']['answer'])
    markup.append((storyline['4']['answers_and_aftereffects']['4']['answer']))


def send_aftereffect_cell_answer(bot, message, error_func, next_step):
    if message.text == storyline['2']['answers_and_aftereffects']['1']['answer']:
        bot.send_message(message.chat.id, f'{storyline['2']['answers_and_aftereffects']['1']['aftereffect']}')
        next_step(message)

    elif message.text == storyline['2']['answers_and_aftereffects']['2']['answer']:
        bot.send_message(message.chat.id, f'{storyline['2']['answers_and_aftereffects']['2']['aftereffect']}')
        next_step(message)

    elif message.text == storyline['2']['answers_and_aftereffects']['3']['answer']:
        bot.send_message(message.chat.id, f'{storyline['2']['answers_and_aftereffects']['3']['aftereffect']}')
        next_step(message)

    elif message.text == storyline['2']['answers_and_aftereffects']['4']['answer']:
        bot.send_message(message.chat.id, f'{storyline['2']['answers_and_aftereffects']['4']['aftereffect']}')
        next_step(message)

    else:
        error_func(message)


def send_aftereffect_room_answer(bot, message, user_character, error_func, next_step):
    if message.text == storyline['3']['answers_and_aftereffects']['1']['answer']:
        send_photo(bot, message, 'game_media/library.jpg')
        bot.send_message(message.chat.id, f'{storyline['3']['answers_and_aftereffects']['1']['aftereffect']}')
        user_character.intellect_up(5)
        next_step(message)

    elif message.text == storyline['3']['answers_and_aftereffects']['2']['answer']:
        send_photo(bot, message, 'game_media/chest_find.jpg')
        bot.send_message(message.chat.id, f'{storyline['3']['answers_and_aftereffects']['2']['aftereffect']}')
        user_character.strength_up(5)
        next_step(message)

    elif message.text == storyline['3']['answers_and_aftereffects']['3']['answer']:
        send_photo(bot, message, 'game_media/chest_find.jpg')
        bot.send_message(message.chat.id, f'{storyline['3']['answers_and_aftereffects']['3']['aftereffect']}')
        user_character.agility_up(5)
        next_step(message)

    else:
        error_func(message)


def send_aftereffect_door_answer(bot, message, main_markup, error_func, next_step):
    if message.text == storyline['4']['answers_and_aftereffects']['1']['answer']:
        bot.send_message(message.chat.id, f'{storyline['4']['answers_and_aftereffects']['1']['aftereffect']}')
        next_step(message)

    elif message.text == storyline['4']['answers_and_aftereffects']['2']['answer']:
        bot.send_message(message.chat.id, f'{storyline['4']['answers_and_aftereffects']['2']['aftereffect']}')
        next_step(message)

    elif message.text == storyline['4']['answers_and_aftereffects']['3']['answer']:
        bot.send_message(message.chat.id, f'{storyline['4']['answers_and_aftereffects']['3']['aftereffect']}')
        next_step(message)

    elif message.text == storyline['4']['answers_and_aftereffects']['4']['answer']:
        bot.send_message(message.chat.id, f'{storyline['4']['answers_and_aftereffects']['4']['aftereffect']}',
                         parse_mode="HTML",
                         reply_markup=main_markup
                         )

    else:
        error_func(message)


def send_aftereffect_helpers_answer(bot, message, user_character, error_func, next_step):
    if message.text == storyline['5']['answers_and_aftereffects']['1']['answer']:
        send_photo(bot, message, 'game_media/scepter_gift.jpg')
        bot.send_message(message.chat.id, f'{storyline['5']['answers_and_aftereffects']['1']['aftereffect']}')
        user_character.intellect_up(10)
        user_character.add_to_inventory('scepter')
        next_step(message)

    elif message.text == storyline['5']['answers_and_aftereffects']['2']['answer']:
        send_photo(bot, message, 'game_media/sword_gift.jpg')
        bot.send_message(message.chat.id, f'{storyline['5']['answers_and_aftereffects']['2']['aftereffect']}')
        user_character.strength_up(10)
        user_character.add_to_inventory('sword')
        next_step(message)

    elif message.text == storyline['5']['answers_and_aftereffects']['3']['answer']:
        send_photo(bot, message, 'game_media/cloak_gift.jpg')
        bot.send_message(message.chat.id, f'{storyline['5']['answers_and_aftereffects']['3']['aftereffect']}')
        user_character.agility_up(10)
        user_character.add_to_inventory('cloak')
        next_step(message)

    else:
        error_func(message)


def send_aftereffect_final_answer(bot, message, user_character, error_func):
    if message.text == storyline['6']['answers_and_aftereffects']['1']['answer']:
        if user_character.intellect == 20:
            bot.send_message(message.chat.id,
                             f'{storyline['6']['answers_and_aftereffects']['1']['aftereffect']['win']}')
        else:
            send_photo(bot, message, 'game_media/lost_photo.jpg')
            bot.send_message(message.chat.id,
                             f'{storyline['6']['answers_and_aftereffects']['1']['aftereffect']['lose']}')

    elif message.text == storyline['6']['answers_and_aftereffects']['2']['answer']:
        if user_character.intellect >= 18 and 'scepter' in user_character.inventory:
            send_photo(bot, message, 'game_media/win_with_scepter.jpg')
            bot.send_message(message.chat.id,
                             f'{storyline['6']['answers_and_aftereffects']['2']['aftereffect']['win']}')
        else:
            send_photo(bot, message, 'game_media/lost_photo.jpg')
            bot.send_message(message.chat.id,
                             f'{storyline['6']['answers_and_aftereffects']['2']['aftereffect']['lose']}')

    elif message.text == storyline['6']['answers_and_aftereffects']['3']['answer']:
        if user_character.strength >= 20 and 'sword' in user_character.inventory:
            send_photo(bot, message, 'game_media/win_with_sword.jpg')
            bot.send_message(message.chat.id,
                             f'{storyline['6']['answers_and_aftereffects']['3']['aftereffect']['win']}')
        else:
            send_photo(bot, message, 'game_media/lost_photo.jpg')
            bot.send_message(message.chat.id,
                             f'{storyline['6']['answers_and_aftereffects']['3']['aftereffect']['lose']}')

    elif message.text == storyline['6']['answers_and_aftereffects']['4']['answer']:
        if user_character.agility >= 18 and 'cloak' in user_character.inventory:
            send_photo(bot, message, 'game_media/win_with_cloak.jpg')
            bot.send_message(message.chat.id,
                             f'{storyline['6']['answers_and_aftereffects']['4']['aftereffect']['win']}')
        else:
            send_photo(bot, message, 'game_media/lost_photo.jpg')
            bot.send_message(message.chat.id,
                             f'{storyline['6']['answers_and_aftereffects']['4']['aftereffect']['lose']}')

    else:
        error_func(message)
