import telebot
import time

import top
import mid

bot_token = '744694280:AAGKpQbwNhsilHO7E1Aj1FE6izh2etCJBew'

bot = telebot.TeleBot(token=bot_token)


def find_at(msg):
    for text in msg:
        if 'darius' in text:
            return text


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Olá, seja bem-vindo ao LolBot! Para mais informações sobre o BOT utilize o comando: '
                          '/apresentacao, e para aprender a usar o BOT corretamente utilize o comando /help')


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'Para utilizar o BOT corretamente primeiramente ensira a Lane do campeão que deseja '
                          'utilizando o comando /top para campeões Top Leaners, /mid para campeões Mid Leaners, /jungle'
                          ' para campeões Junglers, /botadc para campeões AdCarrys e /botsup para os campeões suportes'
                          ', fazendo isso sera exibido todos os campeões cadastrados na lane escolhida, posteriormente '
                          'insira o nome do campeão, então todas as informações sobre o mesmo serão exibidas.')


@bot.message_handler(commands=['apresentacao'])
def send_welcome(message):
    bot.reply_to(message, 'Este BOT foi desenvolvido com a finalizade de mostrar para os jogadores de League of Legends'
                          ' informações sobre os campeões do jogo, como por exemplo, machup, ordem de evolução das '
                          'skills, core build, core runnas, entre outras informações. Par aprender a utilizar o BOT '
                          'corretamente utilize o comando /help')


@bot.message_handler(commands=['top'])
def send_welcome(message):
    bot.reply_to(message, 'Você escolheu a Top Lane, os campeões cadastrados nessa lane são: Darius, Jax, Panteon')


@bot.message_handler(commands=['mid'])
def send_welcome(message):
    bot.reply_to(message, 'Você escolheu a Mid Lane, os campeões cadastrados nessa lane são: Ahri, Zed, Yasuo')


@bot.message_handler(commands=['jungle'])
def send_welcome(message):
    bot.reply_to(message, 'Você escolheu a Top Lane, os campeões cadastrados nessa lane são: Master Yi, Jax, Panteon')


def reposta(texto):
    @bot.message_handler(func=lambda msg: msg.text is not None and texto in msg.text)
    def at_answer(message):
        #TODO: chamando Campeões
        if texto == 'Nasus':
            [bot.reply_to(message, x) for x in top.nasus()]
        elif texto == 'Maokai':
            [bot.reply_to(message, x) for x in top.maokai()]
        elif texto == 'Garen':
            [bot.reply_to(message, x) for x in top.garen()]
        elif texto == 'Darius':
            [bot.reply_to(message, x) for x in top.darius()]
        elif texto == 'Malphite':
            [bot.reply_to(message, x) for x in top.malphite()]
        elif texto == 'Wucong':
            [bot.reply_to(message, x) for x in top.wucong()]
        elif texto == 'Riven':
            [bot.reply_to(message, x) for x in top.riven()]
        elif texto == 'Pantheon':
            [bot.reply_to(message, x) for x in top.pantheon()]
        elif texto == 'Sion':
            [bot.reply_to(message, x) for x in top.sion()]
        elif texto == 'Aatrox':
            [bot.reply_to(message, x) for x in top.aatrox()]
        elif texto == 'Coco':
            [bot.reply_to(message, x) for x in mid.coco()]

reposta('Nasus')
reposta('Maokai')
reposta('Garen')
reposta('Darius')
reposta('Malphite')
reposta('Wucong')
reposta('Riven')
reposta('Pantheon')
reposta('Sion')
reposta('Aatrox')
reposta('Coco')




while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)

# .format(at_text) para selecionar o que foi escrito
