class StoredLinks:
    def __init__(self):
        self.linkPrefix = ["https://cdn.discordapp.com/attachments/",
                           "https://media.discordapp.net/attachments/"]
        self.adminRoleId = [511556749392609281,511555135185354767,584394177807384596,513722191154511874,579685479767605259,584397796329914378]

        self.uniqueFile = "reactToLinkUni.txt"
        self.generalFile = "reactToLinkGen.txt"
        self.reactToLinkU = {}
        self.reactToLinkG = {}
        unique = open(self.uniqueFile,'r')
        for line in unique:
            pair = line.split()
            self.reactToLinkU[pair[0]] = pair[1]
        unique.close()

        general = open(self.generalFile,'r')
        for line in general:
            pair = line.split()
            self.reactToLinkG[pair[0]] = pair[1]
        general.close()

    def valid(self, message: str, roleIds: list) -> bool:
        """Check if the message has to correct format according to
        the command and if the author of the message has an adminRoleId."""
        msg = message.strip().split()
        if any(ids in self.adminRoleId for ids in roleIds):
            if len(msg) == 2 and msg[0].startswith('.delete'):
                return True
            elif len(msg) == 3:
                for prefix in self.linkPrefix:
                    if msg[2].startswith(prefix):
                        return True
        return False

    def add(self, name: str, link: str, fileName: str) -> None:
        """Add the new entry to the text file."""
        file = open(fileName,'a')
        file.write(name + ' ' + link + '\n')
        file.close()

    def edit(self, name: str, link: str, fileName: str) -> None:
        """Edit an entry in the text file."""
        file = open(fileName,'r')
        contentsa = ''
        contentsb = ''
        line = file.readline()
        while name not in line:
            contentsa += line
            line = file.readline()
        line = file.readline()
        while line != '':
            contentsb += line
            line = file.readline()
        file.close()
        file = open(fileName,'w')
        file.write(contentsa)
        file.write(name + ' ' + link + '\n')
        file.write(contentsb)
        file.close()

    def delete(self, name: str, fileName: str) -> None:
        """Delete an entry in the text file."""
        file = open(fileName,'r')
        contentsa = ''
        contentsb = ''
        line = file.readline()
        while name not in line:
            contentsa += line
            line = file.readline()
        line = file.readline()
        while line != '':
            contentsb += line
            line = file.readline()
        file.close()
        file = open(fileName,'w')
        file.write(contentsa)
        file.write(contentsb)
        file.close()

    def update(self, message: str, roleIds: list) -> str:
        """Update the intended dictionary and text file according to the message.
        Return a message depending if the operation was successful."""
        if self.valid(message, roleIds) :
            msg = message.strip().split()
            decision = msg[0][-1]
            if decision == 'u':
                fileName = self.uniqueFile
                dictName = self.reactToLinkU
                decision = "unique"
            elif decision == 'g':
                fileName = self.generalFile
                dictName = self.reactToLinkG
                decision = "general"
            else:
                return "Momeca refuses to do anything because Momeca doesn't know which collection to change!"
            command = msg[0][:-1]

            if command == ".add" and msg[1] not in dictName:
                dictName[msg[1]] = msg[2]
                self.add(msg[1], msg[2], fileName)
                return "Momeca has added " + msg[1] + " to Momeca's " + decision + " collection!"
            elif command == ".edit" or command == ".add":
                dictName[msg[1]] = msg[2]
                self.edit(msg[1], msg[2], fileName)
                return "Momeca has updated " + msg[1] + " in Momeca's " + decision + " collection!"
            elif command == ".delete":
                dictName.pop(msg[1])
                self.delete(msg[1], fileName)
                return "Momeca has deleted " + msg[1] + " from Momeca's " + decision + " collection (˘•ω•˘)"
            else:
                return "もめかかもね∼"
        return "Momeca refuses to do anything because the format is not correct or you don't have permission(｀へ´)=3"
            



        
        
