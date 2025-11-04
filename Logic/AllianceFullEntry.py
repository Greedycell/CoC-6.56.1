import json
from Utils.Writer import Writer

config = json.load(open("config.json", "r"))

class AllianceFullEntry(Writer):

    def encode(self):

        self.writeInt(config['AllianceHighID'])  # AllianceHighID
        self.writeInt(config['AllianceLowID'])  # AllianceLowID

        self.writeString(config['AllianceName'])  # AllianceName
    
        self.writeInt(config['AllianceBadge'])  # AllianceBadge

        self.writeInt(0)  # AllianceType
        self.writeInt(1)  # NumberOfMembers
        self.writeInt(0)  # Score
        self.writeInt(0)  # RequiredScore

        self.writeString(config['AllianceDescription'])  # AllianceDescription
        
        self.writeInt(1)  # AllianceMembers

        self.writeInt(config['AccountHighID'])  # AvatarHighID
        self.writeInt(config['AccountLowID'])  # AvatarLowID

        self.writeString(None)  # FacebookID
        self.writeString(config['Name'])  # Name

        self.writeInt(config['AllianceRole'])  # Role
        self.writeInt(config['ExpLevel'])  # ExpLevel
        self.writeInt(config['LeagueType'])  # LeagueType
        self.writeInt(config['Score'])  # Score
        self.writeInt(config['Donations'])  # Donations
        self.writeInt(config['DonationsReceived'])  # DonationsReceived
        self.writeInt(0)  # Order
        self.writeInt(0)  # PreviousOrder

        self.writeByte(0)  # IsNewMember
        self.writeByte(1)

        self.writeInt(config['HomeHighID'])  # HomeHighID
        self.writeInt(config['HomeLowID'])  # HomeHighID