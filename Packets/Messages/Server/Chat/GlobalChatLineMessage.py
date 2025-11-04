import json
from Utils.Writer import Writer
from Packets.Messages.Client.SendGlobalChatLineMessage import *

config = json.load(open("config.json", "r"))


class GlobalChatLineMessage(Writer):

    def __init__(self, device, message):
        super().__init__(device)
        self.device = device
        self.id = 24715
        self.message = message

    def encode(self):

        self.writeString(self.message)  # Message
        self.writeString(config['Name'])  # AvatarName

        self.writeInt(config['ExpLevel'])  # AvatarExpLevel

        self.writeInt(0)
        self.writeInt(1)

        self.writeInt(0)
        self.writeInt(1)

        self.writeByte(1)  # IsInAlliance

        self.writeInt(config['AllianceHighID'])
        self.writeInt(config['AllianceLowID'])

        self.writeString(config['AllianceName'])

        self.writeInt(config['AllianceBadge'])