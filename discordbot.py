from discord.ext import commands
import os
import traceback
import random
import discord

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)
    if message.content.startswith("こんばんは"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "こんばんは" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)
    if message.content.startswith("!dice"):
         # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # 入力された内容を受け取る
            say = message.content 

            # [!dice ]部分を消し、AdBのdで区切ってリスト化する
            order = say.strip('!dice ')
            cnt, mx = list(map(int, order.split('d'))) # さいころの個数と面数
            dice = diceroll(cnt, mx) # 和を計算する関数(後述)
            await message.channel.send(dice[cnt])
            del dice[cnt]

            # さいころの目の総和の内訳を表示する
            await message.channel.send(dice)

def diceroll(cnt, max):
    total = 0
    num_list = []
    for i in range(0, cnt):
        # ランダムに1からサイコロの面数までの和を取得しリストに入れる
        num = random.randint(1, max)
        num_list.append(num)
    # さいころの目の総和を計算しリストに入れる
    total = sum(num_list)
    num_list.append(total)
    return num_list           
 
bot.run(token)
