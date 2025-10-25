class Stream:
    def __init__(self, case):
        self.case = case

    def playground(self):
        # print(dir(self.case.Flowsheet.MaterialStreams.Item('1').AttachedOpers.Names))
        # print()
        # print('**************************')
        # print()
        # print(self.case.Flowsheet.MaterialStreams.Item('1').AttachedOpers.Names)

        print(dir(self.case.UtilityObjects))
        print()
        print('**************************')
        print()
        print(self.case.UtilityObjects.Names)