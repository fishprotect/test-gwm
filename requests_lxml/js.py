import re
import execjs

r = '''var carCompareJson = [[["124096","2.0T 手自一体 四驱 舒适版 5座 汽油"
    ,"http://img1.bitautoimg.com/autoalbum/files/20180907/686/2018090716320132116676
    _2.jpg","3962","H9","哈弗H9","hafuh9","2017","在产","在销","","http://baa.bitauto.com/ha
    valh9/","中大型SUV","炫晶黑,#000000|丛林绿,#3d512f|星空蓝,#424857|哈密尔
    顿灰,#555d66|匹兹堡银,#e2e2e2|汉密尔顿白,#ffffff"],["21.98万","18.98-21.98万"
    ,"2.10万","3年或10万公里","2.0","涡轮增压","","8","手自一体","","8","8","2017","SUV","汽油"],["4856","1926","1900","2800"
    ,"2330","5","","80","265/65 R17",]]]'''
reg = re.findall('carCompareJson = (.*?)]]',r,re.S)


print(reg)
print(len(reg))

