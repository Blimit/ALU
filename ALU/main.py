from alu import ALU
from CreatList import  create
import sys
ProblemsFile = "Exercises.txt"
AnswersFile = "Answers.txt"
Grade = "Grade.txt"
def main():
    try:
        type1,title,type2,index = sys.argv[1:5]
    except:
        print("参数缺失，请下面功能中选择正确的格式：")
        print("生成题目集:python main.py -n 题目数 -r 使用数字范围")
        print("比较题目集和答案：python main.py -e 题目地址 -a 待批改的答案地址")
    if type1 == "-n" and type2 == "-r":

        create(ProblemsFile,int(title), int(index))
        x = ALU()
        x.GetResult(ProblemsFile, AnswersFile)
    elif type1 == "-e" and type2 == "-a":
        exercises = title
        Myanswer = index
        x = ALU()
        x.GetResult(exercises, Grade)
        x.compare(Grade,Myanswer,Grade)
    else:
        print("输入参数错误")
        print("生成题目集:python main.py -n 题目数 -r 使用数字范围")
        print("比较题目集和答案：python main.py -e 题目地址 -a 待批改的答案地址")

if __name__=='__main__':
    main()
