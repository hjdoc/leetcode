class Solution(object):
    def fizzBuzz(self, n):

        def convert(i):
            a = "Fizz"
            b = "Buzz"
            if i % 3 == 0 and i % 5 == 0:
                return a+b
            elif i % 3 == 0:
                return a
            elif i % 5 == 0:
                return b
            else:
                return str(i)
        
        return [convert(num) for num in list(range(1, n+1))]
        
