
# class Solution 
#  def longestCommonPrefix (self,strs : list[str]) -> str:
#   if len(strs) == 0:
#     return (" ")
# minlen = len(strs[0])
# # print (minlen)
#  for i in range(1, len(strs)):

#     minlen = min(minlen, len(strs[i]))  # tim chuoi be nhat trong ki tu da tim
#     # print (minlen)
#  add = ' '
#  for i in range(minlen):
#     si = strs[0][i]  # xet tung ki tu trong chuoi
#     # print (si)
#     for j in range(1, len(strs)):
#         if strs[j][i] != si:
#             return (add)
#     add += si
#  return (add)


# x = ["flower", "flosing", "flowing"]
# prefix = ""
# for i in range(len(x[0])):
#     flag = 0
#     temp = x[0][i]
#     print (i)
#     for j in range(1, len(x)):
#         if  x[j][i] != temp:
#             flag = 0
#             break
#         else:  
#             flag = 1       
#     if flag ==1: 
#         prefix+=temp
#     else:
#         pass   
# print(prefix)