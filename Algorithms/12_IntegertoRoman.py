class Solution:
    def intToRoman(self, num: int) -> str:
        # 從大到小去比較map_dict's keys與num，只要num>=某一個key，則res存入key相對應的羅馬字母的次數為num除以key取floor、num更新為num除以key的餘數
        # 繼續比較次大的特定數字，重複操作直到num歸零
        # e.g. 2002 -> "MMII"
        # 2002 // 1000 = 2  res:"MM"  2002 % 1000 = 2
        # 2 // 1 = 2 res: "MMII" 2002 % 1 = 0

        # Time complexity: O(len(map_dict))
        # Space complexity: O(1)

        map_dict = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX",
                    5: "V", 4: "IV", 1: "I"}

        if num in map_dict:
            return map_dict[num]

        res = ""

        for k in map_dict.keys():
            if num >= k:
                res += map_dict[k] * (num // k)
                num %= k

        return res
