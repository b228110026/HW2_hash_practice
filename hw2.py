import matplotlib.pyplot as plt
f = open("hw2_data.txt")
words = {}
for word in f:
  word = word.replace('\n', '')
  if word in words:
    words[word] = words[word] + 1
  else:
    words[word] = 1

print('1. 總共有多少個不重複的英文字 :')
print(len(words))
print('2. 每一個英文字出現次數為何 :')
print(words)
print('3. 畫出類似附件Figure_1.png圖示的直方圖（hint: 使用matplotlib.pypi），由多到少列出每個英文')

words = sorted(words.items(), key=lambda x:x[1], reverse=True)
words = dict(words)
x = list(words.keys())
y = list(words.values())
plt.bar(x, y)
plt.show()

f.close()