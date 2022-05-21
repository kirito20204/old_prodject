import time
start_time = time.time()
def sum_n(n):
    if n==0:
        return 0
    else:
        return n+sum_n(n-1)

print(sum_n(100))
print("--- %s seconds ---" % (time.time() - start_time))