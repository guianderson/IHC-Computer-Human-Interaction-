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

def ads2a(bot, update):
        response_message = "HORÁRIO DAS AULAS DO CURSO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS TURMA A 2° SEMESTRE\n" \
                           "\nTURMA A: \n" \
                           "\n                              Segunda-Feira:\n" \
                           "07:10 às 08:50: Comunicação e Expressão" \
                           "\n09:15 às 10:55: Linguagem de Programação" \
                           "\n\n                              Terça-Feira:\n" \
                           "07:10 às 08:50: Comunicação e Expressão" \
                           "\n09:15 às 10:55: Inglês II " \
                           "\n10:55 às 12:35:  Sistemas de Informação" \
                           "\n\n                              Quarta-Feira:\n" \
                           "07:10 às 08:50: Linguagem de Programação" \
                           "\n09:15 às 10:55: Cálculo" \
                           "\n\n                              Quinta-Feira:\n" \
                           "07:10 às 08:50: Sistemas de Informação" \
                           "\n09:15 às 10:55: Cálculo" \
                           "\n10:55 às 12:35:  Engenharia de Software I" \
                           "\n\n                              Sexta-Feira:\n" \
                           "07:10 às 08:50: Engenharia de Software I" \
                           "\n09:15 às 10:55: Contabilidade" \

        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message
        )

def ads2b(bot, update):
        response_message = "HORÁRIO DAS AULAS DO CURSO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS TURMA B 2° SEMESTRE\n" \
                           "\nTURMA B: \n" \
                           "\n                              Segunda-Feira:\n" \
                           "07:10 às 08:50: Linguagem de Programação" \
                           "\n09:15 às 10:55: Contabilidade " \
                           "\n\n                              Terça-Feira:\n" \
                           "07:10 às 08:50: Linguagem de Programação" \
                           "\n09:15 às 10:55: Inglês II" \
                           "\n10:55 às 12:35:  Sistemas de Informação" \
                           "\n\n                              Quarta-Feira:\n" \
                           "07:10 às 08:50: Cálculo" \
                           "\n09:15 às 10:55: Engenharia de Software I" \
                           "\n\n                              Quinta-Feira:\n" \
                           "07:10 às 08:50: Sistemas de Informação" \
                           "\n09:15 às 10:55: Comunicação e Expressão" \
                           "\n10:55 às 12:35:  Engenharia de Software I" \
                           "\n\n                              Sexta-Feira:\n" \
                           "07:10 às 08:50: Cálculo" \
                           "\n09:15 às 10:55: Comunicação e Expressão" \

        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message
        )

def ads3a(bot, update):
        response_message = "HORÁRIO DAS AULAS DO CURSO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS TURMA A 3° SEMESTRE\n" \
                           "\nTURMA A: \n" \
                           "\n                              Segunda-Feira:\n" \
                           "07:10 às 08:50: Estruturas de Dados " \
                           "\n09:15 às 10:55: Sistemas Operacionais I" \
                           "\n\n                              Terça-Feira:\n" \
                           "07:10 às 08:50: Estruturas de Dados" \
                           "\n09:15 às 10:55: Engenharia de Software II" \
                           "\n10:55 às 12:35:  Programação Orientada a Objetos" \
                           "\n\n                              Quarta-Feira:\n" \
                           "07:10 às 08:50: Inglês III " \
                           "\n09:15 às 10:55: Interação Humano Computador" \
                           "\n\n                              Quinta-Feira:\n" \
                           "07:10 às 08:50: Sistemas Operacionais I" \
                           "\n09:15 às 10:55: Engenharia de Software II" \
                           "\n10:55 às 12:35:  Economia e Finanças" \
                           "\n\n                              Sexta-Feira:\n" \
                           "07:10 às 08:50: Sociedade e Tecnologia" \
                           "\n09:15 às 10:55: Programação Orientada a Objetos" \

        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message
        )

def ads3b(bot, update):
        response_message = "HORÁRIO DAS AULAS DO CURSO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS TURMA A 3° SEMESTRE\n" \
                           "\nTURMA B: \n" \
                           "\n                              Segunda-Feira:\n" \
                           "07:10 às 08:50: Sistemas Operacionais I " \
                           "\n09:15 às 10:55: Programação Orientada a Objetos" \
                           "\n\n                              Terça-Feira:\n" \
                           "07:10 às 08:50: Sistemas Operacionais I" \
                           "\n09:15 às 10:55: Engenharia de Software II" \
                           "\n10:55 às 12:35:  Economia e Finanças" \
                           "\n\n                              Quarta-Feira:\n" \
                           "07:10 às 08:50: Inglês III" \
                           "\n09:15 às 10:55: Estruturas de Dados" \
                           "\n\n                              Quinta-Feira:\n" \
                           "07:10 às 08:50: Programação Orientada a Objetos" \
                           "\n09:15 às 10:55: Engenharia de Software II" \
                           "\n10:55 às 12:35:  Estruturas de Dados" \
                           "\n\n                              Sexta-Feira:\n" \
                           "07:10 às 08:50: Sociedade e Tecnologia" \
                           "\n09:15 às 10:55: Interação Humano Computador" \

        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message
        )

