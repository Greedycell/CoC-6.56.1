from Utils.Writer import Writer
from Utils.Reader import Reader
from Logic.Player import Player

class ClientHelloMessage(Writer, Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):
        pass

    def process(self):
        self.writeInt(1) # m_protocol
        self.writeInt(0) # m_keyVersion
        self.writeInt(0) # m_majorVersion
        self.writeInt(0) # m_minorVersion
        self.writeInt(0) # m_buildVersion
        self.writeString() # m_contentHash
        self.writeInt(0) # m_deviceType
        self.writeInt(0) # m_appStore