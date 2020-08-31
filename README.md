
# Telegram Bot Prototype 

## Create a telegram bot
* create a bot in telegram: see [https://core.telegram.org/bots#6-botfather](https://core.telegram.org/bots#6-botfather)
* invite the telegram bot in your channel and give admin rights to the bot in order to delete messages
* copy the token of the bot into the TOKEN variable in Main.py

## Set up Main.py as cron job 
* pip install -r requirements.txt
* run Main.py as cronjob every 

## Program Description
The program checks for messages (last 100) and deletes any message, which contains the word "bitcoin" or "crypto". This results in deleting already deleted messages, because telegram does not differentiate between deleted messages and not deleted messages.

[Srceenshot1](https://github.com/davidh38/telegram_bot/docs/img1.png?raw=true "before")
[Srceenshot2](https://github.com/davidh38/telegram_bot/docs/img2.png?raw=true "message")
[Srceenshot3](https://github.com/davidh38/telegram_bot/docs/img3.png?raw=true "after job ran")

## Future Improvements
* it is probably better to have the program as webhook
* set up a database to check when people join in order to only check for messages of new members

## Hosting Cronjob on AWS lambda:
* rename Main.py in lamda_function.py
* create a lambda_handler(context, handler) function
* zip function.zip lambda_funcion.py
* create package directory
* pip3 install --target requests ./package
* cd package
* zip -r9 ../function.zip .
* upload function.zip to aws lambda and use cloudevents as trigger
