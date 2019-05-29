#!/usr/bin/python
# -*- coding: latin-1 -*-

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
import os
from dotenv import load_dotenv
load_dotenv()
TELEGRAM_TOKEN = os.getenv("813769264:AAF36PiMEshOFHWjcLtq6RvEOeOEzM6c9XI")


def start(bot, update):
    response_message = "Bem-vindo ao Bot ADS-CLASSTIME da FATEC SJC, aqui voc� tera acesso aos hor�rios de aula" \
                       " do curso de An�lise e Desenvolvimento de Sistemas \n\nPara maiores informa��es utilize o " \
                       "comando /help"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def help(bot, update):
    response_message = "Este BOT foi desenvolvido durante a aula de Integra��o Humano Computador, do curso de " \
                       "An�lise e Desenvolvimento de Sistemas 3� Semestre. " \
                       "\n\n" \
                       "Possui como objetivo facilitar o acesso dos alunos de An�lise e Desenvolvimento de Sistemas" \
                       " ao hor�rio de suas aulas." \
                       "\n\nPara utilizar o BOT basta digitar /ads e o semestre que o aluno est� cursando, e a turma " \
                       "que deseja saber o horario da aula como por exemplo: /ads1a (para alunos do curso de An�lise e"\
                       " Desenvolvimento de Sistemas, cursando o primeiro semestre do curso, na turma A)"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def ads1a(bot, update):
    response_message = "HOR�RIO DAS AULAS DO CURSO DE AN�LISE E DESENVOLVIMENTO DE SISTEMAS TURMA A 1� SEMESTRE\n" \
                       "\nTURMA A: \n" \
                       "\n                              Segunda-Feira:\n" \
                       "07:10 �s 08:50: Arquitetura e Organiza��o de Computadores" \
                       "\n09:15 �s 10:55: Administra��o Geral" \
                       "\n\n                              Ter�a-Feira:\n" \
                       "07:10 �s 08:50: Ingl�s 1" \
                       "\n09:15 �s 10:55: Matem�tica Discreta" \
                       "\n10:55 �s 12:35: Administra��o Geral "\
                       "\n\n                              Quarta-Feira:\n" \
                       "07:10 �s 08:50: Matem�tica Discreta" \
                       "\n09:15 �s 10:55: Laborat�rio de Hardware" \
                       "\n\n                              Quinta-Feira:\n" \
                       "07:10 �s 08:50: Arquitetura e Organiza��o de Computadores" \
                       "\n09:15 �s 10:55: Algoritmos e L�gica de Programa��o" \
                       "\n10:55 �s 12:35: Programa��o em Microinform�tica " \
                       "\n\n                              Sexta-Feira:\n" \
                       "07:10 �s 08:50: Programa��o em Microinform�tica" \
                       "\n09:15 �s 10:55: Algoritmos e L�gica de Programa��o" \

    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def ads1b(bot, update):
        response_message = "HOR�RIO DAS AULAS DO CURSO DE AN�LISE E DESENVOLVIMENTO DE SISTEMAS TURMA B 1� SEMESTRE\n" \
                           "\nTURMA B: \n" \
                           "\n                              Segunda-Feira:\n" \
                           "07:10 �s 08:50: Programa��o em Microinform�tica" \
                           "\n09:15 �s 10:55: Administra��o Geral" \
                           "\n\n                              Ter�a-Feira:\n" \
                           "07:10 �s 08:50: Ingl�s 1" \
                           "\n09:15 �s 10:55: Algoritmos e L�gica de Programa��o" \
                           "\n10:55 �s 12:35: Programa��o em Microinform�tica " \
                           "\n\n                              Quarta-Feira:\n" \
                           "07:10 �s 08:50: Laborat�rio de Hardware" \
                           "\n09:15 �s 10:55: Matem�tica Discreta" \
                           "\n\n                              Quinta-Feira:\n" \
                           "07:10 �s 10:55: Arquitetura e Organiza��o de Computadores" \
                           "\n10:55 �s 12:35: Matem�tica Discreta " \
                           "\n\n                              Sexta-Feira:\n" \
                           "07:10 �s 08:50: Algoritmos e L�gica de Programa��o" \
                           "\n09:15 �s 10:55: Administra��o Geral" \

        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message
        )

