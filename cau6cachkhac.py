


# prefix = ""
# flag = 0
# for i in range(len(x)):
#         for s in x :
#                 if i == len(s) or s[i] != x[0][i]:
#                     flag=0
#                     break
#                 else:
#                     flag = 1 
#         if flag == 1:             
#             prefix += x[0][i]
#         else:
#             pass # không làm gì cả, nó chỉ giữ chỗ cho các hàm
#                 # print (s)
# print (prefix)
x = ["hello", "heaven", "heavy"]
def longestCommonPrefix(strs):
    longest_pre = []
    if strs and len(strs) > 0:
        strs = sorted(strs)
        # e.g. before sort: ["flower","flow","flight","fake"]
        # after sort: ['fake', 'flight', 'flow', 'flower']
        first, last = strs[0], strs[-1]
        for i in range(len(first)):
            if len(last) > i and last[i] == first[i]:
                longest_pre.append(last[i])
            else:
                return "".join(longest_pre)
    return "".join(longest_pre)

print (longestCommonPrefix(x))