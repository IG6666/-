from sys import argv
from xlrd import open_workbook
import matplotlib.pyplot as plt

script,input_file = argv
file = open_workbook(input_file)
sheet = file.sheet_by_index(0) #通过索引顺序获取第一个工作表

def der(a,b,c,d):
    """求导运算"""
    return (b-a)/(d-c)

Time = []
list1 = []
list2 = []
list3 = []
pypX1 = []
pypY1 = []
pypZ1 = []
pypX2 = []
pypY2 = []
pypZ2 = []
peaktime = []
maximum = []
#传感器1
X1 = []
Y1 = []
Z1 = []
#传感器2
X2 = []
Y2 = []
Z2 = []

for row in range(1,sheet.nrows):
    list1.append(sheet.cell_value(row,1))

#将相邻两数两两之间求导计算出变化趋势
for row in range(1,sheet.nrows-2):
    list2.append(der(list1[row],list1[row+1],sheet.cell_value(row,0),sheet.cell_value(row+1,0)))

list1.clear()

#计算峰值
a = 0
Peakline = []#储存峰值行数
for row in range(0,len(list2)):
    if list2[row] > 50 and (row - a) > 80:
        list3.append(list2[row])
        Peakline.append(row)
        a = row


print("周期数为：{}".format(len(Peakline)))



for row in range(1,sheet.nrows):
    Time.append(sheet.cell_value(row,0))
for row in range(1,sheet.nrows):
    pypX1.append(sheet.cell_value(row,1))
for row in range(1,sheet.nrows):
    pypY1.append(sheet.cell_value(row,2))
for row in range(1,sheet.nrows):
    pypZ1.append(sheet.cell_value(row,3))
for row in range(1,sheet.nrows):
    pypX2.append(sheet.cell_value(row,4))
for row in range(1,sheet.nrows):
    pypY2.append(sheet.cell_value(row,5))
for row in range(1,sheet.nrows):
    pypZ2.append(sheet.cell_value(row,6))


fig1 = plt.figure(figsize=(80,60), dpi=60)
fig2 = plt.figure(figsize=(80,60), dpi=60)
fig3 = plt.figure(figsize=(80,60), dpi=60)
fig4 = plt.figure(figsize=(80,60), dpi=60)
fig5 = plt.figure(figsize=(80,60), dpi=60)
fig6 = plt.figure(figsize=(80,60), dpi=60)

ax1=fig1.add_subplot(1,1,1)
ax1.plot(Time,pypX1)
ay1=fig2.add_subplot(1,1,1)
ay1.plot(Time,pypY1)
az1=fig3.add_subplot(1,1,1)
az1.plot(Time,pypZ1)
ax2=fig4.add_subplot(1,1,1)
ax2.plot(Time,pypX2)
ay2=fig5.add_subplot(1,1,1)
ay2.plot(Time,pypY2)
az2=fig6.add_subplot(1,1,1)
az2.plot(Time,pypZ2)



i = 0
for num in Peakline:
    for b in  range(num - 40,num + 40):
        X1.append(sheet.cell_value(b,1))
        Y1.append(sheet.cell_value(b,2))
        Z1.append(sheet.cell_value(b,3))
        X2.append(sheet.cell_value(b,4))
        Y2.append(sheet.cell_value(b,5))
        Z2.append(sheet.cell_value(b,6))
    time = sheet.cell_value(num + 40,0) - sheet.cell_value(num - 40,0)
    i = i + 1
    print("周期{}的时间:{}s".format(i,time))
    print("传感器1：")
    print("X轴的最大值为:{} ".format(max(X1)))
    print("X轴的最小值为:{} ".format(min(X1)))
    ax1.plot(sheet.cell_value(num,0),max(X1),'ro')
    ax1.annotate(f"{max(X1)}",xy=(sheet.cell_value(num,0),max(X1)))
    X1.clear()
    print("Y轴的最大值为:{} ".format(max(Y1)))
    print("Y轴的最小值为:{} ".format(min(Y1)))
    ay1.plot(sheet.cell_value(num,0),max(Y1),"ro")#ax1.plot(sheet.cell_value(Y1.index(max(Y1)),0),max(Y1),"ro")
    ay1.annotate(f"{max(Y1)}",xy=(sheet.cell_value(num,0),max(Y1)))
    Y1.clear()
    print("Z轴的最大值为:{} ".format(max(Z1)))
    print("Z轴的最小值为:{} ".format(min(Z1)))
    az1.plot(sheet.cell_value(num,0),max(Z1),"ro")#ax1.plot(sheet.cell_value(Y1.index(max(Y1)),0),max(Y1),"ro")
    az1.annotate(f"{max(Z1)}",xy=(sheet.cell_value(num,0),max(Z1)))
    Z1.clear()
    print("传感器2：")
    print("X轴的最大值为:{} ".format(max(X2)))
    print("X轴的最小值为:{} ".format(min(X2)))
    ax2.plot(sheet.cell_value(num,0),max(X2),'ro')
    ax2.annotate(f"{max(X2)}",xy=(sheet.cell_value(num,0),max(X2)))
    X2.clear()
    print("Y轴的最大值为:{} ".format(max(Y2)))
    print("Y轴的最小值为:{} ".format(min(Y2)))
    ay2.plot(sheet.cell_value(num,0),max(Y2),'ro')
    ay2.annotate(f"{max(Y2)}",xy=(sheet.cell_value(num,0),max(Y2)))
    Y2.clear()
    print("Z轴的最大值为:{} ".format(max(Z2)))
    print("Z轴的最小值为:{} \n".format(min(Z2)))
    az2.plot(sheet.cell_value(num,0),max(Z2),'ro')
    az2.annotate(f"{max(Z2)}",xy=(sheet.cell_value(num,0),max(Z2)))
    Z2.clear()

plt.show()