def ads2a(bot, update):
        response_message = "HOR�RIO DAS AULAS DO CURSO DE AN�LISE E DESENVOLVIMENTO DE SISTEMAS TURMA A 2� SEMESTRE\n" \
                           "\nTURMA A: \n" \
                           "\n                              Segunda-Feira:\n" \
                           "07:10 �s 08:50: Comunica��o e Express�o" \
                           "\n09:15 �s 10:55: Linguagem de Programa��o" \
                           "\n\n                              Ter�a-Feira:\n" \
                           "07:10 �s 08:50: Comunica��o e Express�o" \
                           "\n09:15 �s 10:55: Ingl�s II " \
                           "\n10:55 �s 12:35:  Sistemas de Informa��o" \
                           "\n\n                              Quarta-Feira:\n" \
                           "07:10 �s 08:50: Linguagem de Programa��o" \
                           "\n09:15 �s 10:55: C�lculo" \
                           "\n\n                              Quinta-Feira:\n" \
                           "07:10 �s 08:50: Sistemas de Informa��o" \
                           "\n09:15 �s 10:55: C�lculo" \
                           "\n10:55 �s 12:35:  Engenharia de Software I" \
                           "\n\n                              Sexta-Feira:\n" \
                           "07:10 �s 08:50: Engenharia de Software I" \
                           "\n09:15 �s 10:55: Contabilidade" \

        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message
        )

def ads2b(bot, update):
        response_message = "HOR�RIO DAS AULAS DO CURSO DE AN�LISE E DESENVOLVIMENTO DE SISTEMAS TURMA B 2� SEMESTRE\n" \
                           "\nTURMA B: \n" \
                           "\n                              Segunda-Feira:\n" \
                           "07:10 �s 08:50: Linguagem de Programa��o" \
                           "\n09:15 �s 10:55: Contabilidade " \
                           "\n\n                              Ter�a-Feira:\n" \
                           "07:10 �s 08:50: Linguagem de Programa��o" \
                           "\n09:15 �s 10:55: Ingl�s II" \
                           "\n10:55 �s 12:35:  Sistemas de Informa��o" \
                           "\n\n                              Quarta-Feira:\n" \
                           "07:10 �s 08:50: C�lculo" \
                           "\n09:15 �s 10:55: Engenharia de Software I" \
                           "\n\n                              Quinta-Feira:\n" \
                           "07:10 �s 08:50: Sistemas de Informa��o" \
                           "\n09:15 �s 10:55: Comunica��o e Express�o" \
                           "\n10:55 �s 12:35:  Engenharia de Software I" \
                           "\n\n                              Sexta-Feira:\n" \
                           "07:10 �s 08:50: C�lculo" \
                           "\n09:15 �s 10:55: Comunica��o e Express�o" \

        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message
        )

def ads3a(bot, update):
        response_message = "HOR�RIO DAS AULAS DO CURSO DE AN�LISE E DESENVOLVIMENTO DE SISTEMAS TURMA A 3� SEMESTRE\n" \
                           "\nTURMA A: \n" \
                           "\n                              Segunda-Feira:\n" \
                           "07:10 �s 08:50: Estruturas de Dados " \
                           "\n09:15 �s 10:55: Sistemas Operacionais I" \
                           "\n\n                              Ter�a-Feira:\n" \
                           "07:10 �s 08:50: Estruturas de Dados" \
                           "\n09:15 �s 10:55: Engenharia de Software II" \
                           "\n10:55 �s 12:35:  Programa��o Orientada a Objetos" \
                           "\n\n                              Quarta-Feira:\n" \
                           "07:10 �s 08:50: Ingl�s III " \
                           "\n09:15 �s 10:55: Intera��o Humano Computador" \
                           "\n\n                              Quinta-Feira:\n" \
                           "07:10 �s 08:50: Sistemas Operacionais I" \
                           "\n09:15 �s 10:55: Engenharia de Software II" \
                           "\n10:55 �s 12:35:  Economia e Finan�as" \
                           "\n\n                              Sexta-Feira:\n" \
                           "07:10 �s 08:50: Sociedade e Tecnologia" \
                           "\n09:15 �s 10:55: Programa��o Orientada a Objetos" \

        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message
        )

