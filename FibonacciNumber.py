class Solution:
		def fib(self, n: int) -> int:
			if n==0: return 0
			elif n==1: return 1
			else:
				l=[1,1]
				for i in range(2,n+1):
					l.append(l[i-1]+l[i-2])
				return l[n-1]
