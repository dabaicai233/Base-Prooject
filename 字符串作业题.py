"""
2.已知字符串 a = "aAsmr3idd4bgs7Dlsf9eAF",要求如下
	a.请将a字符串的大写改为小写，小写改为大写
	b.请将a字符串的数字取出，并输出成一个新的字符串
	c.请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {'a':4,'b':2}
	d.输出a字符串出现频率最高的字母
	e.请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False
"""
a = "aAsmr3idd4bgs7Dlsf9eAF"

#a
r0 = a.swapcase()

#b
newStr = ""
for c in a:
    if c.isdigit():
        newStr += c

#c
a = a.lower()
dict1 = {}
for ch in a:
    if ch not in dict1:
        dict1[ch] = 1
    else:
        dict1[ch] += 1
print(dict1)

#d.
maxValue = max(list(dict1.values()))
print(maxValue)

for key,value in dict1.items():
    if value == maxValue:
        print(key)

#e
list1 = [1,2,3,4,5]
s1 = set(list1)
print(s1)
s1.update([4])
print(s1)

#将列表转换为集合,同样也可以将字符串转换为结合
s = set(a)
print(s)
search = "boy"
s.update(search)

print(len(set(a)) == len(s))


#3.输入一个字符串，压缩字符串如下aabbbccccd变成a2b3c4d1
str1 = "aabbbccccd"
dict1 = {}
for ch in str1:
    if ch not in dict1:
        dict1[ch] = 1
    else:
        dict1[ch] += 1
print(dict1)
newStr = ""
for key,value in dict1.items():
    newStr += str(key)
    newStr += str(value)
print(newStr)

