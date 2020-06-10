'''
This function is to convert any string representation of price, area to float number.

Language: Python

Creator: https://github.com/Yuliya-HV

'''

from collections import Counter
import re

def convert_to_float(entity):

    '''
    Convert string into float value.
    
    Input: entity -> string
    Return: float
    
    Solving problem of use ., in different position across countries in price/area:
    13 000.00
    38.000,00
    134.000
    38.000,00
    1.064,50
    94.92; 17,83; 13 606.00; 7.8015; 5.65
    2.883,0000; 266,6; 194,0400; 104,16
    '''

    _entity = ['0']

    try:
        if entity == ''.join(x for x in entity if x.isdigit()):
            _entity = entity
        else:
            _entity = re.sub('[,.]', ' ', entity.replace(' ', '.'))
            _entity = _entity.split()

            if len(_entity) > 0:
                if len(_entity[len(_entity)-1]) != 3:
                    _entity[len(_entity)-1:len(_entity)-1] = ['.']
                else:
                    sep = ''.join(x for x in entity if not x.isdigit())
                    dict_sep = Counter(sep)
                    first_sep = dict_sep[sep[0]]
                    
                    if len(set(dict_sep.keys()))>1:
                        _entity[len(_entity)-1:len(_entity)-1] = ['.']
            else:
                _entity = ['0']

        if len(_entity) == 0:
            _entity = ['0']
            
    except Exception as e:
        print('The function rejected an input due to unexpected error :: ', str(e))

    return float(''.join(_entity))
