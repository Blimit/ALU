import re
import sys
from fractions import  Fraction
def main():
    address = 'Exercises.txt'
    sa = 'answer.txt'
    qa = 'Answers.txt'
    Grade = 'Grade.txt'
    project = ALU()
    project.GetResult(address,sa)
    project.compare(sa,qa,Grade)

class ALU:
    def GetResult(self,address1,address2):
        answers = []
        j = 0
        with open(address1,'r',encoding='utf-8') as x:
            for i in x.readlines():
                j +=1
                a = i.split('.',1)
                data = a[1].replace('=','')
                data = re.sub("(\d+'\d+/\d+)", r'(\1)',data).replace("'",'+').replace('×','*').replace(' ','')
                data = re.sub("(\d+/\d+)",r'(\1)',data).replace('÷','/')
                #print(str(j)+'.  '+data)
                if '/' in data:
                    data = re.sub(r"(\d+/\d+)",r"Fraction('\1')",data)
                    result = eval(data)
                else :
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
                #print(result)
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
                CorrectAnswer.append(i)
        #print(CorrectAnswer)
        with open(address2,'r',encoding='utf-8') as x:
            for i in x.readlines():
                #print(i)
                #print(CorrectAnswer[line])
                if i == CorrectAnswer[line]:
                    CorrectList.append(str(line+1))
                    counter += 1
                else:
                    WrongList.append(str(line+1))
                line += 1

        print(CorrectList)
        print(WrongList)
        with open(address3, 'w', encoding='utf-8') as y:
            y.write("Correct: "+str(counter)+'  ("'+',"'.join(CorrectList)+')'+"\n")
            y.write("Wrong: " + str(line-counter) + "   ('"+"','".join(WrongList)+"')"+"\n")



if __name__ == "__main__":
    main()