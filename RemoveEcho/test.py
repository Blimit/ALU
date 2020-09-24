import unittest

from main import simhash
basepath = "D:\\testfile\\"
layoutpath = "D:\\"
class TestDict(unittest.TestCase):
    def setUp(self):
        print("-------------------------")
    def test_init(self):
        print("测试单元启动")
        print("开始载入orig.txt进行对比：")
    def testadd(self):
        print("载入orig_0.8_add.txt")
        _main("orig.txt","orig_0.8_add.txt")

    def testdel(self):
        print("载入orig_0.8_del.txt")
        _main("orig.txt","orig_0.8_del.txt")

    def testdis_1(self):
        print("载入orig_0.8_dis_1.txt")
        _main("orig.txt","orig_0.8_dis_1.txt")


    def testdis_10(self):
        print("载入orig_0.8_dis_10.txt")
        _main("orig.txt","orig_0.8_dis_10.txt")

    def testdis_15(self):
        print("载入orig_0.8_dis_15.txt")
        _main("orig.txt","orig_0.8_dis_15.txt")


def _main(origpath, testpath):
    _path = testpath
    origpath = basepath + origpath
    testpath = basepath + testpath
    a = simhash(origpath,testpath)
    print("与原文本的相似度是：%f" %a.siminarity)

if __name__ == '__main__':
    unittest.main()