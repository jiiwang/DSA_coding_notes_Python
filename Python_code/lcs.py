def longest_common_subsequence(str1, str2):
    # Handle edge cases where one or both strings are empty
    if not str1 or not str2:
        return ""

    # Initialize a 2D list to store the length of LCS
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to find the LCS string
    ans = ""
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            ans = str1[i - 1] + ans
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ans

# Example usage
str1 = "serendipitious"
str2 = "precipitation"
print(longest_common_subsequence(str1, str2))  