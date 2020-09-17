class Solution:
    def defangIPaddr(self, address: str) -> str:
        # Time  Complexity -> O(n)
        # Space Complexity -> O(1)
        return address.replace('.', '[.]')