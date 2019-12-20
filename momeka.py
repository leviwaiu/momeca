import discord
import random

class MyClient(discord.Client):

    feed_count = 0
    #dictionary for pictures
    reactToLink = {}
    reactToLink2 = {}
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        unique = open("reactToLinkUni.txt",'r')
        for line in unique:
            pair = line.split()
            MyClient.reactToLink[pair[0]] = pair[1]
            print("added key " + pair[0] + " and value " + pair[1])
        unique.close()

        general = open("reactToLinkGen.txt",'r')
        for line in general:
            pair = line.split()
            MyClient.reactToLink2[pair[0]] = pair[1]
            print("added key " + pair[0] + " and value " + pair[1])
        general.close()

    async def on_message(self, message):   

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
                await message.channel.send("Momeca is happy!".format(message))
            elif msg == 'lemon':
                await message.channel.send("nooooOOOOO! >A<".format(message))
            elif msg == 'total':
                await message.channel.send("Momeca has eaten " + str(MyClient.feed_count) + " fish!( ﾟ▽ﾟ)/ ".format(message))
            else:
                await message.channel.send("_The food has been stolen by a mysterious shadow_".format(message))

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
                    await message.channel.send("Momeca is happy! (✿´ ꒳ ` )".format(message))
                else:
                    await message.channel.send("Momeca pats you back ✲ﾟ｡.(✿╹◡╹)ﾉ☆.｡₀:*ﾟ".format(message))
            elif 'love' in msg:
                if 511556749392609281 in [role.id for role in message.author.roles] or 511555135185354767 in [role.id for role in message.author.roles]:
                    await message.channel.send("Momeca loves you too (,,•﹏•,,)".format(message))
                else:
                    await message.channel.send("Momeca loves fish too (\*ฅ́˘ฅ̀\*) .｡.:*♡".format(message))
            elif 'feed' in msg:
                await message.channel.send("Type .feed fish to feed Momeca ((^∀^*))".format(message))
            elif 'poke' in msg:
                if num < 0.9:
                    await message.channel.send("Momeca pokes back with beak".format(message))
                elif num < 0.99:
                    await message.channel.send("Momeca used drill peck! It's super effective!".format(message))
                else:
                    await message.channel.send("Momeca forgives you uwu".format(message))
            else:
                if num < 0.5:
                    await message.channel.send("Momeca does not understand".format(message))
                elif num < 0.75:
                    await message.channel.send("Momeca does not understand what you're talking about but pretends to know exactly what you're talking about".format(message))
                else:
                    await message.channel.send("もめかかもね∼".format(message))

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
                                                   '\n' + "Momeca will only do the below commands for special members" +
                                                   '\n' + "Type .addu or .addg [image_name] [image_link] to add a picture into Momeca's collection  ( ´ ▽ \` )ノ " +
                                                   '\n' + "Type .editu or .editg [image_name] [image_link] to update a picture in Momeca's collection ( • ̀ω•́ )✧ " +
                                                   '\n' + "Type .deleteu or .deleteg [image_name] to delete a picture in Momeca's collection (｡•́︿•̀｡)").format(
                    message))
                return
            msg = message.content[6:].strip()
            #help command to display general pictures
            if msg == 'general':
                await message.author.send("Here is a list of pictures that Momeca found on Momeca's adventures ㄟ(≧◇≦)ㄏ ".format(message))
                genlst = ''
                for react in MyClient.reactToLink2:
                    genlst += react + '\n'
                await message.author.send(genlst.format(message))
            #help command to display unique pictures
            elif msg == 'unique':
                await message.author.send(
                    "Here is Momeca's observation log of the server members (๑•̀ㅁ•́๑)✧".format(
                        message))
                unilst = ''
                for react1 in MyClient.reactToLink:
                    unilst += react1 + '\n'
                await message.author.send(unilst.format(message))
            else:
                await message.channel.send("Momeca will only answer if you ask properly (｀へ´)=3".format(message))


        #adds new key pair to dictionary
        if message.content.startswith('.add'):
            if len(message.content.strip()) > 5:
                msg = message.content[5:].strip().split()
                if 511556749392609281 in [role.id for role in message.author.roles] or 511555135185354767 in [role.id for role in message.author.roles]:
                    if message.content[4] == 'u':
                        if len(msg) == 2 and msg[0] not in MyClient.reactToLink and msg[1].startswith("https://cdn.discordapp.com/attachments/"):
                            MyClient.reactToLink[msg[0]] = msg[1]
                            await message.channel.send("Momeca has added " + msg[0] + " to Momeca's unique collection!".format(message))
                            unilst = ''#test
                            for react1 in MyClient.reactToLink:
                                unilst += react1 + '\n'
                            print(unilst)#endtest
                            unique = open("reactToLinkUni.txt",'a')
                            unique.write(message.content[5:].strip() + '\n')
                            unique.close()
                        elif msg[0] in MyClient.reactToLink:
                            await message.channel.send("Momeca refuses to do anything because the name is already used! Type .edit to change the picture for the name ㄟ(≧◇≦)ㄏ".format(message))
                        else:
                            await message.channel.send("Momeca refuses to do anything because the format is not correct (｀へ´)=3".format(message))
                    elif message.content[4] == 'g':
                        if len(msg) == 2 and msg[0] not in MyClient.reactToLink2 and msg[1].startswith("https://cdn.discordapp.com/attachments/"):
                            MyClient.reactToLink2[msg[0]] = msg[1]
                            await message.channel.send("Momeca has added " + msg[0] + " to Momeca's general collection!".format(message))
                            genlst = ''#test
                            for react2 in MyClient.reactToLink2:
                                genlst += react2 + '\n'
                            print(genlst)#endtest
                            general = open("reactToLinkGen.txt",'a')
                            general.write(message.content[5:].strip() + '\n')
                            general.close()
                        elif msg[0] in MyClient.reactToLink2:
                            await message.channel.send("Momeca refuses to do anything because the name is already used! Type .edit to change the picture for the name ㄟ(≧◇≦)ㄏ".format(message))
                        else:
                            await message.channel.send("Momeca refuses to do anything because the format is not correct (｀へ´)=3".format(message))
                    else:
                        await message.channel.send("Momeca refuses to do anything because the format is not correct (｀へ´)=3".format(message))
                else:
                    await message.channel.send("Momeca refuses to do anything because you don't have permission (｀へ´)=3".format(message))
            else:
                await message.channel.send("もめかかもね∼".format(message))


        #edits existing key pair in dictionary
        if message.content.startswith('.edit'):
            if len(message.content.strip()) > 6:
                msg = message.content[6:].strip().split()
                if 511556749392609281 in [role.id for role in message.author.roles] or 511555135185354767 in [role.id for role in message.author.roles]:
                    if message.content[5] == 'u':
                        if len(msg) == 2 and msg[0] in MyClient.reactToLink and msg[1].startswith("https://cdn.discordapp.com/attachments/"):
                            MyClient.reactToLink[msg[0]] = msg[1]
                            await message.channel.send("Momeca has updated " + msg[0] + " in Momeca's unique collection!".format(message))
                            unilst = ''#test
                            for react1 in MyClient.reactToLink:
                                unilst += react1 + '\n'
                            print(unilst)#endtest
                            unique = open("reactToLinkUni.txt",'r')
                            contentsa = ''
                            contentsb = ''
                            line = unique.readline()
                            while msg[0] not in line:
                                contentsa += line
                                line = unique.readline()
                            line = unique.readline()
                            while line != '':
                                contentsb += line
                                line = unique.readline()
                            unique.close()
                            unique = open("reactToLinkUni.txt",'w')
                            unique.write(contentsa)
                            unique.write(message.content[6:].strip() + '\n')
                            unique.write(contentsb)
                            unique.close()
                        elif msg[0] not in MyClient.reactToLink:
                            await message.channel.send("Momeca refuses to do anything because Momeca hasn't seen this reaction before! Type .addu to add a new picture ㄟ(≧◇≦)ㄏ".format(message))
                        else:
                            await message.channel.send("Momeca refuses to do anything because the format is not correct (｀へ´)=3".format(message))
                    elif message.content[5] == 'g':
                        if len(msg) == 2 and msg[0] in MyClient.reactToLink2 and msg[1].startswith("https://cdn.discordapp.com/attachments/"):
                            MyClient.reactToLink2[msg[0]] = msg[1]
                            await message.channel.send("Momeca has updated " + msg[0] + " in Momeca's general collection!".format(message))
                            genlst = ''#test
                            for react2 in MyClient.reactToLink2:
                                genlst += react2 + '\n'
                            print(genlst)#endtest
                            general = open("reactToLinkGen.txt",'r')
                            contentsa = ''
                            contentsb = ''
                            line = general.readline()
                            while msg[0] not in line:
                                contentsa += line
                                line = general.readline()
                            line = general.readline()
                            while line != '':
                                contentsb += line
                                line = general.readline()
                            general.close()
                            general = open("reactToLinkGen.txt",'w')
                            general.write(contentsa)
                            general.write(message.content[6:].strip() + '\n')
                            general.write(contentsb)
                            general.close()
                        elif msg[0] not in MyClient.reactToLink2:
                            await message.channel.send("Momeca refuses to do anything because Momeca hasn't seen this reaction before! Type .addg to add a new picture ㄟ(≧◇≦)ㄏ".format(message))
                        else:
                            await message.channel.send("Momeca refuses to do anything because the format is not correct (｀へ´)=3".format(message))
                    else:
                        await message.channel.send("Momeca refuses to do anything because the format is not correct (｀へ´)=3".format(message))
                else:
                    await message.channel.send("Momeca refuses to do anything because you don't have permission (｀へ´)=3".format(message))
            else:
                await message.channel.send("もめかかもね∼".format(message))


        #deleting existing key-pair from dictionary
        if message.content.startswith('.delete'):
            if len(message.content.strip()) > 8:
                msg = message.content[8:].strip()
                if 511556749392609281 in [role.id for role in message.author.roles] or 511555135185354767 in [role.id for role in message.author.roles]:
                    if message.content[7] == 'u' and msg in MyClient.reactToLink:
                        await message.channel.send("Momeca has deleted " + msg + " from Momeca's unique collection (˘•ω•˘)" + MyClient.reactToLink[msg].format(message))
                        MyClient.reactToLink.pop(msg)
                        unique = open("reactToLinkUni.txt",'r')
                        contentsa = ''
                        contentsb = ''
                        line = unique.readline()
                        while msg not in line:
                            contentsa += line
                            line = unique.readline()
                        line = unique.readline()
                        while line != '':
                            contentsb += line
                            line = unique.readline()
                        unique.close()
                        unique = open("reactToLinkUni.txt",'w')
                        unique.write(contentsa)
                        unique.write(contentsb)
                        unique.close()
                    elif message.content[7] == 'g' and msg in MyClient.reactToLink2:
                        await message.channel.send("Momeca has deleted " + msg + " from Momeca's general collection (˘•ω•˘)" + MyClient.reactToLink2[msg].format(message))
                        MyClient.reactToLink2.pop(msg)
                        general = open("reactToLinkGen.txt",'r')
                        contentsa = ''
                        contentsb = ''
                        line = general.readline()
                        while msg not in line:
                            contentsa += line
                            line = general.readline()
                        line = general.readline()
                        while line != '':
                            contentsb += line
                            line = general.readline()
                        general.close()
                        general = open("reactToLinkGen.txt",'w')
                        general.write(contentsa)
                        general.write(contentsb)
                        general.close()
                    else:
                        await message.channel.send("Momeca refuses to do anything because there is something wrong (｀へ´)=3".format(message))
                else:
                    await message.channel.send("Momeca refuses to do anything because you don't have permission (｀へ´)=3".format(message))
            else:
                await message.channel.send("もめかかもね∼".format(message))
                    

        #sends a link of a picture using the dictionary
        if message.content.startswith('.reply'):
            if message.content.strip() == '.reply':
                await message.channel.send("もめかかもね∼".format(message))
                return
            msg = message.content[7:].strip()
            if msg in MyClient.reactToLink:
                link = MyClient.reactToLink[msg]
                await message.channel.send(link.format(message))
            elif msg in MyClient.reactToLink2:
                link = MyClient.reactToLink2[msg]
                await message.channel.send(link.format(message))
            else:
                await message.channel.send("Momeca hasn't seen this reaction before (˘•ω•˘)".format(message))
            return


client = MyClient()
client.run('NTk1NTA5MjcxNTg0NzAyNDkw.XRsBrQ.lQwm9aG_Uk3E_yWIKvtahKP2aG0')
