import matplotlib.pyplot as plt

x = [1,2,3,4,5]
k1 = [1.22,0.58,0.44,0.28,0.29]
k2 = [1.66,0.84,0.58,0.46,0.37]
k3 = [51.92,29.36,19.59,15.36,12.32]
plt.plot(x,k1,'s-',color = 'r',label="mp")
plt.plot(x,k2,'o-',color = 'g',label="mpc")
plt.plot(x,k3,'o-',color = 'c',label="mpcs")
plt.xlabel("server number")#横坐标名字
plt.ylabel("time")#纵坐标名字
plt.legend(loc = "best")#图例
plt.show()
