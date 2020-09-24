
import re
import jieba
import jieba.analyse
import sys
'''
fr1 = "D:\\testfile\orig_0.8_dis_10.txt" 个人测试用例
fr2 = "D:\\testfile\orig.txt"
savepath = "D:\\testfile\out.txt"
'''
class simhash:
    def __init__(self,fl1,fl2):#方便直接调用最常用的两个数据
        self.haiming = self.haiming(fl1,fl2)
        self.siminarity = self.siminarity(fl1,fl2)

    def getfile(self,file): #从地址中获取对应文本，返回关键词字典和关键词数目
        txt1 = ''
        dictXL = {}
        with open(file, 'r', encoding="utf-8") as origin_file:
            for line in origin_file.readlines():
                if line !='\n': #不写入换行符
                    punctuation = '`,.={}()#↵_·%@+&"？\-/<>、，。!;:?"\'' #筛除掉常用的符号
                    text = re.sub(r'[a-zA-Z0-9{}]+'.format(punctuation), '', line)#筛选掉数字和字母，用于筛除html代码
                    txt1 = txt1 + text.strip()
                else:
                    continue
            txt1 =txt1.replace(" ",'')
        jieba.analyse.set_stop_words('./stopwords.txt') #设置停词库
        size = 50#最高权的前n个关键词
        for feature, weight in jieba.analyse.extract_tags(txt1, topK=size, withWeight=True): #用jieba分词，权重处理在jieba内部使用tf-idf算法，返回权重最高那几十个词和其权重的列表
            dictXL[feature] = weight
            #print (dictXL[feature])
        return dictXL,size

    def string_hash(self,source):#汉字hash算法，此处借用了网上的汉字hash处理算法，
        if source == "":
            return 0
        else:
            x = ord(source[0]) << 7
            m = 1000003
            mask = 2 ** 128 - 1
            for c in source:
                x = ((x * m) ^ ord(c)) & mask
            x ^= len(source)
            if x == -1:
                x = -2
            x = bin(x).replace('0b', '').zfill(64)[-64:]
            #print(source,x)
            return str(x)

    def simhashalgo(self,file):#simhash算法部分
        dictXL = {}
        dictXL,size = self.getfile(file)
        #print(dictXL)
        database = []
        length = 0
        for key,weight in dictXL.items():
            data = []
            weight = int(weight*100)
            #print(key)
            keyhash = self.string_hash(key)#对汉字进行hash处理
            for i in keyhash:
                length +=1
                if i =='1':#simhash = hash * weight
                    data.append(weight)
                else :
                    data.append(-weight)
            database.append((data))

        list1 = [x*0 for x in range(64)]
        for i in range(64):
            for j in range(size):
                list1[i] += database[j][i]
        hashlist = []#simhash值（二进制）
        for i in list1:
            if i>=0:    #simhash算法核心，特征向量运算后又重新降维
                hashlist.append('1')
            else:
                hashlist.append('0')
        #print(list1)
        #print(hashlist)
        return hashlist

    def haiming(self,file1,file2):#求取海明距离长度
        F1 = self.simhashalgo(file1)
        F2 = self.simhashalgo(file2)
        haimingdistance = 0
        for i in range(64):
            if F1[i] ==F2[i]:
                continue
            else :
                haimingdistance +=1
        return haimingdistance

    def siminarity(self,file1,file2):#相似度取两数相除
        a = ''
        b = ''
        F1 = self.simhashalgo(file1)
        F2 = self.simhashalgo(file2)
        a = int(a.join(F1),2)
        b = int(b.join(F2),2)

        if(a > b):
            return float(b/a)*100
        else:
            return float(a/b)*100
def main():
    try:
        fr1,fr2,savepath = sys.argv[1:4]
    except Exception as e:
        print("文件列表获取失败")
    project = simhash(fr1, fr2)

    with open(savepath,'w',encoding='utf-8') as save:
        save.write("两文件的海明距离为：%d \n" %project.haiming)
        save.write("两文件的相似度为：%0.2f" %project.siminarity)

    print(project.siminarity)

if __name__ == "__main__":
    main()


