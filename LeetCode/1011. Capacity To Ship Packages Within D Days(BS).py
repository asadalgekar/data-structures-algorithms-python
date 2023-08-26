"""
A conveyor belt has packages that must be shipped from one port to another within days days.
The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights).
We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10
"""

# Solution: Optimal Time: O(n log n) Space: O(1)
class Solution:

    def findDays(self, weights, capacity):
        days = 1
        load = 0
        for i in range(len(weights)):
            if load + weights[i] > capacity:
                days += 1
                load = weights[i]
            else:
                load += weights[i]
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minimum = max(weights)
        maximum = sum(weights)

        low = minimum
        high = maximum

        while low <= high:
            mid = (low + high) // 2

            required_days = self.findDays(weights, mid)

            if required_days <= days:
                high = mid - 1

            else:
                low = mid + 1

        return low
