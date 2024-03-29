class Client():
    cIdNum = int(1000)
    cRecNum = int(100000)

    def __init__(self, newcFName, newcLName, newcPhone, newcEmail):
        self.cID = Client.cIdNum
        Client.cIdNum += 10
        self.cFName = newcFName
        self.cLName = newcLName
        self.cPhone = newcPhone
        self.cEmail = newcEmail
        self.cOwing = float(0)
        self.cReciepts = []
        self.prevRentals = []
        self.currRental = None

    def setPhone(self, newPhone):
       self.cPhone = newPhone

    def setEmail(self, newEmail):
        self.cEmail = newEmail

    def __str__(self):
        return (f"{self.cFName} {self.cLName}\n"
                f"Phone: {self.cPhone}\n"
                f"Email: {self.cEmail}\n"\
                f"Owing: {self.cOwing}\n"
                f"Current: {self.currRental}")
