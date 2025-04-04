def get_word_count(text):
	word_arr = text.split()
	word_count = len(word_arr)
	return word_count

def get_letter_counts(text):
	
	lower_text = text.lower()
	letter_counts = {}
	for character in lower_text:
		if character not in letter_counts:
			letter_counts[character] = 1
		else:
			letter_counts[character] += 1
	return letter_counts
