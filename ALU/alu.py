import re
import sys
from fractions import  Fraction

class ALU:
    def GetResult(self,address1,address2):
        answers = []
        j = 0
        with open(address1,'r',encoding='utf-8') as x:
            for i in x.readlines():
                j +=1
                a = i.split('.',1)
                data = a[1].replace('=','')
                data = data.replace('×', '*').replace(' ', '')
                data = re.sub("r(\d+'\d+/\d+)", r'(\1)',data).replace("'", '+')#筛选假分数，给假分数左右两边加括号来确保运算的正确性


                error = re.compile(r"\)÷\d+÷\d+")
                special = error.findall(data)
                if special:
                    data = re.sub(r"(\d+/\d+)", r"Fraction(\1)", data)
                    data = data.replace('÷', '/')
                else:
                    data = data.replace('÷', '/')
                    data = re.sub(r"(\d+/\d+)", r"Fraction(\1)", data)


                #print(er)
                result = eval(data)
                result1 = Fraction(str(result)).limit_denominator()

                s = result1._numerator
                x = result1._denominator
                z = int(s/x)
                if x == 1 or int(result1)==0:
                    result = str(result1)
                else :
                    result1 = result1 - z
                    result = str(z)+"'"+str(result1)
                answers.append(result)

        with open (address2,'w',encoding='utf-8') as y:
            line = 0
            for i in answers:
                line +=1
                y.write(str(line)+'. '+i+'\n')
        return answers

    def compare(self,address1,address2,address3):
        line = 0
        counter = 0
        CorrectList = []
        WrongList = []
        CorrectAnswer = []
        with open(address1,'r',encoding='utf-8') as z:
            for i in z.readlines():
                i = re.sub('\n','',i)
                CorrectAnswer.append(i)
        #print(CorrectAnswer)
        with open(address2,'r',encoding='utf-8') as x:
            for i in x.readlines():
                i = re.sub('\n','', i)
                if i == CorrectAnswer[line]:
                    CorrectList.append(str(line+1))
                    counter += 1
                else:
                    WrongList.append(str(line+1))
                line += 1

        #print(CorrectList)
        #print(WrongList)
        with open(address3, 'w', encoding='utf-8') as y:
            y.write("Correct: "+str(counter)+'  ("'+',"'.join(CorrectList)+')'+"\n")
            y.write("Wrong: " + str(line-counter) + "   ('"+"','".join(WrongList)+"')"+"\n")



if __name__ == "__main__":
    address = 'Exercises.txt'
    sa = 'answer.txt'
    qa = 'Answers.txt'
    Grade = 'Grade.txt'
    project = ALU()
    project.GetResult(address, qa)
    project.compare(sa, qa, Grade)