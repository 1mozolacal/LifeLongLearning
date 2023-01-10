class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        costs.sort()
        bought = 0
        for cost in costs:
            if coins >= cost:
                coins -= cost
                bought += 1
            else:
                break
        return bought
