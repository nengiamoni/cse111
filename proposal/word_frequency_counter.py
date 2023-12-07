def read_file(file_path):
    """Read the content of a text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def clean_text(text):
    """Clean the text by removing punctuation and converting to lowercase."""
    import string
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator)
    return cleaned_text.lower()

def count_words(text):
    """Count the frequency of each word in the text."""
    word_counts = {}
    words = text.split()

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

def display_results(word_counts):
    """Display the word frequencies in a readable format."""
    print("Word Frequency Counter")
    print("----------------------")
    print("Word\t\tFrequency")
    print("----------------------")

    for word, frequency in word_counts.items():
        print(f"{word.ljust(15)}\t{frequency}")

def word_frequency_counter(file_path):
    """Main function to orchestrate the word frequency counting process."""
    text = read_file(file_path)
    cleaned_text = clean_text(text)
    word_counts = count_words(cleaned_text)
    display_results(word_counts)

if __name__ == "__main__":
    file_path = 'c:/Users/admin/Desktop/CSE111/proposal/word_frequency_counter.py'
    word_frequency_counter(file_path)
