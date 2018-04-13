from math import sqrt,pi
from functools import wraps

def setround(func,accuracy=4):
    """
    装饰器，用于确定函数返回的浮点值位数,默认保留4位小数
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args,**kwargs):
        result=round(func(*args,**kwargs),accuracy)
        return result
    return wrapper

class LoadCalculation:
    """
    用于计算阻抗相关参数的类
    #Doctest String
    >>> load=LoadCalculation(voltage=24,current=100,cosf=0.25)
    >>> print(load.sinf)
    0.9682
    >>> print(load.impedance)
    0.24
    >>> print(load.resistance)
    0.06
    >>> print(load.reactance)
    0.2324
    >>> print(load.inductance)
    0.7398
    """
    def __init__(self,voltage,current,cosf):
        """
        负载计算必须初始化输入电压、电流与功率因数作为参数
        单位分别为V，A
        :param voltage:
        :param current:
        :param cosf:
        根据输入参数计算出 电阻、电抗以及电感值
        """
        self._voltage=voltage
        self._current=current
        self._cosf=cosf
        self._sinf= self.sinf
        self._impedance=self.impedance #计算总阻抗，单位欧姆
        self._resistance=self.resistance # 电阻的阻抗值，单位欧姆
        self._reactance=self.reactance   # 电感的感抗值，单位欧姆
        self._inductance=self.inductance #电感的电感值，单位  毫亨

    @property
    @setround
    def sinf(self):
        #self._sinf=round(sqrt(1-self._cosf**2),4)
        self._sinf = sqrt(1 - self._cosf ** 2)
        return self._sinf

    @property
    @setround
    def impedance(self):
        if self._current!=0:
            self._impedance=self._voltage/self._current
        else:
            self._impedance=-1
        return self._impedance

    @property
    @setround
    def resistance(self):
        if self._impedance!=-1:
            self._resistance=self._impedance*self._cosf
        else:
            self._resistance=-1
        return self._resistance

    @property
    @setround
    def reactance(self):
        if self._impedance!=-1:
            self._reactance=self._impedance*self.sinf
        else:
            self._reactance=-1
        return self._reactance

    @property
    @setround
    def inductance(self):
        if self._impedance!=-1:
            self._inductance=10*self.reactance/pi
        else:
            self._inductance=-1
        return self._inductance


if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)
    #load = LoadCalculation(voltage=24, current=100, cosf=0.25)
    #print(load.sinf)