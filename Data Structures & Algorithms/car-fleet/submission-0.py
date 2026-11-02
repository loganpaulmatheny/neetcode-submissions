class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Track the speed and position of the cars in an array
        # Iterate through right to left
        # Get the time the car 
        # Check if the time is before the top of the stack, if it is then it should be popped (it'll travel with that car)

        pair = [[p, s] for p, s in zip(position, speed)]
        stack = [] 

        for p, s in sorted(pair, reverse = True):
            stack.append((target - p) / s) # put the finish time for the farthest positioned car on the stack (processing)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        