from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from emoji import emojize
from urllib2 import urlopen, URLError
from bs4 import BeautifulSoup
import urllib2
import re
import json
import telegram
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
#from pyjsonrpc import ServiceProxy

#class DecimalEncoder(json.JSONEncoder):
#    def default(self, o):
#        if isinstance(o, decimal.Decimal):
#            return float(o)
#        return super(DecimalEncoder, self).default(o)

# Enable logging

def get_pretty_print(json_object):
    return json.dumps(json_object, sort_keys=True, indent=4, separators=(',', ': '))

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:29513"%('dingle','dingus'))
# Define a few command handlers. These usually take the two arguments bot and# update. Error handlers also receive the raised TelegramError object in error.

def main():
        updater = Updater("472892918:AAFr2EgVJsNCH7d6D7gM9Wg3wf91hoqigD0")
        bot = telegram.Bot("472892918:AAFr2EgVJsNCH7d6D7gM9Wg3wf91hoqigD0")
#       rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%('dingle','dingus'))
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("wallet", wallet))
        dp.add_handler(CommandHandler("charts", charts))
        dp.add_handler(CommandHandler("exchanges", exchanges))
        dp.add_handler(CommandHandler("snapshot", snap))
        dp.add_handler(CommandHandler("wat", wat))
        dp.add_handler(CommandHandler("rules", rules))
        dp.add_handler(CommandHandler("donation", donation))
        dp.add_handler(CommandHandler("getblockcount", getblockcount))
        dp.add_handler(CommandHandler("getrawmempool", getrawmempool))
        dp.add_handler(CommandHandler("guides", guides))
        dp.add_handler(CommandHandler("getinfo", getinfo))
        dp.add_handler(CommandHandler("readme", readme))
        dp.add_error_handler(error)
        dp.add_handler(CommandHandler("addnode", addnode))
        dp.add_handler(CommandHandler("getblockhash", getblockhash, pass_args=True))
        dp.add_handler(CommandHandler("toadinfo",toadinfo))
        updater.start_polling()
        updater.idle()
def toadinfo(bot, update):
        texto = "masternodes.online/currencies/MEME"
        update.message.reply_text(texto)

def rules(bot, update):
        emoji = emojize(":frog:", use_aliases=True)
        texto = "PepeCoin"+emoji+"Memetic"+emoji+"Kekdaq  "
        texto +="Official Telegram\n"
        texto +="Welcome!"
        texto +="\nChatroom Rules: \n" + "1-No shilling other coins"
        texto +="\n2-No market manipulation\n3-No asking for signal/target\n"
        texto +="4-braise geg\n\n"
        texto +="Info, Websites, Resources\n"
        texto +="memetic.ai\nexplorer.memetic.ai\n"
        texto +="\n\nhttps://bitcointalk.org/index.php?topic=1391598"
        texto +="\n\nhttps://medium.com/@pepecoins/pepecoin-a-year-in-review-2017-edition-4940f6fe3e1c"
        texto +="\n                                     Shadilay! " + emoji
        update.message.reply_text(texto)
def wallet(bot, update):
    
        url = "https://api.github.com/repos/pepeteam/pepecoin/releases/latest"
        try:
                resp = urlopen(url)
        except URLError as e:
                logger.warning("ERROR WITH URL FETCH - " + e.reason)
        resp_dict = json.load(resp)
        update.message.reply_text(resp_dict['html_url'])
#        bot.send_message(chat_id=update.message.chat_id,text=resp_dict['html_url'],disable_web_page_preview="true")
def addnode(bot, update):
        textout = "addnode=seed.pepecoin.net\naddnode=seed.kekdaq.com\naddnode=seed.memetic.ai"
        update.message.reply_text(textout)
def snap(bot, update):
        url ='http://snap.pepecoin.net/latest.tar.gz'
        url += '\n\nsnapshot instructions:\nview.publitas.com/memetic-pepecoin/snapshot-guide/'
	url += '\n\nsnapshot video:\nwww.youtube.com/watch?v=Ig20aP-K_nY'
        bot.send_message(chat_id=update.message.chat_id,text=url,disable_web_page_preview="false")
def getblockhash(bot, update, args):
        if not len(args):
                update.message.reply_text("what block pls ser")
        else:
                req = args[0]
                if req.isnumeric():
                        try:
                                update.message.reply_text(rpc_connection.getblockhash(int(req)))
                        except:
                                update.message.reply_text("OOOOOOOOOOPS")
                else:
                        update.message.reply_text("Gimme a number nigga")
