word = input()
slice_num = len(word) // 3
first_word = word[:slice_num]
second_word = word[slice_num : slice_num * 2]
third_word = word[slice_num * 2 :]
if first_word == second_word:
    print(first_word)
elif second_word == third_word:
    print(second_word)
else:
    print(third_word)
