import copy
class Reaction:
    def __init__(self, uniqueDict, generalDict):
        self.reactToLink = copy.deepcopy(uniqueDict)
        self.reactToLink.update(generalDict)

    def react(self, message: str) -> str:
        """Return the link of the image corresponding to
        the name given in the message."""
        if len(message) <= 7:
            return "もめかかもね∼"
        msg = message[7:].strip()
        link = "Momeca hasn't seen this reaction before (˘•ω•˘)"
        if msg in self.reactToLink:
            link = self.reactToLink[msg]
        return link
