Cool_sticker = ("Классный стикер, но все же используйте бота по назначению\n"
                "Введите /help")
Not_understand_text = "Извините я вас не понял, пожалуйста введите команду или /help для просмотра списка команд"
Not_understand_media = ("К сожалению я всего лишь бот и не могу послушать и посмотреть все это\n"
                        "Введите команду /help")

say_start = (
        'Ты попал в бота-квест, чтобы начать свое приключение сначала выбери своего персонажа нажав на\n '
        '/choise_character\n'
        'Также можно ознакомиться с правилами нажав на /quest_rules\n'
        'Затем нажми на /start_quest, но помни что судьба твоего персонажа зависит только от тебя.')

rules = ('<b>Перед началом квеста</b>:\n'
         'Для начала выбери своего персонажа нажав на /choise_character\n'
         'Затем можно начинать квест нажав на /start_quest\n'
         '<b>Правила квеста</b>\n'
         'Во-первых если ты начал квест, то доходи до конца иначе прийдется начать сначала\n'
         'Во-вторых выбирай ответы кнопками снизу\n'
         'В-третьих квест за каждого из персонажей имеет разные варианты прохождения и иди по своей ветке,'
         ' не потайся из мага сделать мечника, максимальное значение атрибута 20\n'
         'В-четвёртых не пытайся поломать бота (у тебя все равно не получиться)\n'
         'В-пятых если у тебя нету вариантов кроме того как сдаться это значит что ты выбрал не правильный путь '
         'прокачки\n'
         'И последнее после каждой удачной и неудачной игры выбирай персонажа через /choise_character\n'
         'Вот и всё, удачного приключения!'
         )

commands = {

    '/start': 'Напишите /start чтобы бот заработал',

    '/help': 'Напишите /help для вывода списка команд',

    '/quest_rules': 'Напишите /quest_rules для вывода правил',

    '/choise_character': 'Напишите /choise_character чтобы выбрать своего персонажа',

    '/start_quest': 'Напишите /start_quest для старта вашего приключения'

}

characters = {
    'a_brilliant_mind': {
        'name': 'Гениальный Разум',
        'description': 'Ты мудрец который долгие годы учился и читал книги. '
                       'О твоем прошлом известно только то, что ты был самым умным человеком в твоем городе.\n'
                       'Также некоторые колдуны говорили что у тебя есть определённые способности к магии'},

    'bitter_knight': {
        'name': 'Печальный Рыцарь',
        'description': 'Ты бывший придворный рыцарь самого короля, но однажды ты подвел его и потерял свою честь.\n'
                       'Теперь ты только и можешь, что страдать по своему прошлому'},

    'child_of_thieves': {
        'name': 'Дитя Воров',
        'description': 'Ты ребенок которого выкинула собственная семья, но однажды тебя подобрали воры и обучили тебя '
                       'своим умениям.'
                       'К сожалению твоя банда распалась и ты остался совсем один.\n'
                       'Зато  умение искусно воровать осталось при тебе.'
    }
}

