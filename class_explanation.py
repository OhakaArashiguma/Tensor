#マジックナンバー
#通常intやfloat, strにしか対応できない関数をclassにも適応

#文字表現を定義
#正味def name(self): return self.nameすればいいと思ってる
class sample1:
    def __init__(self,name):
        self.name = name
    
    #str(クラス)したときの出力を定義
    def __str__(self):
        return f'{self.name}が貴様の名前だ'
    
    #str(クラス)と同じ意味（デバッグ用）
    def __repr__(self):
        return "良いぞ少年！"
    
#四則演算を定義
#__add__(+), __sub__(-), __mul__(*), __truediv__(/)

class sample2:
    def __init__(self, value):
        self.value = value
    
    def __add__(self,other):
        return sample2(self.value + other.value)

a = sample2(500)
b = sample2(1000)

#挙動としては
#①a + bの+で__add__の呼び出しを決意、aをself, bをotherで決める
#②sample2を新たに作成、cに追加
c = a+b
print(c.value)

#論理式を定義
#__eq__(==), __ne__(!), __lt__(<) etc
class sample3:
    def __init__(self,value):
        self.value = value
    def __eq__(self, other):
        return self.value == other.value

a = sample3(500)
b = sample3(500)
c = sample3(1100)

print(a == b)
print(a == c)

#イテレーターを設定
class sample4:
    def __init__(self,max_count):
        self.count =0
        self.max_count = max_count
    
    #クラスがforで扱えることをパイソンに伝える
    def __iter__(self):
        return self
    #for される度カウンターを一つづつ増やす
    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        
        self.count +=1
        return self.count
         
a = sample4(10)

for num in a:

#forが出たのでself.__iter__()が実行、numが主役に
#ループの度にself.__next__が行われる

    print(num)

import numpy as np
#リストの作成
class sample5:
    def __init__(self):
        #平均、標準偏差、データ数の順
        self.data=np.random.normal(0,1,6)
    def __getitem__(self,index):
        return self.data[index] #インデックスアクセスを許可
    def __setitem__(self, index, value):
        self.data[index] = value #データの編集を許可 クラス[index]=valueで編集可能
    def __len__(self):
        return len(self.data) #len(クラス)で長さを出せる

a = sample5()
print(a[3],len(a))
