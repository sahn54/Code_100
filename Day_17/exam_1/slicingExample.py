# Given the list a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], slice it to get the sublists:

# [2, 3, 4] => [2:5]
# [6, 7] => [6:8]
# [0, 2, 4, 6, 8] = > [::2]
# [9, 7, 5, 3] (in reverse order) => [9:2:-2]
# Given the string s = "abcdefghijklmnopqrstuvwxyz", slice it to get the substrings:

# "abc" => [0:3]
# "defg" =>  [3:7]
# "xyz" => [-3:]
# "fedcba" (in reverse order) [::-1][0:6]


# Given the list a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], slice it to get the sublists:

# [1, 3, 5, 7, 9] => [1::2]=> [1:10:2]
# [2, 4, 6, 8] => [2:9:2] => correct
# [9, 7, 5, 3, 1] [-1::-2] => [9:0:-2]
# [0, 2, 4, 6, 8] (in reverse order) [8::-2]
# Given the string s = "The quick brown fox jumps over the lazy dog.", slice it to get the substrings:

# "The"
# "quick brown"
# "dog."
# "o t" (every other character, starting from index 2)


s = (input("Enter a string "))
n = len(s)
start = n//2
end = n if n % 2 == 0 else n + 1
print(s[start:end])
