# 格式化字符串
print("today's stock price:%f"%50.4625)
print("today's stock price:%.2f"%50.4625)
print("change since yesterday:%+.2f"%1.5)
u = "ios"
v = "9001"
print("%s = %s"%(u, v))
# 映射
li = [1, 9, 8, 4]
print([elem*2 for elem in li])
params = {"server":"mpilgrim", "database":"master","uid":"sa","pwd":"secert"}
print(params.keys())
print(params.values())
print(params.items())
print(["%s = %s"%(k,v) for k, v in params.items()])
print("; ".join(["%s = %s"%(k, v) for k, v in params.items()])) # join 只对字符串有用
