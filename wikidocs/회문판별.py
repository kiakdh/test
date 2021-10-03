word = input("단어를 입력해주세요: ")

word_l = word.lower()
word_p = word_l.replace(' ','')
word_r = word_p[::-1]



print(word_l)
print(word_r)
print(word_p)

if word_p == word_r:
    print("True")
else:
    print("False")