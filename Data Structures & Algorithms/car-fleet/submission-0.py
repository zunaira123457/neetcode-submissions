class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
         #some sorting bc if the first car is fast but the second car 
        #is slow then the rest of the cars will also be slow.
        #sort the postion and speed. 

        pairs = sorted(zip(position,speed), reverse = True)
        stack = []

        for p,s in pairs: 
            stack.append((target - p)/s)
            if len(stack)>= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

        



        
       




        

        