s = 'azcbobobegghakl'
# s = 'abcbcd'
s = 'abc'
index=0
alpha=""
truth=0
final=""
alpha=s[0]
for letter in s:
    if index+1==len(s):
        break
    elif letter>s[index+1]:
        alpha=s[index+1]
    elif letter<=s[index+1]:
        alpha +=s[index+1]

    if truth<len(alpha):
        final=alpha
        truth=len(alpha)
    index += 1
print(final)





# for letter in s:
#     alpha=letter
#     if letter<=s[index+1]:
#           alpha += letter
#     index += 1
#     if len(alpha)>truth:
#         truth=len(alpha)
#         final=alpha
# print(alpha)




# while index+1<len(s)
#     for letter in s:
        