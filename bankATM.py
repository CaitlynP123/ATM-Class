class ATM(object):
    def __init__(self, cardNo, pinNo):
        self.cardNo = cardNo,
        self.pinNo = pinNo
    
    def display(self):
        print(self.cardNo)
        print(self.pinNo)

bankUser = ATM(123456789, 987654321)
bankUser.display()