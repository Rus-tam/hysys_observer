from typing import Dict, List
import pandas as pd

class Stream:
    def __init__(self, case):
        self.case = case
    
    def get_stream_props(self, stream_name: str):
        """
        Метод для получения физических свойств заданного потока
        """
        stream = self.case.Flowsheet.MaterialStreams.Item(stream_name)
        
        if stream.VapourFractionValue > 0:
            actual_liq_flow = stream.ActualLiqFlowValue * 3600
            actual_vap_flow = stream.ActualGasFlowValue * 3600
        elif stream.VapourFractionValue == 1:
            actual_liq_flow = 0
            actual_vap_flow = stream.ActualGasFlowValue * 3600
        elif stream.VapourFractionValue == 0:
            actual_liq_flow = stream.ActualLiqFlowValue * 3600
            actual_vap_flow = 0
        
        return {f'{stream_name}_temperature_C': stream.TemperatureValue, f'{stream_name}_pressure_kPa': stream.PressureValue,
                f'{stream_name}_mass_flow_kg/h': stream.MassFlowValue * 3600,
                f'{stream_name}_molecular_weight': stream.MolecularWeightValue, f'{stream_name}_mass_density_kg/m3': stream.MassDensityValue,
                f'{stream_name}_actual_liquid_flow_m3/h': actual_liq_flow, f'{stream_name}_actual_vapour_flow_m3/h': actual_vap_flow,
                f'{stream_name}_mass_heat_capacity': stream.MassHeatCapacityValue, f'{stream_name}_vapour_fraction': stream.VapourFractionValue, 
                f'{stream_name}_molar_flow_kgmole/h': stream.MolarFlowValue * 3600, f'{stream_name}_vapour_fraction_value': stream.VapourFractionValue,
                f'{stream_name}_liquid_fraction_value': stream.LightLiquidFractionValue,
                f'{stream_name}_heavy_liquid_fraction_value': stream.HeavyLiquidFractionValue}


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


    def _get_components_list(self, comp_list_number: str) -> List[str]:
        """
        Приватный метод для получения списка используемых компонентов.
        Если в модели используется один набор компонентов, то comp_list_number = 1
        Если в модели используется больше, чем один набор компонентов, то необходимо указать номер набора компонентов.
        """
        return list(self.case.BasisManager.ComponentLists.Item(f'Component List - {comp_list_number}').Components.Names)


    def playground(self):
        print(dir(self.case.Flowsheet.MaterialStreams.Item('1')))
        print()
        print('**************************')
        print()
        print(self.case.Flowsheet.MaterialStreams.Item('1'))

        # print(dir(self.case.BasisManager.ComponentLists.Item('Component List - 1').Components.Names))
        # print()
        # print('**************************')
        # print()
        # print(self.case.BasisManager.ComponentLists.Item('Component List - 1').Components.Names)