def getinfo(bot, update):
        texto = ""
        rpc_dict = rpc_connection.getinfo()
#       for items in rpc_dict:
        del rpc_dict['errors']
#       del rpc_dict['paytxfee']
        del rpc_dict['keypoololdest']
        del rpc_dict['ip']
        del rpc_dict['connections']
        del rpc_dict['stake']
#       del rpc_dict['smugsend_balance']
#       del rpc_dict['difficulty']
        del rpc_dict['keypoolsize']
        del rpc_dict['mininput']
        del rpc_dict['balance']
        del rpc_dict['newmint']
        del rpc_dict['walletversion']
        del rpc_dict['timeoffset']
        del rpc_dict['proxy']
        del rpc_dict['testnet']
        del rpc_dict['smugsend_balance']
        texto = '\n'.join(":".join((str(k),str(v))) for k,v in rpc_dict.items())
        texto = texto.replace('difficulty:{u\'proof-of-stake\': Decimal(\'','POS diff: ')
        texto = texto.replace('\'), u\'proof-of-work\': Decimal(\'','\nPOW diff: ')
        texto = texto.replace('\')}',' ')
        texto = texto.replace('version:','ver:')
#               for values in rpc_dict[items]:
#@                      texto = '\n'.join(rpc_dict[items],':',values)
#       test_dict = json.loads(text_str)
        update.message.reply_text(texto)
def error(bot, update, error):
        logger.warning('Update "%s" caused error "%s"', update, error)
def charts(bot, update):
        mesg = "CMC Charts & Stats\nhttp://www.coinmarketcap.com/currencies/memetic/"
        mesg += "\nTradingView Charts\nhttps://www.tradingview.com/symbols/MEMEBTC/"
        mesg += "\nNomics Charts & Stats\nhttps://nomics.com/markets/meme-memetic--pepecoin/btc-bitcoin"
        bot.send_message(chat_id=update.message.chat_id,text=mesg,disable_web_page_preview="true")
def exchanges(bot, update):
        mesg = "Bittrex\nhttps://bittrex.com/Market/Index?MarketName=BTC-MEME"
        mesg += "\nCoinExchange\nhttps://www.coinexchange.io/market/MEME/BTC"
        mesg += "\nChangeNOW\nhttps://changenow.io/exchange?&from=btc&to=meme"
        bot.send_message(chat_id=update.message.chat_id,text=mesg,disable_web_page_preview="true")        
def wat(bot, update):
        bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/pepe/wat.jpg', 'rb'))
def guides(bot, update):
        mesg = "Running local (Non-VPS) MT\nview.publitas.com/memetic-pepecoin/local-mastertoad-guide/"
        mesg = mesg + "\nRunning VPS MT\nview.publitas.com/memetic-pepecoin/mastertoad-vps/"
        mesg += "\nVideo Guide for MT VPS\nhttps://youtu.be/lPKAHluBQOY"
        mesg += "\nCheatSheet for easy copy/paste\nhttp://snap.pepecoin.net/misc/cheatsheet.txt"
        mesg += "\nRunning VPS MT (Korean)\nview.publitas.com/memetic-pepecoin/korean-mastertoad-guide/"
        mesg += "\nNODEshare Subscription + Guide\nwww.nodeshare.in/memetic-masternode-setup-guide/"
        mesg = mesg + "\nKekdaq Guide (ALPHA)\nview.publitas.com/memetic-pepecoin/kekdaq-burning/"
        mesg += "\nUsing Blockchain Snapshot\nview.publitas.com/memetic-pepecoin/snapshot-guide/"
        bot.send_message(chat_id=update.message.chat_id,text=mesg,disable_web_page_preview="true")
def readme(bot, update):
        texto = "https://github.com/pepeteam/pepecoin/blob/master/README.md"
        update.message.reply_text(texto)        
def donation(bot,update):
        messaged = "Buy tendies to grease up keyboard\n\n"
        messaged = messaged + "PKmyFVEf94N6DDP9opvncgei8bCRC6M6KZ"
        messaged = messaged + "Bot created by @freeman, maintained by @damoos3"
        update.message.reply_text(messaged)

def getblockcount(bot,update):
        update.message.reply_text(rpc_connection.getblockcount())
def getrawmempool(bot,update):
         update.message.reply_text(rpc_connection.getrawmempool())
    



if __name__ == '__main__':
        main()
