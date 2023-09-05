class Vehicle():
    vIdNum = int(10)
    vRented = []

    def __init__(self, newMake, newModel, newYear, newRego, newCost, newOdo):
        self.vID = Vehicle.vIdNum
        Vehicle.vIdNum += 5
        self.vMake = newMake
        self.vModel = newModel
        self.vYear = newYear
        self.vRego = newRego
        self.vCost = newCost
        self.vOdo = newOdo
        self.vRenter = None
        self.vStatus = True