def ads3b(bot, update):
        response_message = "HOR�RIO DAS AULAS DO CURSO DE AN�LISE E DESENVOLVIMENTO DE SISTEMAS TURMA A 3� SEMESTRE\n" \
                           "\nTURMA B: \n" \
                           "\n                              Segunda-Feira:\n" \
                           "07:10 �s 08:50: Sistemas Operacionais I " \
                           "\n09:15 �s 10:55: Programa��o Orientada a Objetos" \
                           "\n\n                              Ter�a-Feira:\n" \
                           "07:10 �s 08:50: Sistemas Operacionais I" \
                           "\n09:15 �s 10:55: Engenharia de Software II" \
                           "\n10:55 �s 12:35:  Economia e Finan�as" \
                           "\n\n                              Quarta-Feira:\n" \
                           "07:10 �s 08:50: Ingl�s III" \
                           "\n09:15 �s 10:55: Estruturas de Dados" \
                           "\n\n                              Quinta-Feira:\n" \
                           "07:10 �s 08:50: Programa��o Orientada a Objetos" \
                           "\n09:15 �s 10:55: Engenharia de Software II" \
                           "\n10:55 �s 12:35:  Estruturas de Dados" \
                           "\n\n                              Sexta-Feira:\n" \
                           "07:10 �s 08:50: Sociedade e Tecnologia" \
                           "\n09:15 �s 10:55: Intera��o Humano Computador" \

        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message
        )

def ads4a(bot, update):
        response_message = "HOR�RIO DAS AULAS DO CURSO DE AN�LISE E DESENVOLVIMENTO DE SISTEMAS TURMA A 4� SEMESTRE\n" \
                           "\nTURMA 4: \n" \
                           "\n                              Segunda-Feira:\n" \
                           "07:10 �s 08:50: Testes de Software" \
                           "\n09:15 �s 10:55: Engenharia de Software III" \
                           "\n\n                              Ter�a-Feira:\n" \
                           "07:10 �s 08:50: Estat�stica Aplicada" \
                           "\n09:15 �s 10:55: Estat�stica Aplicada" \
                           "\n10:55 �s 12:35:  Engenharia de Software III" \
                           "\n\n                              Quarta-Feira:\n" \
                           "07:10 �s 08:50: Testes de Software" \
                           "\n09:15 �s 10:55: Sistemas Operacionais II" \
                           "\n\n                              Quinta-Feira:\n" \
                           "07:10 �s 08:50: Ingl�s IV " \
                           "\n09:15 �s 10:55: Banco de Dados" \
                           "\n10:55 �s 12:35:  Metod. da Pesq. Cient�fico-Tecnol�gica" \
                           "\n\n                              Sexta-Feira:\n" \
                           "07:10 �s 08:50: Sistemas Operacionais II" \
                           "\n09:15 �s 10:55: Banco de Dados" \

        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message
        )

def ads4b(bot, update):
        response_message = "HOR�RIO DAS AULAS DO CURSO DE AN�LISE E DESENVOLVIMENTO DE SISTEMAS TURMA A 4� SEMESTRE\n" \
                           "\nTURMA B: \n" \
                           "\n                              Segunda-Feira:\n" \
                           "07:10 �s 08:50: Banco de Dados" \
                           "\n09:15 �s 10:55: Sistemas Operacionais II" \
                           "\n\n                              Ter�a-Feira:\n" \
                           "07:10 �s 08:50: Engenharia de Software III" \
                           "\n09:15 �s 10:55: Programa��o de Scripts" \
                           "\n10:55 �s 12:35:  Metod. da Pesq. Cient�fico-Tecnol�gica" \
                           "\n\n                              Quarta-Feira:\n" \
                           "07:10 �s 08:50: Estat�stica Aplicada" \
                           "\n09:15 �s 10:55: Sistemas Operacionais II" \
                           "\n\n                              Quinta-Feira:\n" \
                           "07:10 �s 08:50: Ingl�s IV" \
                           "\n09:15 �s 10:55: Engenharia de Software III" \
                           "\n10:55 �s 12:35:  Programa��o de Scripts" \
                           "\n\n                              Sexta-Feira:\n" \
                           "07:10 �s 08:50: Banco de Dados" \
                           "\n09:15 �s 10:55: Estat�stica Aplicada" \

        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message
        )

