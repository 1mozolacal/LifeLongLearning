class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        all_upper = all([x.isupper() for x in word])
        all_lower = all([x.islower() for x in word])
        capped = all([x.islower() for i, x in enumerate(
            word) if i > 0]) and word[0].isupper()

        return all_upper or all_lower or capped
