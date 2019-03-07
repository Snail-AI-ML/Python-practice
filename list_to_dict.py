#嵌套列表转换为字典
list = [['k1','v1'],['lining','一切皆有可能'],['nike','just do'],['Anta','永不止步']]
dict = {}
for i in list:
    dict[i[0]] = i[1] 
#用for循环的时候，i是可以直接进入嵌套列表内部，代表最内层的单个元素，所以i[1]指的是v1.
print(dict, '\n')

for i in list:
#value为列表形式写法
	dict[i[0]] = [i[1]]
print(dict)