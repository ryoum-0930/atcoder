import bisect, array
# s = input()
# data = int(s[3:])

# if(data == 316):
#   print("No")
# elif(0 < data and data < 350):
#   print("Yes")
# else:
#   print("No")

# n, q = input().split()
# t = (int(x) for x in input().split())
# n = int(n)
# s = set()
# for i in t:
#   if i in s:
#     s.remove(i)
#   else:
#     s.add(i)

# cnt = len(s)

# print(n-cnt)

n = int(input())
a = [int(i) for i in input().split()]

pos = [0]*n

for i in range(n):
  pos[a[i]-1] = i

ans = []
cnt = 0
for i in range(n):
  if a[i] != i+1:
    cnt+=1
    ans.append([i+1,pos[i]+1])
    idx = a[i] - 1
    a[i], a[pos[i]] = a[pos[i]], a[i]
    pos[i], pos[idx] = i, pos[i]

print(cnt)
[print(a,b) for a,b in ans]