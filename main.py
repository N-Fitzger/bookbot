import sys
from stats import get_word_count, get_letter_counts

def get_book_text(file_path):
	with open(file_path) as f:
		file_contents = f.read()
		return file_contents


def main():
	
	try:
		book_dir = sys.argv[1]
	except Exception as e:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	word_arr = get_book_text(book_dir)
	num_words = get_word_count(word_arr)
	letters = get_letter_counts(word_arr)
	
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_dir}")
	print("---------- Word count -----------")
	print(f"Found {num_words} total words")
	print("-------- Character Count --------")
	for list in letters:
		letter = list[0]
		number = list[1]
		if letter.isalpha():
			print(f"{letter}: {number}")
	print("============== END ===============")
main()
