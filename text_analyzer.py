from collections import Counter

def analyze_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.lower().split()
    freqs = Counter(words)  # replaces word_count_dict
    long_words = [w for w in words if len(w) > 3]
    for w in words:
        if len(w) > 3:
            long_words.append(w)
    print(f"Total words: {len(words)}")
    print(f"Unique words: {len(freqs)}")
    print("Top words:")
    for word, count in freqs.most_common(5):
        print(f"'{word}': {count}")
    print(f"Long words (more than 3 characters): {len(long_words)}")

    
    # Let's count the occurrences of each word.
    word_count_dict = {}
    
    for word_item in my_list:
        if word_item in word_count_dict:
            word_count_dict[word_item] = word_count_dict[word_item] + 1
        else:
            word_count_dict[word_item] = 1
    
    # Now let's find the words with more than 3 characters.
    long_words = []
    for word_element in my_list:
        if len(word_element) > 3:
            long_words.append(word_element)
            
    print(f"Total words: {len(words)}")
    print(f"Unique words: {len(freqs)}")
    print("Top words:")

        for word, count in freqs.most_common(5):
            
            print(f"  '{word}': {count}")
            print(f"Long words (more than 3 characters): {len(long_words)}")
    
    the_file.close()

# You will need to create a text file named 'sample.txt' for testing.
analyze_text("sample.txt")