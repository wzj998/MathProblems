# https://www.zhihu.com/question/368683537/answer/996406236

import random
import math


def yansuan(a,b,c, n_tries=1000000): # 验算看看结果对不对
    sum_n=0
    for i_try in range(n_tries):
        # if i_try%10000==0:
        #     print("i_try="+str(i_try))
        sum_now=0
        n=0
        while True:
            n+=1
            rnd=random.uniform(a,b)
            sum_now+=rnd
            if sum_now>c:
                sum_n+=n
                # print(n)
                break
    print("蒙特卡洛:",sum_n/n_tries)

p_rcd=dict()
def p(i,j):
# (一直抛[aa,bb]的数，和恰为大于cc（已知j<=cc）就停止，抛了i轮之后，和恰为j)这一事件的概率
    str_index=str(i)+"_"+str(j)
    ans=0
    if str_index in p_rcd:
        ans=p_rcd[str_index]
    else:
        global aa,bb,cc,p_every
        if i==1:
            if aa<=j<=bb and j<=cc:  # <=cc也一定要
                ans=p_every
            else:
                ans=0
            pass
        elif i>1:
            if j>cc:
                ans=0
            else:
                i_last=i-1
                j_last_max = j - aa
                j_last_min = j - bb  # 就是这么神奇，后面这两行直接复制过来~
                ans=0
                for j_last in range(j_last_min,j_last_max+1):
                    ans+=p(i_last,j_last)*p_every
        else:
            print("大事不妙！i<1了")
            jy=input()
        # print("p("+str(i)+","+str(j)+")="+str(ans))
        p_rcd[str_index]=ans


    return ans


array_in=input("a b c=").split()
a=float(array_in[0])
b=float(array_in[1])
c=float(array_in[2])

yansuan(a,b,c)  # 蒙特卡洛得到的结果用于验算

# 最多取多少个ab之间的数放入期望计算
i_max=10#int(input("i_max="))
# 有可能永远都加不到(比如每次随机到都是0，还有负数更复杂了)。。。人为设定i_max吧
n_expand=1000 # 假设世界上的实数不是无限可分割的，把a,b,c膨胀到n_expand倍的整数，所求答案是一样的
# 显然i_max变大对精度改善作用很小，太大的时候概率会很小

aa=int(a*n_expand)
bb=int(b*n_expand)
cc=int(c*n_expand)
ans=0



j_min=cc+1 # 因为开区间所以要+1
j_max=cc+bb # 上一轮刚好cc，下一轮掷出最大的bb
e=0
print("aa bb cc =",aa,bb,cc)
p_every=0
if aa<=bb:
    p_every=1/(bb-aa+1)
for i in range(1,i_max+1):
    if i==1:
        if aa<=cc<=bb:
            e+=p_every
    else:
        for j in range(j_min,j_max+1):
            p_i=0
            j_last_max=j-aa
            j_last_min=j-bb
            for j_last in range(j_last_min, j_last_max+1):
                p_i+=p(i-1,j_last)
            e+=p_i*p_every*i  # p_every统一最后乘，都是可以达到的情况
            # print("i j e_now= ", i, j, e)
print("递推法:", e)




