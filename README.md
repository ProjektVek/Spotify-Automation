# SpotiBot: Spotify Automation / Automação do Spotify
### by Victor "VeK" Ferreira 
<br>

### A bot for automating Spotify Web / Um bot para automatizar o Spotify Web
<br>

### Observations / Observações:

- I don't added support for English Spotify Yet / Eu ainda não adicionei suporte para o Spotify em Inglês
- Probably you will need to setup a few things to run, like create .env file with your Spotify credentials / Provavelmente voce terá que ajustar algumas coisas para rodar, como criar arquivo .env com suas credenciais(login) do Spotify
- I STRONGLY recommend to check out <a href="https://youtu.be/uU9MoVgElcg">BotCity tutorial</a> before trying to use this program on your computer / Eu recomendo FORTEMENTE que você assista ao <a href="https://youtu.be/uU9MoVgElcg">tutorial da BotCity</a> antes de tentar usar esse programa no seu computador.

### Whats it does? / O que ele faz?:

This is a automation code (bot) for automating spotify web, using python and BotCity tools. It mutes ads automatically when they start to playing, and try to skip them when possible.
I will be adding another functions if there is another thing that i would like to do with this bot. It does automatic login on Spotify too. 
<br><br>
Isso é um código para automação (bot) do spotify web, utilizando python e as ferramentas da BotCity. Ele muta os anúncios automaticamente quando eles começam a tocar, e tenta pular quando for possível.
Eu estarei adicionando outras funções caso haja outras coisas que eu gostaria de fazer com esse bot. Ele também realiza Login automático.

- Enter Open Spotify Website and tries to Login (You have to create a .env file with your credentials, more details below) / Entra no site Open Spotify e tenta Logar (Você tem que criar um arquivo .env com suas credenciais(Login) do Spotify, mais detalhes abaixo)
- After logged in, tries to identify when an ad is running, and when detected, mutes Spotify volume and tries to skip the ad. / Depois de logado, tenta identificar quando um anúncio esta sendo executado, e quando detectado, muta o volume do Spotify e tenta pular o anúncio.

### Why I did this? / Porque eu fiz isso?:

The spotify free on desktop(/web) is already good enough for me, but i always have to mute and skip ads manually. I have the idea to create a bot to do this for me automatically. I know i wanted to do using Python, and then, someday before I started the project, I watched a BotCity Workshop from Gabriel Archanjo (BotCity CTO) using BotCity tools to automate Web and Desktop systems. In that moment, I think it would be the perfect tool for the task. 
<br><br>
A versão gratuita do spotify desktop(/web) já e suficiente pra mim, porém eu sempre tenho que mutar e pular os anúncios manualmente. Então eu tive a ideia de criar um bot para fazer isso para mim automaticamente. Eu sabia que eu queria fazer usando Python, e então, certo dia antes de comecar o projeto, eu assisti um Workshop da BotCity (DoWhile 2021) do Gabriel Archanjo (CTO da BotCity) utilizando as ferramentas da BotCity para automatizar Sistemas Web e Desktop. Naquele momento, eu acreditei que elas seriam as ferramentas perfeitas para a tarefa.

### Technologies / Tecnologias:

This project will be made primarily in Python, with BotCity automation tools.

- Python
- BotCity Framework Web - Python

### Links:

- #### Python
  - https://www.python.org/

- #### BotCity Resources
    - https://www.botcity.dev/
    - https://botcity.atlassian.net/wiki/spaces/CBG/overview
    - https://www.youtube.com/channel/UCMa1T08wvhxiG0rcm8Yh9Rw
  
- #### <a href="www.linkedin.com/in/victor-hugo-souza-ferreira"> My LinkedIn Profile / Meu perfil no Linkedin </a>  
### Important things to make it run / Detalhes importantes para fazer funcionar:

- I used Decouple Library to read .env files, where my login was stored / Eu usei a biblioteca Decouple para ler arquivos .env, onde meu login estava armazenado.
- You have to create a .env file with you login credentials inside 'SpotiBot' folder, on the same location of 'bot.py' file (or you can configure it manually). The default environment variables are 'USER_LOGIN' and 'USER_PASSWORD' / Você tem que criar um arquivo .env contendo suas credenciais de login dentro pasta 'SpotiBot', no mesmo local do arquivo 'bot.py' (ou você pode configurar manualmente). O váriaveis de ambiente padrão são 'USER_LOGIN' e 'USER_PASSWORD'
- There is a variable inside 'action' method called 'listening_on_desktop', set it to 'True' if you are using the bot to mute and skip ads, but listening on the spotify desktop app. / Há uma variável dentro do método 'action' chamada 'listening_on_desktop', defina seu valor como 'True' se você está usando o bot para mutar e pular os anúncios, mas está ouvindo no aplicativo desktop do spotify.