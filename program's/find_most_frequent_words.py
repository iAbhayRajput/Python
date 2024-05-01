#Wap to find the most frequent words in the text file

def find_most_frequent_words(filename):
    try:
        # Open the text file.
        with open(filename, "r") as f:
            # Read the contents of the file.
            text = f.read()

        # Convert the text to lowercase.
        text = text.lower()

        # Split the text into words.
        words = text.split()

        # Create a dictionary to store the frequency of each word.
        word_counts = {}
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

        # Find the most frequent word and its frequency.
        most_frequent_word = max(word_counts, key=word_counts.get)
        frequency = word_counts[most_frequent_word]

        # Print the most frequent word and its frequency.
        print("The most frequent word in the text file is '{}' with a frequency of {}.".format(most_frequent_word, frequency))

        return most_frequent_word, frequency

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None, None


def main():
    # Prompt the user to input the filename.
    filename = input("Enter the name of the text file: ")

    # Find the most frequent words.
    most_frequent_words = find_most_frequent_words(filename)

if __name__ == "__main__":
    main()
