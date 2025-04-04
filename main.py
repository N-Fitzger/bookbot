from stats import get_word_count, get_letter_counts

def get_book_text(file_path):
	with open(file_path) as f:
		file_contents = f.read()
		return file_contents


def main():
	word_arr = get_book_text("books/frankenstein.txt")
	num_words = get_word_count(word_arr)
	letters = get_letter_counts(word_arr)
	print(f"{num_words} words found in the document")
	print(letters)

main()
