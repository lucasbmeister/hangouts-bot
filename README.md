# hangouts-bot

BOT escrito em python (3.8.3 [64]) que utiliza o Selenium driver para integração com Hangouts (Legacy).

Dentro do arquivo \datafiles\settings.config é possível configurar o bot:

[CONFIG]
chat=nome do chat

[WEATHER]
api_key=key do serviço https://api.weatherapi.com

Para executar é necessário que a instância do Chrome utilizada pelo Selenium esteja autenticada (logar na primeira execução e depois reiniciar o bot).
Comando para rodar: 

python run.py

Comandos:
 - !entrar : BOT entra no chat
 - !sair : BOT sai do chat
 - !bolsa : Retorna informações sobre a ação informada no parâmetro. Segundo parâmetro é opcional. Ex.: !bolsa tots3 [high] 
 - !traduzir : Traduz última mensagem enviada ou, o texto em parâmetro. Idioma destino é opcional. Ex.: !traduzir Hello [es] 
 - !covid : Mostrar status COVID atual para o Brasil ou, país em parâmetro. Ex. !covid [US] 
 - !xeule : Remove paywall do ultimo link enviado ou em parametro 
 - !lancamento : Próximo lançamento de foguete. Aceita parâmetro. Ex.: !lancamento [spacex] 
 - !previsao : Retorna o clima atual ou os próximos dias conforme parâmetro. Ex.: !previsao [2] //retorna previsão para daqui dois dias 
 - !dolar : Retorna cotação do dia do dólar 
 - !euro : Retorna cotação do dia do euro 
 - !libra : Retorna cotação do dia da libra esterlina 
 - !bitcoin : Retorna cotação do dia do bitcoin 
 - !moeda : Retorna cotação da moeda em parâmetro em reais. Ex.: !moeda [USDT] 
 - !includes : Retorna pasta das includes do protheus 
 - !meme : Retorna link de um meme do Reddit (EN) 
 - !charada : Retorna uma charada bem bosta 
 - !resposta : Retorna a resposta da ultima charada 
 - !cow : Mostra uma vaca 
 - !bomdia : Responde bom dia educadamente 
 - !comandos : Retorna esta lista 
