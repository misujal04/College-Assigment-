s = input("Enter a sentence: ")

words = s.split()

if len(words) == 0:
    print("No words entered")
else:
    longest = max(words, key=len)
    shortest = min(words, key=len)

    print("Longest word =", longest)
    print("Shortest word =", shortest)