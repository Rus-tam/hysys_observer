class Utility:
    def __init__(self, case):
        self.case = case

    def playground(self):
        print(dir(self.case.UtilityObjects.Item('Огибающая-1').DewTempValue))
        print()
        print('**************************')
        print()
        print(self.case.UtilityObjects.Item('Огибающая-1').DewTempValue)