storyline = {
    '1': {
        'question': 'Ты оказываешься в темной темнице.\n'
                    'Ты абсолютно ничего не помнишь, кто ты? и как ты здесь оказался? '
                    'Перед тобой решетка и ты решаешь осмотреться вокруг.\n'
                    'Ты видишь приближающего к тебе охранника, у тебя есть время осмотреть только одно место.\n'
                    'Что осмотришь?',
        'answers': {
            '1': 'Выпирающий из стены кирпич',
            '2': 'Кровать',
            '3': 'Раковину и зеркало'}
    },

    '2': {
        'question': 'Охранник подходит к твоей камере для того, чтобы дать тебе еду.\n'
                    'Что ты сделаешь?',

        'answers_and_aftereffects': {
            '1': {'answer': 'Нападу на него',
                  'aftereffect': 'Ты успешно нападаешь на охранника и вырубаешь его,'
                                 'из его кармана ты достаешь ключ\n'
                                 'Ты выходишь в коридор'},

            '2': {'answer': 'Просто приму еду',
                  'aftereffect': 'Ты просто принимаешь его еду и он уходит\n'
                                 'Ты сбегаешь из камеры используя отмычку', },

            '3': {'answer': 'Выкраду у него  ключ',
                  'aftereffect': 'У тебя получается незаметно выкрасть ключ, охранник уходит.\n'
                                 'Ты выходишь в коридор'},
            '4': {'answer': 'Попытаюсь обмануть охранника и закрыть его в камере.',
                  'aftereffect': 'У тебя получается закрыть его в камере, а сам ты оказываешься в коридоре'}
            # конец 1 акта
        },
    },

    '3': {
        'question': 'Ты попадаешь в непонятное заброшенное место оно напоминает тебе чей-то дом, '
                    'ты идешь по дому и видишь 3 двери\n'
                    'Куда зайдешь?',
        'answers_and_aftereffects': {
            '1': {'answer': 'Библиотека',
                  'aftereffect': 'Ты заходишь туда и читаешь множество полезных книг'},
            '2': {'answer': 'Хранилище инструментов',
                  'aftereffect': 'Ты заходишь туда и находишь там топор'},
            '3': {'answer': 'Хранилище одежды и вещей',
                  'aftereffect': 'Ты заходишь туда и находишь много полезных вещей для того чтобы стать скрытнее'},
        }
    },

    '4': {
        'question': 'Перед тобой оказывается дверь с выходом, но она закрыта.\n'
                    'Над дверью висит табличка с загадкой что будешь делать?',
        'answers_and_aftereffects': {
            '1': {'answer': 'Решу ее и открою дверь',
                  'aftereffect': 'у тебя успешно получается решить головоломку и открыть дверь'},
            '2': {'answer': 'С помощью силы и топора сломаю ее',
                  'aftereffect': 'используя топор ты выбиваешь дверь'},
            '3': {'answer': 'Попытаюсь отмычкой открыть дверь',
                  'aftereffect': 'у тебя получается открыть дверь'},
            '4': {'answer': 'Сдаться',
                  'aftereffect': 'Ты остаешься в этом доме и тебя находит охранник\n'
                                 'Конец'}
        }
    },

    '5': {
        'question': 'Ты выходишь и оказываешься в лесу перед тобой 3 таблички\n'
                    'Куда пойдешь?',
        'answers_and_aftereffects': {
            '1': {'answer': 'Волшебник',
                  'aftereffect': 'Ты приходишь к волшебнику и просишь помочь тебе понять кто ты.\n'
                                 'Он говорит что это произошло из-за злого колдуна который питается чужыми '
                                 'воспоминаниями,'
                                 'но еще не поздно все вспомнить для этого нужно победить колдуна и забрать свои '
                                 'воспоминания.\n'
                                 'Волшебник решается тебе помочь и дарит тебе волшебный скипетр и учит тебя им '
                                 'пользоваться'},
            '2': {'answer': 'Кузнец',
                  'aftereffect': 'Ты приходишь к кузнецу и просишь помочь тебе понять кто ты.\n'
                                 'Он говорит что это произошло из-за злого колдуна который питается чужыми '
                                 'воспоминаниями,'
                                 'но еще не поздно все вспомнить для этого нужно победить колдуна и забрать свои '
                                 'воспоминания.\n'
                                 'Кузнец решает тебе помочь и дарит тебе меч которым пользовались только лучшие воины'},
            '3': {'answer': 'Глава воров',
                  'aftereffect': 'Ты приходишь к ворам и просишь помочь тебе понять кто ты.\n'
                                 'Они говорят что это произошло из-за злого колдуна который питается чужыми '
                                 'воспоминаниями,'
                                 'но еще не поздно все вспомнить для этого нужно победить колдуна и забрать свои '
                                 'воспоминания.\n'
                                 'Воры решают  тебе помочь и дарят тебе плащ-невидимку'}

        }
    },

    '6': {
        'question': 'Ты приходишь к логову колдуна и входишь в его владения. Он встречает тебя и говорит, что ждал '
                    'тебя.\n'
                    'Также колдун показывает тебе твои воспоминания, они находятся в специальном сосуде.\n'
                    'Колдун предлагает тебе 2 варианта: примкнуть к нему или сразиться за твои воспоминания\n'
                    'Что выберешь?',
        'answers_and_aftereffects': {
            '1': {'answer': 'Примкнуть к колдуну',
                  'aftereffect': {'lose': 'Ты примкнул к волшебнику , он тебя обманул и превратил  в крысу, '
                                          'теперь ты вынужден всю жизнь бегать по норам ',
                                  'win': 'Колдун принял тебя и сделал своим помощником.\n'
                                         'Вместе вы продолжаете творить зло'}
                  },

            '2': {'answer': 'Сразиться используя маг оружие и интеллект',
                  'aftereffect': {'lose': 'Тебе не удается победить колдуна он оказался слишком силен для тебя, '
                                          'он превратил тебя в крысу, теперь ты вынужден всю жизнь бегать по норам',
                                  'win': 'С помощью скипетра тебе удается победить злого колдуна и забрать свои '
                                         'воспоминания'}
                  },

            '3': {'answer': 'Сразиться используя оружие и силу',
                  'aftereffect': {'lose': 'Тебе не удается победить колдуна он оказался слишком силен для тебя, '
                                          'он превратил тебя в крысу, теперь ты вынужден всю жизнь бегать по норам',
                                  'win': 'С помощью меча тебе удается победить злого колдуна и забрать свои '
                                         'воспоминания'}
                  },

            '4': {'answer': 'Попытаться выкрасть сосуд и сбежать с помощью ловкости и др вещей',
                  'aftereffect': {'lose': 'Колдун оказался внимательнее чем ты думал и понял что ты пытаешься '
                                          'выкрасть сосуд.\n'
                                          'Он превратил тебя в крысу, теперь ты вынужден всю жизнь бегать по норам ',
                                  'win': 'С помощью плаща тебе удается выкрасть сосуд и сбежать от колдуна'}
                  }
        }
    }
}
