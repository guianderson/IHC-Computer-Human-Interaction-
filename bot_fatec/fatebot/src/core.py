from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from conf.settings import TELEGRAM_TOKEN, HTTP_CATS_URL


def start(bot, update):
    response_message = "Bem-vindo ao Bot ADS-CLASSTIME da FATEC SJC, aqui você tera acesso aos horários de aula" \
                       " do curso de Análise e Desenvolvimento de Sistemas \n\nPara maiores informações utilize o " \
                       "comando /help"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def help(bot, update):
    response_message = "Este BOT foi desenvolvido durante a aula de Integração Humano Computador, do curso de " \
                       "Análise e Desenvolvimento de Sistemas 3° Semestre. " \
                       "\n\n" \
                       "Possui como objetivo facilitar o acesso dos alunos de Análise e Desenvolvimento de Sistemas" \
                       " ao horário de suas aulas." \
                       "\n\nPara utilizar o BOT basta digitar /ads e o semestre que o aluno está cursando, e a turma " \
                       "que deseja saber o horario da aula como por exemplo: /ads1a (para alunos do curso de Análise e"\
                       " Desenvolvimento de Sistemas, cursando o primeiro semestre do curso, na turma A)"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def ads1a(bot, update):
    response_message = "HORÁRIO DAS AULAS DO CURSO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS TURMA A 1° SEMESTRE\n" \
                       "\nTURMA A: \n" \
                       "\n                              Segunda-Feira:\n" \
                       "07:10 às 08:50: Arquitetura e Organização de Computadores" \
                       "\n09:15 às 10:55: Administração Geral" \
                       "\n\n                              Terça-Feira:\n" \
                       "07:10 às 08:50: Inglês 1" \
                       "\n09:15 às 10:55: Matemática Discreta" \
                       "\n10:55 às 12:35: Administração Geral "\
                       "\n\n                              Quarta-Feira:\n" \
                       "07:10 às 08:50: Matemática Discreta" \
                       "\n09:15 às 10:55: Laboratório de Hardware" \
                       "\n\n                              Quinta-Feira:\n" \
                       "07:10 às 08:50: Arquitetura e Organização de Computadores" \
                       "\n09:15 às 10:55: Algoritmos e Lógica de Programação" \
                       "\n10:55 às 12:35: Programação em Microinformática " \
                       "\n\n                              Sexta-Feira:\n" \
                       "07:10 às 08:50: Programação em Microinformática" \
                       "\n09:15 às 10:55: Algoritmos e Lógica de Programação" \

    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def ads1b(bot, update):
        response_message = "HORÁRIO DAS AULAS DO CURSO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS TURMA B 1° SEMESTRE\n" \
                           "\nTURMA B: \n" \
                           "\n                              Segunda-Feira:\n" \
                           "07:10 às 08:50: Programação em Microinformática" \
                           "\n09:15 às 10:55: Administração Geral" \
                           "\n\n                              Terça-Feira:\n" \
                           "07:10 às 08:50: Inglês 1" \
                           "\n09:15 às 10:55: Algoritmos e Lógica de Programação" \
                           "\n10:55 às 12:35: Programação em Microinformática " \
                           "\n\n                              Quarta-Feira:\n" \
                           "07:10 às 08:50: Laboratório de Hardware" \
                           "\n09:15 às 10:55: Matemática Discreta" \
                           "\n\n                              Quinta-Feira:\n" \
                           "07:10 às 10:55: Arquitetura e Organização de Computadores" \
                           "\n10:55 às 12:35: Matemática Discreta " \
                           "\n\n                              Sexta-Feira:\n" \
                           "07:10 às 08:50: Algoritmos e Lógica de Programação" \
                           "\n09:15 às 10:55: Administração Geral" \

        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message
        )

def http_cats(bot, update, args):
    bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo=HTTP_CATS_URL + args[0]
    )


def unknown(bot, update):
    response_message = "Perdão, comando ou mensagem inexistente..."
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def main():
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', start)
    )

    dispatcher.add_handler(
        CommandHandler('help', help)
    )

    dispatcher.add_handler(
        CommandHandler('ads1a', ads1a)
    )

    dispatcher.add_handler(
        CommandHandler('ads1b', ads1b)
    )

    dispatcher.add_handler(
        CommandHandler('http', http_cats, pass_args=True)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.command, unknown)
    )

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()