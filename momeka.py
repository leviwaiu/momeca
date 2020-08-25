import discord
import random
from functionality.reaction import Reaction
from functionality.storedLinks import StoredLinks

class MyClient(discord.Client):

    feed_count = 0
    #dictionary for pictures
    stored = StoredLinks();
    userIdToYes = {511514664731934720:"<:art_yes:653453533894541343>",
                   187217072768548864:"<:mat_yes:653453592337842177>",
                   257143466931388416:"<:ramen_yes:653212656269787159>",
                   458189536460144641:"<:jas_yes:653453549375848478>",
                   277001583370305557:"<:bev_yes:653212526049492992>",
                   513615775039356932:"<:wings_yes:653453576424914955>",
                   554408249366020138:"<:van_yes:653132743428800512>",
                   571566359150854165:"<:que_yes:653453560499011584>",}

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        #makes send empty every time to keep the message
        send = ''

        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.lower().startswith('m-'):
            if message.content.strip() == 'm-':
                await message.channel.send("もめかかもね∼".format(message))
                return
            msg = message.content[2:].strip().lower()
            num = random.random()
            if 'hello' in msg:
                await message.channel.send("(●っゝω・)っ～☆HELLO☆" + str(message.author.nick) + "!" .format(message))
            elif 'pat' in msg:
                if num < 0.9:
                    send = "Momeca is happy! (✿´ ꒳ ` )"
                else:
                    send = "Momeca pats you back ✲ﾟ｡.(✿╹◡╹)ﾉ☆.｡₀:*ﾟ"
            elif 'love' in msg:
                if any(ids in MyClient.stored.adminRoleId for ids in [role.id for role in message.author.roles]):
                    send = "Momeca loves you too (,,•﹏•,,)"
                else:
                    send = "Momeca loves fish too (\*ฅ́˘ฅ̀\*) .｡.:*♡"
            elif 'feed' in msg:
                send = "Type m-feed fish to feed Momeca ((^∀^*))"
            elif 'poke' in msg:
                if num < 0.9:
                    send = "Momeca pokes back with beak"
                elif num < 0.99:
                    send = "Momeca used drill peck! It's super effective!"
                else:
                    send = "Momeca forgives you uwu"
            else:
                if num < 0.5:
                    send = "Momeca does not understand"
                elif num < 0.75:
                    send = "Momeca does not understand what you're talking about but pretends to know exactly what you're talking about"
                else:
                    send = "もめかかもね∼"
                    
        #feeding food to Momeca
        if message.content.lower().startswith('m-feed'):
            if message.content.strip() == 'm-feed':
                await message.channel.send("Momeca is curious what food Momeca is gonna receive".format(message))
                return
            msg = message.content[6:].strip()
            if msg == 'fish':
                MyClient.feed_count += 1
                send = "Momeca is happy!"
            elif msg == 'lemon':
                send = "nooooOOOOO! >A<"
            elif msg == 'total':
                send = "Momeca has eaten " + str(MyClient.feed_count) + " fish!( ﾟ▽ﾟ)/ "
            else:
                send = "_The food has been stolen by a mysterious shadow_"

        #help command to display usable commands
        if message.content.lower().startswith('m-help'):
            if message.content.lower().strip() == 'm-help':
                await message.author.send((
                                                   "Type m-help and the below command for a list of pictures in that category ( ´ ▽ \` )ノ" + '\n' +
                                                   "general: This is a list of pictures that Momeca found on Momeca's adventures ㄟ(≧◇≦)ㄏ" +
                                                   '\n' + "unique: This is Momeca's observation log of the server members (๑•̀ㅁ•́๑)✧" + '\n' +
                                                   "✧･ﾟ: \*✧･ﾟ:\*:･ﾟ✧\*:･ﾟ✧✧･ﾟ: \*✧･ﾟ:\*:･ﾟ✧\*:･ﾟ✧" +'\n' +
                                                   "Type m-reply [image_name] to obtain an image from Momeca's picture collection" +
                                                   '\n' + "Type m-feed fish to feed Momeca ((^∀^*))  Please only feed me fish! (not lemon or anything else!)" +
                                                   '\n' + "Type m- to interact with Momeca" +
                                                   '\n' + "Type m-ready when you are ready for a voice chat" + '\n' +
                                                   "✧･ﾟ: \*✧･ﾟ:\*:･ﾟ✧\*:･ﾟ✧✧･ﾟ: \*✧･ﾟ:\*:･ﾟ✧\*:･ﾟ✧" +
                                                   '\n' + "Type m-addu or m-addg [image_name] [image_link] to add a picture into Momeca's collection  ( ´ ▽ \` )ノ " +
                                                   '\n' + "Type m-editu or m-editg [image_name] [image_link] to update a picture in Momeca's collection ( • ̀ω•́ )✧ " +
                                                   '\n' + "Type m-deleteu or m-deleteg [image_name] to delete a picture in Momeca's collection (｡•́︿•̀｡)" +
                                                   '\n' + "Momeca will only modify the unique collection for special members").format(message))
                return
            msg = message.content[7:].lower().strip()
            #help command to display general pictures
            if msg == 'general':
                send = "Here is a list of pictures that Momeca found on Momeca's adventures ㄟ(≧◇≦)ㄏ" + '\n'
                for genReact in MyClient.stored.reactToLinkG:
                    send += genReact + '\t'
            #help command to display unique pictures
            elif msg == 'unique':
                send = "Here is Momeca's observation log of the server members (๑•̀ㅁ•́๑)✧" + '\n'
                for uniReact in MyClient.stored.reactToLinkU:
                    send += uniReact + '\t'
            else:
                send = "Momeca will only answer if you ask properly (｀へ´)=3"


        #make changes to key pair in dictionary and text file
        if message.content.lower().startswith('m-add') or message.content.lower().startswith('m-edit') or message.content.lower().startswith('m-delete'):
            send = MyClient.stored.update(message.content, [role.id for role in message.author.roles])

                
        #sends a link of a picture using the dictionary
        if message.content.lower().startswith('m-reply'):
            react = Reaction(MyClient.stored.reactToLinkU, MyClient.stored.reactToLinkG)
            send = react.react(message.content)
            if send.startswith('https://'):
                embed = discord.Embed(colour=message.author.color.value)
                embed.add_field(name="Reaction",value=message.content.split()[1])
                embed.set_image(url = send)
                await message.channel.send(embed=embed)
                send = ''

        if message.content.lower().startswith('m-ready'):
            send = 'Someone is ready to start a voice chat! Momeca wants to know who is free to join(*^▽^*) @everyone'
            msg = await message.channel.send(send.format(message))
            send = ''
            if message.author.id in MyClient.userIdToYes:
                await msg.add_reaction(MyClient.userIdToYes[message.author.id])

        if send != '':
            msg = await message.channel.send(send.format(message))
            return


token = 'NjYxMzExOTA3MjczMjQ0Njcz.XgppZQ.nRVrwqex6h4HBIHJPWabhlhTVLQ'
client = MyClient()
client.run(token)

