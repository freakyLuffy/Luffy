from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def quote(bot, update):
    url = 'https://anime-chan.herokuapp.com/api/quotes/random'
    r = requests.get(url)
    data = r.json()[0]
    new_text="_{}_".format(data['quote'])
    new_char="*{}*".format(data['character'])
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text= "Quote: "+new_text+'\n'+'\n'+" "+"*-*"+new_char,parse_mode='Markdown')

def bop(bot, update):
    url = get_image_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def start(bot, update):
    bot.send_message(chat_id=update.effective_chat.id, text="Heya! I'm Luffy, a bot with random collection of images of dogs. Try sending me a '/bop'")

def main():
    updater = Updater('1133372318:AAGqkAt77Tv2Cah74ODMa5I0O30T352-jjA')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('quote',quote))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
