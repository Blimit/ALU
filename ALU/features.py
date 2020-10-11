import re
from fractions import Fraction
string = "5÷(9-0）+3"
symbol = "5/9 + 3 "
import cal_sys
class Feature:
    def __init__(self,string,symbol):
        number,op = self.information(string)
        self.problem = string
        self.sym = self.turn(symbol)
        self.num = '-'.join(number)
        self.op = ''.join(op)


    def information(self,string):
        number=[]
        op_list = []
        sym = string.replace("×", "*").replace(" ", "").replace("=", '').replace('÷', '/')
        # print (sym)

        # 插入假分数
        data_list = re.findall(r"(\d+'\d+/\d+)", sym)
        sym = re.sub(r"(\d+'\d+/\d+)", ' ', sym)
        # 插入真分数
        data_list += re.findall(r"(\d+/\d+)", sym)
        sym = re.sub(r"(\d+/\d+)", ' ', sym)
        # 插入整数
        data_list += re.findall(r"(\d+)", sym)

        for x in data_list:
            if "'" in x:
                y = x.replace("'", '+')
                number.append(str(round(eval(y), 3)))
            else:
                number.append(str(round(eval(x), 3)))

        number.sort()

        #print(number)
        op = re.compile(r"[+\-*/]+")
        op_list = op.findall(sym)

        return number,op_list

    def turn(self,symbol):
        data_list ,op = self.information(symbol)
        return ' '.join(data_list+op)




