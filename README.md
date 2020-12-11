Tutorial pra galera do front

1 - Use o comando "git clone {link do repositorio}"
2 - Entre na pasta e crie uma venv com o comando "python3 -m venv {qualquer_nome}"
3 - Ative a venv com o comando: "{qualquer_nome}\Scripts\activate.bat" (Windows - CMD)
                                "source {qualquer_nome}/bin/activate (Linux - Bash/Zsh)"

4 - Use o comando "pip install -r requirements.txt" para instalar as dependencias
5 - Depois de mudar alguam coisa (Use apenas a pasta template, onde estao os arquivos html/css) use o comando 'git commit -m "Mensagem do que mudou"'
6 - Para subir no repositorio as mudancas que fez use o comando "git push origin master"
7 - Se quiser testar o projeto de o comando "python manage.py runserver" fora da pasta templates (onde esta o arquivo manage.py)
