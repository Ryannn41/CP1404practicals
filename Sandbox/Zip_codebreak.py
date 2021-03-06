import random, zipfile, time, sys


class MyIter():
    cset = 'abcdefghijklmnopqrstuvwxyz0123456789'

    def __init__(self, min, max):  # 迭代器实现初始方法，传入参数
        if min < max:
            self.minlen = min
            self.maxlen = max
        else:
            self.ninlen = max
            self.maxlen = min

    def __iter__(self):
        return self

    def __next__(self):
        rec = ''
        for i in range(0, random.randrange(self.minlen, self.maxlen + 1)):
            rec += random.choice(MyIter.cset)
        return rec


def extract():
    start_time = time.time()
    zfile = zipfile.ZipFile('chubao.zip', 'r')
    for password in MyIter(4, 8):
        if zfile:
            try:
                zfile.extractall(path='.', pwd=str(password).encode('utf-8'))
                print("当前压缩密码为：", password)
                end_time = time.time()
                print('当前破解压缩包花了%s秒' % (end_time - start_time))
                sys.exit(0)
            except Exception as e:
                print('pass密码：', password)
                pass


if __name__ == "__main__":
    extract()
