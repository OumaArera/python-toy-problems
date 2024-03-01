def solution(N):
    # Initialize an empty string to store the result
    result = ""

    # Iterate through the alphabet ('a' to 'z')
    for letter in range(ord('a'), ord('z') + 1):
        # Calculate the number of occurrences for each letter
        occurrences = (N + 25) // 26

        # Repeat each letter the calculated number of occurrences
        result += chr(letter) * occurrences

    # Trim the result string to the desired length N
    result = result[:N]

    return result

# Examples
print(solution(3))   # Output: "abc"
print(solution(5))   # Output: "abcde"
print(solution(30))  # Output: "aabbccddeeffgghhiijjkkllmmnnoo"


