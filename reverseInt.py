#This is only for positive integers
def main():
	x = 123
	num = reverse(x)
	print num
	
def reverse(x):
	revNum = 0
	while x > 0:
		revNum = revNum * 10 + x % 10
		x = x // 10
	return revNum
main()
