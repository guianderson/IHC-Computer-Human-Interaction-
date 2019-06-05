# Trabalho de Interação Humano Computador
# Desenvolvendo ChatBot utilizando Python


O desenvolvimento do Bot foi proposto pelo professor da FATEC SJC, Giuliano Bertoti, para a matéria Interação Humano Computador.

# FateBot - ChatBot que mostrar o horário das aulas para os alunos de Análise e Desenvolvimento de Sistemas

  - Desenvolvido em Python
  - ChatBot desenvolvido utilizando API do Telegran
  - Deploy feito utilizando ferramenta pythonanywhere

### Comandos

Todos os comandos que podem ser utilizados no ChatBot

* /start - Iniciar ChatBot
* /help - Explicação de como o ChatBot funciona
* /ads1a - Horário de Aulas do 1° Semestre turma A de ADS
* /ads1b - Horário de Aulas do 1° Semestre turma B de ADS
* /ads2a - Horário de Aulas do 2° Semestre turma A de ADS
* /ads2b - Horário de Aulas do 2° Semestre turma B de ADS
* /ads3a - Horário de Aulas do 3° Semestre turma A de ADS
* /ads3b - Horário de Aulas do 3° Semestre turma B de ADS
* /ads4a - Horário de Aulas do 4° Semestre turma A de ADS
* /ads4b - Horário de Aulas do 4° Semestre turma B de ADS
* /ads5 - Horário de Aulas do 5° Semestre de ADS
* /ads6 - Horário de Aulas do 6° Semestre de ADS

### Instalação

Para ter o repositório em sua máquina basta clonar o repositório em: https://github.com/guianderson/IHC-Computer-Human-Interaction-

- Para que tudo funione corretamente é importante que instale o requirements.txt.

Para utilizar o chatBot basta acessar o telegran e procurar por: @classHourHelper_FateBot

# Como colocar fazer deploy no pythonanywhere?
  - Acesso o site: https://www.pythonanywhere.com e faça seu cadastro
  - Depois de realizar seu cadastro será redirecionado para o DashBoard
  - Na aba Files, clique em Open another File, e coloque caminho completo que aparecera e o nomedoarquivo.py
  - Será aberto uma página em branco, bem parecida com a página do IDLE, dentro dela cole seu código python, no entanto para que funcione corretamente é necessário que no inicio do código você ensira o seguinte trecho, para que o programa entenda que a linguagem utilizada é python, e que o texto contido no arquivo é Latino.
```sh
$ #!/usr/bin/python
$ # -*- coding: latin-1 -*-
```
5 - Clique em Salvar e volte para o DashBoard do pythonAnywhere
6 - Na aba console, crie um console novo, e utilize o seguinte comando: 
```sh
$ python nomedoarquivo.py
```
7 - Seu projeto já no ar, seu deploy já foi feito e você pode utilizar seu ChatBot sem ter que startar seu projeto manualmente.

### Tendo alguma dúvida me chame no Facebook: https://www.facebook.com/guilherme.andernson