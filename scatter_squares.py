import matplotlib.pyplot as plt
'''
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, s=100)
#plt.scatter(2, 4, s=200)
# 设置图标标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
'''
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, c='red', edgecolors=None, s=40)
# plt.scatter(x_values, y_values, c=(0, 0, 0.1), edgecolors=None, s=40)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors=None, s=40)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置每个坐标轴取值范围
plt.axis([0, 1100, 0, 1100000])
plt.show()
# 程序员自动保存图表
plt.savefig('squares_plot.png', bbox_inches='tight') # 裁剪掉周围空白的区域