class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        diff = {}
        for t in tasks:
            if not t in diff:
                diff[t] = 1
            else:
                diff[t] += 1

        total = 0
        for i, amount in diff.items():
            if amount < 2:
                return -1
            diff_amount = 0
            if amount % 2 == 1:
                amount -= 3
                diff_amount += 1
            sixs = amount // 6
            amount -= sixs*6
            diff_amount += sixs*2
            twos = amount // 2
            amount -= twos*2
            diff_amount += twos

            total += diff_amount

        return total
