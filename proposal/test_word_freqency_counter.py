import unittest
from io import StringIO
from unittest.mock import patch
from word_frequency_counter import read_file, clean_text, count_words, display_results


class TestWordFrequencyCounter(unittest.TestCase):

    def test_read_file(self):
        # Create a temporary file with sample text
        with open('temp_test_file.txt', 'w', encoding='utf-8') as temp_file:
            temp_file.write("This is a sample text file for testing purposes.")

        # Test reading the file
        content = read_file('temp_test_file.txt')
        self.assertEqual(content, "This is a sample text file for testing purposes.")

    def test_clean_text(self):
        # Test cleaning text by removing punctuation and converting to lowercase
        text = "This is, a Sample text - with Punctuation!"
        cleaned_text = clean_text(text)
        self.assertEqual(cleaned_text, "this is a sample text  with punctuation")

    def test_count_words(self):
        # Test counting the frequency of words in a given text
        text = "apple orange banana apple orange"
        word_counts = count_words(text)
        expected_counts = {'apple': 2, 'orange': 2, 'banana': 1}
        self.assertEqual(word_counts, expected_counts)

    def test_display_results(self):
        # Capture print output for testing display_results function
        captured_output = StringIO()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            display_results({'apple': 2, 'orange': 2, 'banana': 1})
            captured_output.write(mock_stdout.getvalue())

        expected_output = "Word Frequency Counter\n----------------------\nWord\t\tFrequency\n----------------------\napple          \t2\norange         \t2\nbanana         \t1\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    # Clean up the temporary test file
    def tearDown(self):
        import os
        if os.path.exists('temp_test_file.txt'):
            os.remove('temp_test_file.txt')

if __name__ == '__main__':
    unittest.main()
