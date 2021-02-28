s = 'azcbobobegghakl'

count=0
index=0
for vowel in s:
    if vowel=='b' and len(s)>(index+3) and (vowel+"ob")==s[index:index+3]:
        count +=1
    index += 1
print(count)