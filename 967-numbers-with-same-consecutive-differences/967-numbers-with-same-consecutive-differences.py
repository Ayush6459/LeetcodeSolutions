class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        # efficient dfs solution
        if N == 1:
            return [i for i in range(10)]

        # initialize the queue with candidates for the first level
        queue = [digit for digit in range(1, 10)]

        for level in range(N-1):
            next_queue = []
            for num in queue:
                tail_digit = num % 10
                # using set() to avoid duplicates when K == 0
                next_digits = set([tail_digit + K, tail_digit - K])

                for next_digit in next_digits:
                    if 0 <= next_digit < 10:
                        new_num = num * 10 + next_digit
                        next_queue.append(new_num)
            # start the next level
            queue = next_queue

        return queue
        
        
        
        '''
        # my solution using dfs concept
        def generate(s,n,k,res):
            if len(s)==n:
                res.append(int(s))
                return 
            x = int(s[-1])
            if k == 0:
                generate(s+str(x),n,k,res)
            else:
                if x-k >=0:
                    generate(s+str(x-k),n,k,res)
                if x+k<=9:
                    generate(s+str(x+k),n,k,res)
            return res 
        
        result = []
        s = '1'
        while int(s)<=9:
            temp = generate(s,n,k,[])
            result.extend(temp)
            s=str(int(s)+1)
            
        return result
        '''
        