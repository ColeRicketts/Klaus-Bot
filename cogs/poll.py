import discord
from discord.ext import commands
import sqlite3
from random import randint
import json
client = commands.Bot(command_prefix='!')

with open('config.json') as configFile:
    data = json.load(configFile)
    for value in data["server_details"]:
        bot_id = value['bot_id']

tochange = False
validID = False
ticker=0
alphabetReactions = ["🇦", "🇧", "🇨", "🇩", "🇪", "🇫", "🇬", "🇭", "🇮", "🇯", "🇰", "🇱", "🇲", "🇳", "🇴", "🇵", "🇶", "🇷", "🇸", "🇹", "🇺", "🇻", "🇼", "🇽", "🇾", "🇿"]

class Poll(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Poll Online!')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.user_id == int(bot_id):
            pass
        else:
            dbconnect = sqlite3.connect('users.db')
            cursor = dbconnect.cursor()
            message_id = payload.message_id
            testMessageID = "(" + str(message_id) + ",)"
            usedMessages = cursor.execute("SELECT message_id FROM pollscreated").fetchall()
            for field in usedMessages:
                if testMessageID == str(field):
                    active = cursor.execute("SELECT active FROM pollscreated WHERE message_id = ?", [message_id]).fetchone()
                    if str(active) == "(1,)":
                        if payload.emoji.name == '🇦':
                            initalTotal = cursor.execute("SELECT message_id, option1 FROM pollscreated WHERE message_id = ?", [message_id]).fetchall()
                            for row in initalTotal:
                                print(row[1])
                                total = row[1] + 1
                                cursor.execute("UPDATE pollscreated SET option1 = ? WHERE message_id = ?", [total, message_id])
                        else:
                            cursor.execute("UPDATE pollscreated SET option1 = ? WHERE message_id = ?", [0, message_id])
                        if payload.emoji.name == '🇧':
                            initalTotal = cursor.execute("SELECT message_id, option2 FROM pollscreated WHERE message_id = ?", [message_id]).fetchall()
                            for row in initalTotal:
                                print(row[1])
                                total = row[1] + 1
                                cursor.execute("UPDATE pollscreated SET option2 = ? WHERE message_id = ?", [total, message_id])
                        else:
                            cursor.execute("UPDATE pollscreated SET option2 = ? WHERE message_id = ?", [0, message_id])
                        if payload.emoji.name == '🇨':
                            initalTotal = cursor.execute("SELECT message_id, option3 FROM pollscreated WHERE message_id = ?", [message_id]).fetchall()
                            for row in initalTotal:
                                print(row[1])
                                total = row[1] + 1
                                cursor.execute("UPDATE pollscreated SET option3 = ? WHERE message_id = ?", [total, message_id])
                        else:
                            cursor.execute("UPDATE pollscreated SET option3 = ? WHERE message_id = ?", [0, message_id])
                        if payload.emoji.name == '🇩':
                            initalTotal = cursor.execute("SELECT message_id, option4 FROM pollscreated WHERE message_id = ?", [message_id]).fetchall()
                            for row in initalTotal:
                                print(row[1])
                                total = row[1] + 1
                                cursor.execute("UPDATE pollscreated SET option4 = ? WHERE message_id = ?", [total, message_id])
                        else:
                            cursor.execute("UPDATE pollscreated SET option4 = ? WHERE message_id = ?", [0, message_id])
                        if payload.emoji.name == '🇪':
                            initalTotal = cursor.execute("SELECT message_id, option5 FROM pollscreated WHERE message_id = ?", [message_id]).fetchall()
                            for row in initalTotal:
                                print(row[1])
                                total = row[1] + 1
                                cursor.execute("UPDATE pollscreated SET option5 = ? WHERE message_id = ?", [total, message_id])
                        else:
                            cursor.execute("UPDATE pollscreated SET option5 = ? WHERE message_id = ?", [0, message_id])
                        if payload.emoji.name == '🇫':
                            initalTotal = cursor.execute("SELECT message_id, option6 FROM pollscreated WHERE message_id = ?", [message_id]).fetchall()
                            for row in initalTotal:
                                print(row[1])
                                total = row[1] + 1
                                cursor.execute("UPDATE pollscreated SET option6 = ? WHERE message_id = ?", [total, message_id])
                        else:
                            cursor.execute("UPDATE pollscreated SET option6 = ? WHERE message_id = ?", [0, message_id])
                        if payload.emoji.name == '🇬':
                            initalTotal = cursor.execute("SELECT message_id, option7 FROM pollscreated WHERE message_id = ?", [message_id]).fetchall()
                            for row in initalTotal:
                                print(row[1])
                                total = row[1] + 1
                                cursor.execute("UPDATE pollscreated SET option7 = ? WHERE message_id = ?", [total, message_id])
                        else:
                            cursor.execute("UPDATE pollscreated SET option7 = ? WHERE message_id = ?", [0, message_id])
                        if payload.emoji.name == '🇭':
                            initalTotal = cursor.execute("SELECT message_id, option8 FROM pollscreated WHERE message_id = ?", [message_id]).fetchall()
                            for row in initalTotal:
                                print(row[1])
                                total = row[1] + 1
                                cursor.execute("UPDATE pollscreated SET option8 = ? WHERE message_id = ?", [total, message_id])
                        else:
                            cursor.execute("UPDATE pollscreated SET option8 = ? WHERE message_id = ?", [0, message_id])
                        if payload.emoji.name == '🇮':
                            initalTotal = cursor.execute("SELECT message_id, option9 FROM pollscreated WHERE message_id = ?", [message_id]).fetchall()
                            for row in initalTotal:
                                print(row[1])
                                total = row[1] + 1
                                cursor.execute("UPDATE pollscreated SET option9 = ? WHERE message_id = ?", [total, message_id])
                        else:
                            cursor.execute("UPDATE pollscreated SET option9 = ? WHERE message_id = ?", [0, message_id])
                        if payload.emoji.name == '🇯':
                            initalTotal = cursor.execute("SELECT message_id, option10 FROM pollscreated WHERE message_id = ?", [message_id]).fetchall()
                            for row in initalTotal:
                                print(row[1])
                                total = row[1] + 1
                                cursor.execute("UPDATE pollscreated SET option10 = ? WHERE message_id = ?", [total, message_id])
                        else:
                            cursor.execute("UPDATE pollscreated SET option10 = ? WHERE message_id = ?", [0, message_id])
                        if payload.emoji.name == '🇰':
                            initalTotal = cursor.execute("SELECT message_id, option11 FROM pollscreated WHERE message_id = ?", [message_id]).fetchall()
                            for row in initalTotal:
                                print(row[1])
                                total = row[1] + 1
                                cursor.execute("UPDATE pollscreated SET option11 = ? WHERE message_id = ?", [total, message_id])
                        else:
                            cursor.execute("UPDATE pollscreated SET option11 = ? WHERE message_id = ?", [0, message_id])
                        if payload.emoji.name == '🇱':
                            initalTotal = cursor.execute("SELECT message_id, option12 FROM pollscreated WHERE message_id = ?", [message_id]).fetchall()
                            for row in initalTotal:
                                print(row[1])
                                total = row[1] + 1
                                cursor.execute("UPDATE pollscreated SET option12 = ? WHERE message_id = ?", [total, message_id])
                        else:
                            cursor.execute("UPDATE pollscreated SET option12 = ? WHERE message_id = ?", [0, message_id])
                        if payload.emoji.name == '🇲':
                            initalTotal = cursor.execute("SELECT message_id, option13 FROM pollscreated WHERE message_id = ?", [message_id]).fetchall()
                            for row in initalTotal:
                                print(row[1])
                                total = row[1] + 1
                                cursor.execute("UPDATE pollscreated SET option13 = ? WHERE message_id = ?", [total, message_id])
                        else:
                            cursor.execute("UPDATE pollscreated SET option13 = ? WHERE message_id = ?", [0, message_id])
                        if payload.emoji.name == '🇳':
                            initalTotal = cursor.execute("SELECT message_id, option14 FROM pollscreated WHERE message_id = ?", [message_id]).fetchall()
                            for row in initalTotal:
                                print(row[1])
                                total = row[1] + 1
                                cursor.execute("UPDATE pollscreated SET option14 = ? WHERE message_id = ?", [total, message_id])
                        else:
                            cursor.execute("UPDATE pollscreated SET option14 = ? WHERE message_id = ?", [0, message_id])
                        if payload.emoji.name == '🇴':
                            initalTotal = cursor.execute("SELECT message_id, option15 FROM pollscreated WHERE message_id = ?", [message_id]).fetchall()
                            for row in initalTotal:
                                print(row[1])
                                total = row[1] + 1
                                cursor.execute("UPDATE pollscreated SET option15 = ? WHERE message_id = ?", [total, message_id])
                        else:
                            cursor.execute("UPDATE pollscreated SET option15 = ? WHERE message_id = ?", [0, message_id])
                        if payload.emoji.name == '🇵':
                            initalTotal = cursor.execute("SELECT message_id, option16 FROM pollscreated WHERE message_id = ?", [message_id]).fetchall()
                            for row in initalTotal:
                                print(row[1])
                                total = row[1] + 1
                                cursor.execute("UPDATE pollscreated SET option16 = ? WHERE message_id = ?", [total, message_id])
                        else:
                            cursor.execute("UPDATE pollscreated SET option16 = ? WHERE message_id = ?", [0, message_id])
                        if payload.emoji.name == '🇶':
                            initalTotal = cursor.execute("SELECT message_id, option17 FROM pollscreated WHERE message_id = ?", [message_id]).fetchall()
                            for row in initalTotal:
                                print(row[1])
                                total = row[1] + 1
                                cursor.execute("UPDATE pollscreated SET option17 = ? WHERE message_id = ?", [total, message_id])
                        else:
                            cursor.execute("UPDATE pollscreated SET option17 = ? WHERE message_id = ?", [0, message_id])
                        if payload.emoji.name == '🇷':
                            initalTotal = cursor.execute("SELECT message_id, option18 FROM pollscreated WHERE message_id = ?", [message_id]).fetchall()
                            for row in initalTotal:
                                print(row[1])
                                total = row[1] + 1
                                cursor.execute("UPDATE pollscreated SET option18 = ? WHERE message_id = ?", [total, message_id])
                        else:
                            cursor.execute("UPDATE pollscreated SET option18 = ? WHERE message_id = ?", [0, message_id])
                        if payload.emoji.name == '🇸':
                            initalTotal = cursor.execute("SELECT message_id, option19 FROM pollscreated WHERE message_id = ?", [message_id]).fetchall()
                            for row in initalTotal:
                                print(row[1])
                                total = row[1] + 1
                                cursor.execute("UPDATE pollscreated SET option19 = ? WHERE message_id = ?", [total, message_id])
                        else:
                            cursor.execute("UPDATE pollscreated SET option19 = ? WHERE message_id = ?", [0, message_id])
                        if payload.emoji.name == '🇹':
                            initalTotal = cursor.execute("SELECT message_id, option20 FROM pollscreated WHERE message_id = ?", [message_id]).fetchall()
                            for row in initalTotal:
                                print(row[1])
                                total = row[1] + 1
                                cursor.execute("UPDATE pollscreated SET option20 = ? WHERE message_id = ?", [total, message_id])
                        else:
                            cursor.execute("UPDATE pollscreated SET option20 = ? WHERE message_id = ?", [0, message_id])
                        if payload.emoji.name == '🇺':
                            initalTotal = cursor.execute("SELECT message_id, option21 FROM pollscreated WHERE message_id = ?", [message_id]).fetchall()
                            for row in initalTotal:
                                print(row[1])
                                total = row[1] + 1
                                cursor.execute("UPDATE pollscreated SET option21 = ? WHERE message_id = ?", [total, message_id])
                        else:
                            cursor.execute("UPDATE pollscreated SET option21 = ? WHERE message_id = ?", [0, message_id])
                        if payload.emoji.name == '🇻':
                            initalTotal = cursor.execute("SELECT message_id, option22 FROM pollscreated WHERE message_id = ?", [message_id]).fetchall()
                            for row in initalTotal:
                                print(row[1])
                                total = row[1] + 1
                                cursor.execute("UPDATE pollscreated SET option22 = ? WHERE message_id = ?", [total, message_id])
                        else:
                            cursor.execute("UPDATE pollscreated SET option22 = ? WHERE message_id = ?", [0, message_id])
                        if payload.emoji.name == '🇼':
                            initalTotal = cursor.execute("SELECT message_id, option23 FROM pollscreated WHERE message_id = ?", [message_id]).fetchall()
                            for row in initalTotal:
                                print(row[1])
                                total = row[1] + 1
                                cursor.execute("UPDATE pollscreated SET option23 = ? WHERE message_id = ?", [total, message_id])
                        else:
                            cursor.execute("UPDATE pollscreated SET option23 = ? WHERE message_id = ?", [0, message_id])
                        if payload.emoji.name == '🇽':
                            initalTotal = cursor.execute("SELECT message_id, option24 FROM pollscreated WHERE message_id = ?", [message_id]).fetchall()
                            for row in initalTotal:
                                print(row[1])
                                total = row[1] + 1
                                cursor.execute("UPDATE pollscreated SET option24 = ? WHERE message_id = ?", [total, message_id])
                        else:
                            cursor.execute("UPDATE pollscreated SET option24 = ? WHERE message_id = ?", [0, message_id])
                        if payload.emoji.name == '🇾':
                            initalTotal = cursor.execute("SELECT message_id, option25 FROM pollscreated WHERE message_id = ?", [message_id]).fetchall()
                            for row in initalTotal:
                                print(row[1])
                                total = row[1] + 1
                                cursor.execute("UPDATE pollscreated SET option25 = ? WHERE message_id = ?", [total, message_id])
                        else:
                            cursor.execute("UPDATE pollscreated SET option25 = ? WHERE message_id = ?", [0, message_id])
            dbconnect.commit()
            dbconnect.close()

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.user_id == int(bot_id):
            pass
        else:
            dbconnect = sqlite3.connect('users.db')
            cursor = dbconnect.cursor()
            message_id = payload.message_id
            testMessageID = "(" + str(message_id) + ",)"
            usedMessages = cursor.execute("SELECT message_id FROM pollscreated").fetchall()
            for field in usedMessages:
                if testMessageID == str(field):
                    active = cursor.execute("SELECT active FROM pollscreated WHERE message_id = ?",
                                            [message_id]).fetchone()
                    if str(active) == "(1,)":
                        if payload.emoji.name == '🇦':
                            initalTotal = cursor.execute(
                                "SELECT message_id, option1 FROM pollscreated WHERE message_id = ?",
                                [message_id]).fetchall()
                            for row in initalTotal:
                                total = row[1] - 1
                                cursor.execute("UPDATE pollscreated SET option1 = ? WHERE message_id = ?",
                                               [total, message_id])
                        elif payload.emoji.name == '🇧':
                            initalTotal = cursor.execute(
                                "SELECT message_id, option2 FROM pollscreated WHERE message_id = ?",
                                [message_id]).fetchall()
                            for row in initalTotal:
                                total = row[1] - 1
                                cursor.execute("UPDATE pollscreated SET option2 = ? WHERE message_id = ?",
                                               [total, message_id])
                        elif payload.emoji.name == '🇨':
                            initalTotal = cursor.execute(
                                "SELECT message_id, option3 FROM pollscreated WHERE message_id = ?",
                                [message_id]).fetchall()
                            for row in initalTotal:
                                total = row[1] - 1
                                cursor.execute("UPDATE pollscreated SET option3 = ? WHERE message_id = ?",
                                               [total, message_id])
                        elif payload.emoji.name == '🇩':
                            initalTotal = cursor.execute(
                                "SELECT message_id, option4 FROM pollscreated WHERE message_id = ?",
                                [message_id]).fetchall()
                            for row in initalTotal:
                                total = row[1] - 1
                                cursor.execute("UPDATE pollscreated SET option4 = ? WHERE message_id = ?",
                                               [total, message_id])
                        elif payload.emoji.name == '🇪':
                            initalTotal = cursor.execute(
                                "SELECT message_id, option5 FROM pollscreated WHERE message_id = ?",
                                [message_id]).fetchall()
                            for row in initalTotal:
                                total = row[1] - 1
                                cursor.execute("UPDATE pollscreated SET option5 = ? WHERE message_id = ?",
                                               [total, message_id])
                        elif payload.emoji.name == '🇫':
                            initalTotal = cursor.execute(
                                "SELECT message_id, option6 FROM pollscreated WHERE message_id = ?",
                                [message_id]).fetchall()
                            for row in initalTotal:
                                total = row[1] - 1
                                cursor.execute("UPDATE pollscreated SET option6 = ? WHERE message_id = ?",
                                               [total, message_id])
                        elif payload.emoji.name == '🇬':
                            initalTotal = cursor.execute(
                                "SELECT message_id, option7 FROM pollscreated WHERE message_id = ?",
                                [message_id]).fetchall()
                            for row in initalTotal:
                                total = row[1] - 1
                                cursor.execute("UPDATE pollscreated SET option7 = ? WHERE message_id = ?",
                                               [total, message_id])
                        elif payload.emoji.name == '🇭':
                            initalTotal = cursor.execute(
                                "SELECT message_id, option8 FROM pollscreated WHERE message_id = ?",
                                [message_id]).fetchall()
                            for row in initalTotal:
                                total = row[1] - 1
                                cursor.execute("UPDATE pollscreated SET option8 = ? WHERE message_id = ?",
                                               [total, message_id])
                        elif payload.emoji.name == '🇮':
                            initalTotal = cursor.execute(
                                "SELECT message_id, option9 FROM pollscreated WHERE message_id = ?",
                                [message_id]).fetchall()
                            for row in initalTotal:
                                total = row[1] - 1
                                cursor.execute("UPDATE pollscreated SET option9 = ? WHERE message_id = ?",
                                               [total, message_id])
                        elif payload.emoji.name == '🇯':
                            initalTotal = cursor.execute(
                                "SELECT message_id, option10 FROM pollscreated WHERE message_id = ?",
                                [message_id]).fetchall()
                            for row in initalTotal:
                                total = row[1] - 1
                                cursor.execute("UPDATE pollscreated SET option10 = ? WHERE message_id = ?",
                                               [total, message_id])
                        elif payload.emoji.name == '🇰':
                            initalTotal = cursor.execute(
                                "SELECT message_id, option11 FROM pollscreated WHERE message_id = ?",
                                [message_id]).fetchall()
                            for row in initalTotal:
                                total = row[1] - 1
                                cursor.execute("UPDATE pollscreated SET option11 = ? WHERE message_id = ?",
                                               [total, message_id])
                        elif payload.emoji.name == '🇱':
                            initalTotal = cursor.execute(
                                "SELECT message_id, option12 FROM pollscreated WHERE message_id = ?",
                                [message_id]).fetchall()
                            for row in initalTotal:
                                total = row[1] - 1
                                cursor.execute("UPDATE pollscreated SET option12 = ? WHERE message_id = ?",
                                               [total, message_id])
                        elif payload.emoji.name == '🇲':
                            initalTotal = cursor.execute(
                                "SELECT message_id, option13 FROM pollscreated WHERE message_id = ?",
                                [message_id]).fetchall()
                            for row in initalTotal:
                                total = row[1] - 1
                                cursor.execute("UPDATE pollscreated SET option13 = ? WHERE message_id = ?",
                                               [total, message_id])
                        elif payload.emoji.name == '🇳':
                            initalTotal = cursor.execute(
                                "SELECT message_id, option14 FROM pollscreated WHERE message_id = ?",
                                [message_id]).fetchall()
                            for row in initalTotal:
                                total = row[1] - 1
                                cursor.execute("UPDATE pollscreated SET option14 = ? WHERE message_id = ?",
                                               [total, message_id])
                        elif payload.emoji.name == '🇴':
                            initalTotal = cursor.execute(
                                "SELECT message_id, option15 FROM pollscreated WHERE message_id = ?",
                                [message_id]).fetchall()
                            for row in initalTotal:
                                total = row[1] - 1
                                cursor.execute("UPDATE pollscreated SET option15 = ? WHERE message_id = ?",
                                               [total, message_id])
                        elif payload.emoji.name == '🇵':
                            initalTotal = cursor.execute(
                                "SELECT message_id, option16 FROM pollscreated WHERE message_id = ?",
                                [message_id]).fetchall()
                            for row in initalTotal:
                                total = row[1] - 1
                                cursor.execute("UPDATE pollscreated SET option16 = ? WHERE message_id = ?",
                                               [total, message_id])
                        elif payload.emoji.name == '🇶':
                            initalTotal = cursor.execute(
                                "SELECT message_id, option17 FROM pollscreated WHERE message_id = ?",
                                [message_id]).fetchall()
                            for row in initalTotal:
                                total = row[1] - 1
                                cursor.execute("UPDATE pollscreated SET option17 = ? WHERE message_id = ?",
                                               [total, message_id])
                        elif payload.emoji.name == '🇷':
                            initalTotal = cursor.execute(
                                "SELECT message_id, option18 FROM pollscreated WHERE message_id = ?",
                                [message_id]).fetchall()
                            for row in initalTotal:
                                total = row[1] - 1
                                cursor.execute("UPDATE pollscreated SET option18 = ? WHERE message_id = ?",
                                               [total, message_id])
                        elif payload.emoji.name == '🇸':
                            initalTotal = cursor.execute(
                                "SELECT message_id, option19 FROM pollscreated WHERE message_id = ?",
                                [message_id]).fetchall()
                            for row in initalTotal:
                                total = row[1] - 1
                                cursor.execute("UPDATE pollscreated SET option19 = ? WHERE message_id = ?",
                                               [total, message_id])
                        elif payload.emoji.name == '🇹':
                            initalTotal = cursor.execute(
                                "SELECT message_id, option20 FROM pollscreated WHERE message_id = ?",
                                [message_id]).fetchall()
                            for row in initalTotal:
                                total = row[1] - 1
                                cursor.execute("UPDATE pollscreated SET option20 = ? WHERE message_id = ?",
                                               [total, message_id])
                        elif payload.emoji.name == '🇺':
                            initalTotal = cursor.execute(
                                "SELECT message_id, option21 FROM pollscreated WHERE message_id = ?",
                                [message_id]).fetchall()
                            for row in initalTotal:
                                total = row[1] - 1
                                cursor.execute("UPDATE pollscreated SET option21 = ? WHERE message_id = ?",
                                               [total, message_id])
                        elif payload.emoji.name == '🇻':
                            initalTotal = cursor.execute(
                                "SELECT message_id, option22 FROM pollscreated WHERE message_id = ?",
                                [message_id]).fetchall()
                            for row in initalTotal:
                                total = row[1] - 1
                                cursor.execute("UPDATE pollscreated SET option22 = ? WHERE message_id = ?",
                                               [total, message_id])
                        elif payload.emoji.name == '🇼':
                            initalTotal = cursor.execute(
                                "SELECT message_id, option23 FROM pollscreated WHERE message_id = ?",
                                [message_id]).fetchall()
                            for row in initalTotal:
                                total = row[1] - 1
                                cursor.execute("UPDATE pollscreated SET option23 = ? WHERE message_id = ?",
                                               [total, message_id])
                        elif payload.emoji.name == '🇽':
                            initalTotal = cursor.execute(
                                "SELECT message_id, option24 FROM pollscreated WHERE message_id = ?",
                                [message_id]).fetchall()
                            for row in initalTotal:
                                total = row[1] - 1
                                cursor.execute("UPDATE pollscreated SET option24 = ? WHERE message_id = ?",
                                               [total, message_id])
                        elif payload.emoji.name == '🇾':
                            initalTotal = cursor.execute(
                                "SELECT message_id, option25 FROM pollscreated WHERE message_id = ?",
                                [message_id]).fetchall()
                            for row in initalTotal:
                                total = row[1] - 1
                                cursor.execute("UPDATE pollscreated SET option25 = ? WHERE message_id = ?",
                                               [total, message_id])
            dbconnect.commit()
            dbconnect.close()


    @client.command()
    async def rating(self, ctx, *, content):
        dbconnect = sqlite3.connect('users.db')
        cursor = dbconnect.cursor()
        customIdentifier: int = randint(1, 999999999999)
        testIdentifier = "("+str(customIdentifier)+",)"
        usedIdentifiers = cursor.execute("SELECT unique_code FROM pollscreated").fetchall()
        for field in usedIdentifiers:
            if str(field) == testIdentifier:
                customIdentifier = randint(1, 999999999999)
                testIdentifier = "(" + str(customIdentifier) + ",)"
        embedVar = discord.Embed(title="Rate: **{0}**".format(content), description="Give this a rating from 1 to 10! A-J is equal to 1-10!", color=0x9b59b6)
        embedVar.add_field(name="Called By:", value="**{0}**".format(ctx.author.mention), inline=False)
        embedVar.set_footer(text="Unique ID: {0}".format(customIdentifier))
        message = await ctx.send(embed=embedVar)
        for i in range(10):
            await message.add_reaction(alphabetReactions[i])
        cursor.execute('''INSERT INTO pollscreated(unique_code, message, message_id, channel_id, option1, option2, option3, option4, option5, option6, option7, option8, option9, option10, type, active) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (customIdentifier, content, ctx.channel.last_message_id, ctx.channel.id, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "Rating", 1))
        dbconnect.commit()
        dbconnect.close()

    @client.command()
    async def truefalse(self, ctx, *, content):
        dbconnect = sqlite3.connect('users.db')
        cursor = dbconnect.cursor()
        customIdentifier: int = randint(1, 999999999999)
        testIdentifier = "(" + str(customIdentifier) + ",)"
        usedIdentifiers = cursor.execute("SELECT unique_code FROM pollscreated").fetchall()
        for field in usedIdentifiers:
            if str(field) == testIdentifier:
                customIdentifier = randint(1, 999999999999)
                testIdentifier = "(" + str(customIdentifier) + ",)"
        embedVar = discord.Embed(title="T or F: **{0}**".format(content), description="Is it true or false?", color=0x9b59b6)
        embedVar.add_field(name="Called By:", value="**{0}**".format(ctx.author.mention), inline=False)
        embedVar.set_footer(text="Unique ID: {0}".format(customIdentifier))
        message = await ctx.send(embed=embedVar)
        await message.add_reaction("🇹")
        await message.add_reaction("🇫")
        cursor.execute('''INSERT INTO pollscreated(unique_code, message, message_id, channel_id, option6, option20, type, active) VALUES(?,?,?,?,?,?,?,?)''', (customIdentifier, content, ctx.channel.last_message_id, ctx.channel.id, 0, 0, "TrueFalse", 1))
        dbconnect.commit()
        dbconnect.close()

    @client.command()
    async def poll(self, ctx, *, content):
        dbconnect = sqlite3.connect('users.db')
        cursor = dbconnect.cursor()
        customIdentifier: int = randint(1, 999999999999)
        testIdentifier = "(" + str(customIdentifier) + ",)"
        usedIdentifiers = cursor.execute("SELECT unique_code FROM pollscreated").fetchall()
        for field in usedIdentifiers:
            if str(field) == testIdentifier:
                customIdentifier = randint(1, 999999999999)
                testIdentifier = "(" + str(customIdentifier) + ",)"
        itemCount = 0
        splitMessage = content.split(";")
        pollTitle = splitMessage[0]
        embedVar = discord.Embed(title="Pick: **{0}**".format(pollTitle), description="Pick an option!", color=0x9b59b6)
        for i in splitMessage:
            if i == pollTitle:
                pass
            else:
                embedVar.add_field(name="Option {0}:".format(alphabetReactions[itemCount-1]), value="{0}".format(i), inline=True)
            itemCount += 1
        embedVar.add_field(name="Called By:", value="**{0}**".format(ctx.author.mention), inline=True)
        embedVar.set_footer(text="Unique ID: {0}".format(customIdentifier))
        message = await ctx.send(embed=embedVar)
        itemCount = 0
        for i in splitMessage:
            if i == pollTitle:
                 pass
            else:
                await message.add_reaction(str(alphabetReactions[itemCount]))
                itemCount += 1
        cursor.execute('''INSERT INTO pollscreated(unique_code, message, message_id, channel_id, option1, option2, option3, option4, option5, option6, option7, option8, option9, option10, option11, option12, option13, option14, option15, option16, option17, option18, option19, option20, option21, option22, option23, option24, option25, type, active) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (customIdentifier, content, ctx.channel.last_message_id, ctx.channel.id, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "Strawpoll", 1))
        dbconnect.commit()
        dbconnect.close()


    @client.command()
    @commands.has_permissions(manage_channels=True)
    async def endpoll(self, ctx, identifier):
        dbconnect = sqlite3.connect('users.db')
        cursor = dbconnect.cursor()
        pollActive = cursor.execute("SELECT active FROM pollscreated WHERE unique_code = ?", [identifier]).fetchone()
        if pollActive:
            if str(pollActive) == "(1,)":
                pollType = cursor.execute("SELECT type FROM pollscreated WHERE unique_code = ?",
                                            [identifier]).fetchone()
                if str(pollType) == "('Rating',)":
                    pollMessage = cursor.execute("SELECT message FROM pollscreated WHERE unique_code = ?",
                                            [identifier]).fetchone()
                    pollMessage = str(pollMessage).split("'")
                    pollOptionCounts = cursor.execute("SELECT option1, option2, option3, option4, option5, option6, option7, option8, option9, option10 FROM pollscreated WHERE unique_code = ?",[identifier]).fetchone()
                    pollOptionCounts = str(pollOptionCounts).split("(")
                    pollOptionCounts = str(pollOptionCounts[1]).split(")")
                    pollOptionCounts = str(pollOptionCounts[0]).split(",")
                    winningVote = max(int(pollOptionCounts[0]), int(pollOptionCounts[1]), int(pollOptionCounts[2]), int(pollOptionCounts[3]), int(pollOptionCounts[4]), int(pollOptionCounts[5]), int(pollOptionCounts[6]), int(pollOptionCounts[7]), int(pollOptionCounts[8]), int(pollOptionCounts[9]))
                    for i in range(10):
                        testVote = int(pollOptionCounts[i])
                        if testVote == winningVote:
                            winningValue = alphabetReactions[i]
                            await ctx.send("POLL RESULTS ARE IN: The most popular result for the rating of **{0}** was **{1}** with **{2}** votes".format(pollMessage[1], winningValue, winningVote))
                if str(pollType) == "('TrueFalse',)":
                    pollMessage = cursor.execute("SELECT message_id, channel_id FROM pollscreated WHERE unique_code = ?", [identifier]).fetchone()
                    pollMessage = str(pollMessage).split("'")
                    pollOptionCounts = cursor.execute(
                        "SELECT option1, option2 FROM pollscreated WHERE unique_code = ?",
                        [identifier]).fetchone()
                    pollOptionCounts = str(pollOptionCounts).split("(")
                    pollOptionCounts = str(pollOptionCounts[1]).split(")")
                    pollOptionCounts = str(pollOptionCounts[0]).split(",")
                    winningVote = max(int(pollOptionCounts[0]), int(pollOptionCounts[1]))
                    for i in range(2):
                        testVote = int(pollOptionCounts[i])
                        if testVote == winningVote:
                            winningValue = alphabetReactions[i]
                            await ctx.send(
                                "POLL RESULTS ARE IN: The most popular result for the true or false of **{0}** was **{1}** with **{2}** votes".format(
                                    pollMessage[1], winningValue, winningVote))
                if str(pollType) == "('Strawpoll',)":
                    pollMessage = cursor.execute("SELECT message FROM pollscreated WHERE unique_code = ?",
                                                 [identifier]).fetchone()
                    pollMessage = str(pollMessage).split("'")
                    pollMessage = pollMessage[1].split(";")
                    pollOptionCounts = cursor.execute("SELECT option1, option2, option3, option4, option5, option6, option7, option8, option9, option10, option11, option12, option13, option14, option15, option16, option17, option18, option19, option20, option21, option22, option23, option24, option25 FROM pollscreated WHERE unique_code = ?",[identifier]).fetchone()
                    pollOptionCounts = str(pollOptionCounts).split("(")
                    pollOptionCounts = str(pollOptionCounts[1]).split(")")
                    pollOptionCounts = str(pollOptionCounts[0]).split(",")
                    winningVote = max(int(pollOptionCounts[0]), int(pollOptionCounts[1]), int(pollOptionCounts[2]), int(pollOptionCounts[3]), int(pollOptionCounts[4]), int(pollOptionCounts[5]), int(pollOptionCounts[6]), int(pollOptionCounts[7]), int(pollOptionCounts[8]), int(pollOptionCounts[9]), int(pollOptionCounts[10]), int(pollOptionCounts[11]), int(pollOptionCounts[12]), int(pollOptionCounts[13]), int(pollOptionCounts[14]), int(pollOptionCounts[15]), int(pollOptionCounts[16]), int(pollOptionCounts[17]), int(pollOptionCounts[18]), int(pollOptionCounts[19]), int(pollOptionCounts[20]), int(pollOptionCounts[21]), int(pollOptionCounts[22]), int(pollOptionCounts[23]), int(pollOptionCounts[24]))
                    for i in range(25):
                        testVote = int(pollOptionCounts[i])
                        if testVote == winningVote:
                            winningValue = alphabetReactions[i]
                            await ctx.send(
                                "POLL RESULTS ARE IN: The most popular result for the rating of **{0}** was **{1}** with **{2}** votes".format(
                                    pollMessage[0], pollMessage[i+1], winningVote))

            else:
                ctx.send("Poll is Inactive!")
        cursor.execute("UPDATE pollscreated SET active = 0 WHERE unique_code = ?", [identifier])
        dbconnect.commit()
        dbconnect.close()

def setup(client):
    client.add_cog(Poll(client))