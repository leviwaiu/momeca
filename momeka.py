import discord
import random
from functionality.reaction import Reaction
from functionality.storedLinks import StoredLinks


class MyClient(discord.Client):

    feed_count = 0
    #dictionary for pictures
    stored = StoredLinks();

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

        #feeding food to Momeca
        if message.content.startswith('.feed'):
            if message.content.strip() == '.feed':
                await message.channel.send("Momeca is curious what food Momeca is gonna receive".format(message))
                return
            msg = message.content[5:].strip()
            if msg == 'fish':
                MyClient.feed_count += 1
                send = "Momeca is happy!"
            elif msg == 'lemon':
                send = "nooooOOOOO! >A<"
            elif msg == 'total':
                send = "Momeca has eaten " + str(MyClient.feed_count) + " fish!( ﾟ▽ﾟ)/ "
            else:
                send = "_The food has been stolen by a mysterious shadow_"

        if message.content.startswith('.momeca'):
            if message.content.strip() == '.momeca':
                await message.channel.send("もめかかもね∼".format(message))
                return
            msg = message.content[7:].strip().lower()
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
                send = "Type .feed fish to feed Momeca ((^∀^*))"
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

        #help command to display usable commands
        if message.content.startswith('.help'):
            if message.content.strip() == '.help':
                await message.author.send((
                                                   "Type .help and the below command for a list of pictures in that category ( ´ ▽ \` )ノ" + '\n' +
                                                   "general: This is a list of pictures that Momeca found on Momeca's adventures ㄟ(≧◇≦)ㄏ" +
                                                   '\n' + "unique: This is Momeca's observation log of the server members (๑•̀ㅁ•́๑)✧" + '\n' +
                                                   "✧･ﾟ: \*✧･ﾟ:\*:･ﾟ✧\*:･ﾟ✧✧･ﾟ: \*✧･ﾟ:\*:･ﾟ✧\*:･ﾟ✧" +'\n' +
                                                   "Type .reply [image_name] to obtain an image from Momeca's picture collection" +
                                                   '\n' + "Type .feed fish to feed Momeca ((^∀^*))  Please only feed me fish! (not lemon or anything else!)" +
                                                   '\n' + "Type .momeca to interact with Momeca" + '\n' +
                                                   "✧･ﾟ: \*✧･ﾟ:\*:･ﾟ✧\*:･ﾟ✧✧･ﾟ: \*✧･ﾟ:\*:･ﾟ✧\*:･ﾟ✧" +
                                                   '\n' + "Momeca will only do the below commands for special members (active members currently have permission for the sake of testing!)" +
                                                   '\n' + "Type .addu or .addg [image_name] [image_link] to add a picture into Momeca's collection  ( ´ ▽ \` )ノ " +
                                                   '\n' + "Type .editu or .editg [image_name] [image_link] to update a picture in Momeca's collection ( • ̀ω•́ )✧ " +
                                                   '\n' + "Type .deleteu or .deleteg [image_name] to delete a picture in Momeca's collection (｡•́︿•̀｡)").format(
                    message))
                return
            msg = message.content[6:].strip()
            #help command to display general pictures
            if msg == 'general':
                send = "Here is a list of pictures that Momeca found on Momeca's adventures ㄟ(≧◇≦)ㄏ" + '\n'
                for genReact in MyClient.stored.reactToLinkG:
                    send += genReact + '\n'
            #help command to display unique pictures
            elif msg == 'unique':
                send = "Here is Momeca's observation log of the server members (๑•̀ㅁ•́๑)✧"
                for uniReact in MyClient.stored.reactToLinkU:
                    send += uniReact + '\n'
            else:
                send = "Momeca will only answer if you ask properly (｀へ´)=3"

        #make changes to key pair in dictionary and text file
        if message.content.startswith('.add') or message.content.startswith('.edit') or message.content.startswith('.delete'):
            send = MyClient.stored.update(message.content, [role.id for role in message.author.roles])

                
        #sends a link of a picture using the dictionary
        if message.content.startswith('.reply'):
            react = Reaction(MyClient.stored.reactToLinkU, MyClient.stored.reactToLinkG)
            send = react.react(message.content)

        if send != '':
            await message.channel.send(send.format(message))



client = MyClient()
client.run('NTk1NTA5MjcxNTg0NzAyNDkw.XRsBrQ.lQwm9aG_Uk3E_yWIKvtahKP2aG0')