def ads4a(bot, update):
        response_message = "HORÁRIO DAS AULAS DO CURSO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS TURMA A 4° SEMESTRE\n" \
                           "\nTURMA 4: \n" \
                           "\n                              Segunda-Feira:\n" \
                           "07:10 às 08:50: Testes de Software" \
                           "\n09:15 às 10:55: Engenharia de Software III" \
                           "\n\n                              Terça-Feira:\n" \
                           "07:10 às 08:50: Estatística Aplicada" \
                           "\n09:15 às 10:55: Estatística Aplicada" \
                           "\n10:55 às 12:35:  Engenharia de Software III" \
                           "\n\n                              Quarta-Feira:\n" \
                           "07:10 às 08:50: Testes de Software" \
                           "\n09:15 às 10:55: Sistemas Operacionais II" \
                           "\n\n                              Quinta-Feira:\n" \
                           "07:10 às 08:50: Inglês IV " \
                           "\n09:15 às 10:55: Banco de Dados" \
                           "\n10:55 às 12:35:  Metod. da Pesq. Científico-Tecnológica" \
                           "\n\n                              Sexta-Feira:\n" \
                           "07:10 às 08:50: Sistemas Operacionais II" \
                           "\n09:15 às 10:55: Banco de Dados" \

        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message
        )

def ads4b(bot, update):
        response_message = "HORÁRIO DAS AULAS DO CURSO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS TURMA A 4° SEMESTRE\n" \
                           "\nTURMA B: \n" \
                           "\n                              Segunda-Feira:\n" \
                           "07:10 às 08:50: Banco de Dados" \
                           "\n09:15 às 10:55: Sistemas Operacionais II" \
                           "\n\n                              Terça-Feira:\n" \
                           "07:10 às 08:50: Engenharia de Software III" \
                           "\n09:15 às 10:55: Programação de Scripts" \
                           "\n10:55 às 12:35:  Metod. da Pesq. Científico-Tecnológica" \
                           "\n\n                              Quarta-Feira:\n" \
                           "07:10 às 08:50: Estatística Aplicada" \
                           "\n09:15 às 10:55: Sistemas Operacionais II" \
                           "\n\n                              Quinta-Feira:\n" \
                           "07:10 às 08:50: Inglês IV" \
                           "\n09:15 às 10:55: Engenharia de Software III" \
                           "\n10:55 às 12:35:  Programação de Scripts" \
                           "\n\n                              Sexta-Feira:\n" \
                           "07:10 às 08:50: Banco de Dados" \
                           "\n09:15 às 10:55: Estatística Aplicada" \

        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message
        )

def ads5(bot, update):
        response_message = "HORÁRIO DAS AULAS DO CURSO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS TURMA A 5° SEMESTRE\n" \
                           "\n                              Segunda-Feira:\n" \
                           "07:10 às 08:50: Programação para Dispositivos Móveis" \
                           "\n09:15 às 10:55: Laboratório de Banco de Dados" \
                           "\n\n                              Terça-Feira:\n" \
                           "07:10 às 08:50: Laboratório de Engenharia de Software" \
                           "\n09:15 às 10:55: Redes de Computadores" \
                           "\n10:55 às 12:35:  Laboratório de Banco de Dados" \
                           "\n\n                              Quarta-Feira:\n" \
                           "07:10 às 08:50: Segurança da Informação" \
                           "\n09:15 às 10:55: Programação Linear e Aplicações" \
                           "\n10:55 às 12:35:  Trabalho de Graduação I" \
                           "\n\n                              Quinta-Feira:\n" \
                           "07:10 às 08:50: Programação Linear e Aplicações" \
                           "\n09:15 às 10:55: Inglês V" \
                           "\n10:55 às 12:35: Programação para Dispositivos Móveis" \
                           "\n\n                              Sexta-Feira:\n" \
                           "07:10 às 08:50: Laboratório de Engenharia de Software" \
                           "\n09:15 às 10:55: Redes de Computadores" \

        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message
        )

def ads6(bot, update):
        response_message = "HORÁRIO DAS AULAS DO CURSO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS TURMA A 6° SEMESTRE\n" \
                           "\n                              Segunda-Feira:\n" \
                           "07:10 às 08:50: Gestão e Governança de Tec. da Informação" \
                           "\n09:15 às 10:55: Tópicos Especiais em Informática" \
                           "\n10:55 às 12:35: Trabalho de graduação II" \
                           "\n\n                              Terça-Feira:\n" \
                           "07:10 às 08:50: Inteligência Artificial" \
                           "\n09:15 às 10:55: Empreendedorismo" \
                           "\n10:55 às 12:35:  Tópicos Especiais em Informática" \
                           "\n\n                              Quarta-Feira:\n" \
                           "07:10 às 08:50: Gestão de Projetos" \
                           "\n09:15 às 10:55: Inglês VI" \
                           "\n\n                              Quinta-Feira:\n" \
                           "07:10 às 08:50: Ética e Responsabilidade Profissional" \
                           "\n09:15 às 10:55: Gestão de Equipes" \
                           "\n10:55 às 12:35: Inteligência Artificial" \
                           "\n\n                              Sexta-Feira:\n" \
                           "07:10 às 08:50: Gestão de Projetos" \
                           "\n09:15 às 10:55: Gestão e Governança de Tec. da Informação" \

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
        CommandHandler('ads2a', ads2a)
    )

    dispatcher.add_handler(
        CommandHandler('ads2b', ads3b)
    )

    dispatcher.add_handler(
        CommandHandler('ads3a', ads3a)
    )

    dispatcher.add_handler(
        CommandHandler('ads3b', ads3b)
    )

    dispatcher.add_handler(
        CommandHandler('ads4a', ads4a)
    )

    dispatcher.add_handler(
        CommandHandler('ads4b', ads4b)
    )

    dispatcher.add_handler(
        CommandHandler('ads5', ads5)
    )

    dispatcher.add_handler(
        CommandHandler('ads6', ads6)
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
