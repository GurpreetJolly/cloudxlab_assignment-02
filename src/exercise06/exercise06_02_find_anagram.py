def find_anagrams(text):
    words = text.split()
    anagrams = {}
    
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    
    return anagrams

def main():
    print("\n*** Find Anagrams ***")
    text = "listen silent enlist inlets hello world"
    print(f"Finding anagrams in the text: '{text}'")
    anagram_groups = find_anagrams(text)
    print(f"Anagram groups: {anagram_groups}")

    text = "evil vile live veil"
    print(f"Finding anagrams in the text: '{text}'")
    anagram_groups = find_anagrams(text)
    print(f"Anagram groups: {anagram_groups}")


if __name__ == "__main__":
    main()
