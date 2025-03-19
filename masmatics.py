class Point:
    #初期値を__init__で設定、x =0 などは指定なしの時の値
    def __init__(self,x=0,y=0):
        self.x = x
        self.y =y
    #self.~の形で書かれた時の処理
    def hamming(self):
        return self.x + self.y
    #str()の処理（）内をstringにする
    def __str__(self):
        return f'({self.x},{self.y})'
    
#クラスの継承、Pointクラスの内容をPoint3Dの中に入れた上で__init__を書き換えている
class Point3D(Point):
    def __init__(self,x=0,y=0,z=0):
        #super().__init__(x,y)でsuper()(Point)を参照しているということ
        super().__init__(x,y)
        self.z = z

p=Point3D(2,5,6)
p=Point(5,6)

print(type(str(p)))