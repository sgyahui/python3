import random,time,math

def shuang():
    red=range(1,34)
    blue=range(1,17)
    while True:
        print('欢迎使用双色球选号程序:')
        redball_number=int(input('请输入购买红球的个数:'))
        blueball_number=int(input('请输入购买篮球个数'))
        if redball_number>=6 and blueball_number>=1:
            redchoice=random.sample(red,redball_number)
            redchoice.sort()
            bluechoice=random.sample(blue,blueball_number)
            bluechoice.sort()
            number=math.factorial(redball_number)/math.factorial(redball_number-6)/math.factorial(6)*blueball_number
            money=2*number
            print('为您推荐的红球是:')
            print(redchoice)
            print('为您推荐的篮球是:')
            print(bluechoice)
            print('你选择了%d注，需要支付%d元' %(number,money))
            
        else:
            print('请至少选择6个红球和1个篮球，请重新输入:')
            continue
        choice=input('是否继续选号，y继续，其他退出出程序')
        if choice=='y':
            continue
        else:
            print('欢迎下次光临')
            break
        