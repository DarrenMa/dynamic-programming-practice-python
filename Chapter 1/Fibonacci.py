import stopwatch

class Fibonacci:
    def __init__(self, n):
        # known fibonacci elements at start
        self.f = [0,1]
        self.n = n
 
    def recursive(self, n):
        """
        This method will calculate the fibonacci value of n using recursion
        Although simple in use it is proportionally inefficient the higher n becomes
        """
        if n < 2:
            # print(f"Returning {n}")
            return n
        else:
            # print(f"Calculating fib ({n-1}) + ({n-2})")
            return self.recursive(n-1) + self.recursive(n-2)
 
    def dynamic(self, n):
        """
        This method will calculate the fibonacci value of n using dynamic programming
        Will determine fib for every number up to n and use stored answers for previously calculated numbers
        The higher n is the more efficient this method is compared to recursion
        """
        if n < 2:
            # print(f"Returning {n}")
            return n
        else:
            # add to the list for every number up to n
            # we know 0 and 1, start at 2
            for i in range(2, n):
                # print(f"Appending ({self.f[i-1]}) + ({self.f[i-2]})")
                self.f.append(self.f[i-1] + self.f[i-2])
            # the answer will be the sum of the last 2 list items
            return self.f[-1] + self.f[-2]


Fibonacci1 = Fibonacci(int(input("Find fibonacci of: ")))  #Creates object
timer = stopwatch.Timer()
timer2 = stopwatch.Timer()
timer.start()
print(Fibonacci1.recursive(Fibonacci1.n))
print(f"{timer.stop()}")
print("===========================================================")
timer2.start()
print(Fibonacci1.dynamic(Fibonacci1.n))
print(f"{timer2.stop()}")