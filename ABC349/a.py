# n = int(input())
# data = input().split()

# sum = 0
# for i in data:
#   sum = sum + int(i)

# sum = sum * -1
# print(sum)
# ------------------
# s = input()

# data = {}
# l = [0]*101
# ans = True
# for i in s:
#   if i not in data:
#     data[f'{i}'] = s.count(i)
#     l[s.count(i)] += 1
#     if(l[s.count(i)] > 2):
#       ans = False

# for i in l:
#   if(i==1):
#     ans = False

# if(ans):
#   print("Yes")
# else:
#   print("No")

# --------------------

# s = input().upper()
# t = input()

# # .lower()
# n = 0
# st = ""

# for i in s:
#   if(n >= len(t)):
#     break
#   if(t[n] == i):
#     n += 1
#     st += i

# if(len(st)==2):
#   st+="X"

# if(st==t):
#   print("Yes")
# else:
#   print("No")

# ---------------------

l,r = (int(x) for x in input().split())
lr = list(range(l,r))

ans = []
n = 0
for j in range(lr[len(lr)-1]):
  left = lr[n]
  print(j,n)
  for i in range(len(lr)):
    num = 2**i
    left_num = num*j
    rigth_num = num*(j+1)
    
    if(left_num==left and rigth_num==lr[i]):
      ans.append([left_num, rigth_num])
      n = i
      break

print(len(ans))
for ansers in ans:
  print(ansers)