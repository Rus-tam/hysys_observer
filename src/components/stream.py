class Stream:
    def __init__(self, case):
        self.case = case

    def get_components_molar_fraction(self, stream_name: str, comp_list_number: str):
        """
        Метод для получения молярного состава заданного потока.
        Если в модели используется один набор компонентов, то comp_list_number = 1
        Если в модели используется больше, чем один набор компонентов, то необходимо указать номер набора компонентов.
        """
        comp_frac_dict = {}
        root = self.case.Flowsheet.MaterialStreams.Item(stream_name)

        molar_fraction_value = root.ComponentMolarFractionValue
        components = self._get_components_list(comp_list_number)

        for i in range(0, len(components)):
            comp_frac_dict[f'{components[i]}_mol_frac'] = round(molar_fraction_value[i], 5)
        
        return comp_frac_dict


    def _get_components_list(self, comp_list_number: str):
        """
        Приватный метод для получения списка используемых компонентов.
        Если в модели используется один набор компонентов, то comp_list_number = 1
        Если в модели используется больше, чем один набор компонентов, то необходимо указать номер набора компонентов.
        """
        return self.case.BasisManager.ComponentLists.Item(f'Component List - {comp_list_number}').Components.Names


    def playground(self):
        # print(dir(self.case.Flowsheet.MaterialStreams.Item('1')))
        # print()
        # print('**************************')
        # print()
        # print(self.case.Flowsheet.MaterialStreams.Item('1').ComponentMolarFractionValue)

        print(dir(self.case.BasisManager.ComponentLists.Item('Component List - 1').Components.Names))
        print()
        print('**************************')
        print()
        print(self.case.BasisManager.ComponentLists.Item('Component List - 1').Components.Names)