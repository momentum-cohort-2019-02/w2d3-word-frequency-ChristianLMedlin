string_tester = "thisismystringanditislong"

string_tester = list(string_tester)

used_letters = []

count_checker = []

for i in string_tester:
    if i in string_tester and i not in used_letters:
        used_letters.append(i)
        count_checker.append(string_tester.count(i))
        count_checker.append(i)

print(count_checker)
    