def ads5(bot, update):
        response_message = "HOR�RIO DAS AULAS DO CURSO DE AN�LISE E DESENVOLVIMENTO DE SISTEMAS TURMA A 5� SEMESTRE\n" \
                           "\n                              Segunda-Feira:\n" \
                           "07:10 �s 08:50: Programa��o para Dispositivos M�veis" \
                           "\n09:15 �s 10:55: Laborat�rio de Banco de Dados" \
                           "\n\n                              Ter�a-Feira:\n" \
                           "07:10 �s 08:50: Laborat�rio de Engenharia de Software" \
                           "\n09:15 �s 10:55: Redes de Computadores" \
                           "\n10:55 �s 12:35:  Laborat�rio de Banco de Dados" \
                           "\n\n                              Quarta-Feira:\n" \
                           "07:10 �s 08:50: Seguran�a da Informa��o" \
                           "\n09:15 �s 10:55: Programa��o Linear e Aplica��es" \
                           "\n10:55 �s 12:35:  Trabalho de Gradua��o I" \
                           "\n\n                              Quinta-Feira:\n" \
                           "07:10 �s 08:50: Programa��o Linear e Aplica��es" \
                           "\n09:15 �s 10:55: Ingl�s V" \
                           "\n10:55 �s 12:35: Programa��o para Dispositivos M�veis" \
                           "\n\n                              Sexta-Feira:\n" \
                           "07:10 �s 08:50: Laborat�rio de Engenharia de Software" \
                           "\n09:15 �s 10:55: Redes de Computadores" \

        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message
        )

def ads6(bot, update):
        response_message = "HOR�RIO DAS AULAS DO CURSO DE AN�LISE E DESENVOLVIMENTO DE SISTEMAS TURMA A 6� SEMESTRE\n" \
                           "\n                              Segunda-Feira:\n" \
                           "07:10 �s 08:50: Gest�o e Governan�a de Tec. da Informa��o" \
                           "\n09:15 �s 10:55: T�picos Especiais em Inform�tica" \
                           "\n10:55 �s 12:35: Trabalho de gradua��o II" \
                           "\n\n                              Ter�a-Feira:\n" \
                           "07:10 �s 08:50: Intelig�ncia Artificial" \
                           "\n09:15 �s 10:55: Empreendedorismo" \
                           "\n10:55 �s 12:35:  T�picos Especiais em Inform�tica" \
                           "\n\n                              Quarta-Feira:\n" \
                           "07:10 �s 08:50: Gest�o de Projetos" \
                           "\n09:15 �s 10:55: Ingl�s VI" \
                           "\n\n                              Quinta-Feira:\n" \
                           "07:10 �s 08:50: �tica e Responsabilidade Profissional" \
                           "\n09:15 �s 10:55: Gest�o de Equipes" \
                           "\n10:55 �s 12:35: Intelig�ncia Artificial" \
                           "\n\n                              Sexta-Feira:\n" \
                           "07:10 �s 08:50: Gest�o de Projetos" \
                           "\n09:15 �s 10:55: Gest�o e Governan�a de Tec. da Informa��o" \

        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message
        )


def unknown(bot, update):
    response_message = "Perd�o, comando ou mensagem inexistente..."
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def main():
    updater = Updater(token="813769264:AAF36PiMEshOFHWjcLtq6RvEOeOEzM6c9XI")

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
        MessageHandler(Filters.command, unknown)
    )

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()
