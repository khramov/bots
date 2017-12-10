# -*- coding: utf-8 -*-
import config
import telebot
import wordLoader
import gameState
import random
import sys

bot = telebot.TeleBot(config.token)
top100List = [];
top1000List = [];
dictChats = {}

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, word.value)
	return

@bot.message_handler(commands=['top100'])
def top100(message):
	chatId = message.chat.id
	chatState = getState(chatId)
	chatState.topDict = top100List
	bot.send_message(message.chat.id, "Bot have been switched to top 100 mod")

@bot.message_handler(commands=['top1000'])
def top1000(message):
	chatId = message.chat.id
	chatState = getState(chatId)
	chatState.topDict = top100List
	bot.send_message(message.chat.id, "Bot have been switched to top 1000 mod")

@bot.message_handler(commands=['next'])
def next(message):
	chatId = message.chat.id
	chatState = getState(chatId)
	topDict = chatState.topDict
	word = topDict[random.randint(0, len(topDict))]
	bot.send_message(message.chat.id, word.value)
	bot.send_message(message.chat.id, "To see next word click /next")

@bot.message_handler(commands=['translate'])
def translate(message):
	chatId = message.chat.id
	chatState = getState(chatId)
	chatState.start()
	topDict = dictChats[chatId].topDict
	word = topDict[random.randint(0, len(topDict))]
	chatState.setWord(word)
	chatState.waitTranslation()
	bot.send_message(message.chat.id, word.value)

@bot.message_handler(content_types=["text"])
def checkText(message):
	chatId = message.chat.id
	chatState = getState(chatId)
	if chatState.state == gameState.states["WaitTranslation"]:
		valid = chatState.word.isTranslationValid(message.text)
		if valid:
			bot.send_message(message.chat.id, "Correct! Translation is %s" % chatState.word.translation)
		else:
			bot.send_message(message.chat.id, "Incorrect! Correct translation is %s" % chatState.word.translation)
		chatState.stop()
		bot.send_message(message.chat.id, "To translate next word click /translate")
	else:
		print("Chat %s is not waiting for tranlation" % chatId)
		bot.send_message(message.chat.id, "después")

def getState(chatId):
	if chatId not in dictChats:
		dictChats[chatId] = gameState.GameState()
		dictChats[chatId].topDict = top100List
	return dictChats[chatId]

if __name__ == '__main__':
	bot.set_webhook('')
	top100List = wordLoader.readTop100()
	top1000List = wordLoader.readTop1000()
	print("Dictionaries loaded")
	bot.polling(none_stop=True)
