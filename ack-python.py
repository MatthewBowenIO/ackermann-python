from joblib import Parallel, delayed
import multiprocessing
import time

def ack(x, y):
	if x == 0:
		return y + 1
	elif y == 0:
		return ack(x - 1, 1)
	else:
		return ack(x - 1, ack(x, y - 1))

def acks(cc):
	return Parallel(n_jobs = cc)(delayed(ack)(i, i + 1) for i in range(4))

def main():
	cc = multiprocessing.cpu_count()
 
 	start = time.clock()
 	results = acks(cc)
	stop = time.clock()
	print (stop - start) * 1000
 	
	for i in results:
		print i

if __name__ == "__main__":
	main()