import os

def word_count(text):
    words = text.split()
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

def main():
    print("\n*** Counts the occurrences of each word in a given text ***")
    
    print(f"Reading from 'TheMartian.txt' in {os.getcwd()}...")
    with open("TheMartian.txt", "r") as the_martian_file:
        file_content = the_martian_file.read()
        result = word_count(file_content)
    output_filename = "TheMartianWordCount.txt"

    print(f"Writing word count results to '{output_filename}' in {os.getcwd()}...")
    with open(output_filename, "w") as output_file:
        for word, count in result.items():
            output_file.write(f"{word}: {count}\n")
    print("Done.")

if __name__ == "__main__":
    main()
