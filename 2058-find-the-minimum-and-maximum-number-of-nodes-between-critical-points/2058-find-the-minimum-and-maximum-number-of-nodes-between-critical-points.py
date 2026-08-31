'''
- At first, we need to find the Positions of Critical Points
- Either we can store all those Critical Points Positions in some data structure and can do some processing on it
- Otherwise we can think about which Critical Points are Necessary/Needed for calculating the Minimum & Maximum Distance
- Maximum distance will be the distance between the first CP & the last CP
- For minimum distance we need to consider the CP's which are near to each other
- Finding the Maximum Distance is somewhat simpler
- So what we will do means, We will traverse the Linked List and if we see a CP then we will compare that position with the position of the previously seen CP
'''
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # A pointer the denoting previous critical point position
        prevCPPosition = 0, 0
        # A pointer the denoting first critical point position
        firstCPPosition = 0

        # For finding the Minimum distance,, distance between above two is compared

        # As the Boundary Nodes does not belongs to critical points, we have to start from second node
        curNode = head.next 
        # Pointer to store 0-indexing based Position of curNode
        curNodePosition = 1 

        prevNode = head # Prev Pointer for curNode

        minDist = float('inf')
        while curNode.next:
            # For a node to become a CP,, its value should be either greater or smaller than the left and the right notes
            
            if ( (curNode.val > curNode.next.val and curNode.val > prevNode.val) or 
                 (curNode.val < curNode.next.val and curNode.val < prevNode.val)
                ):
                # If this condition gets satisfies,, 
                # What if the Current CP is 1st CP,,
                if firstCPPosition == 0:
                    firstCPPosition = curNodePosition
                    prevCPPosition = curNodePosition
                else:
                    minDist = min(minDist, curNodePosition - prevCPPosition)
                    prevCPPosition = curNodePosition
                
            curNodePosition += 1
            prevNode = curNode
            curNode = curNode.next
            
        # After While Loop,, the prevCPPosition stays at the Last CP

        if minDist == float('inf'):
            return [-1, -1]
        else:
            maxDist = prevCPPosition - firstCPPosition
            return [minDist, maxDist]