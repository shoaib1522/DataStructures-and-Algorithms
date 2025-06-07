def can_replicate_ransom_note_magazine(magazine, ransom_note):
    # Split the input strings into words
    magazine_words = magazine.split()
    ransom_note_words = ransom_note.split()
    
    # Create a dictionary to count the occurrences of each word in the magazine
    word_count = {}
    for word in magazine_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Check if each word in the ransom note can be formed using the magazine words
    for word in ransom_note_words:
        if word in word_count and word_count[word] > 0:
            word_count[word] -= 1
        else:
            return "No"
    
    return "Yes"

# Example usage
magazine = "this is a magazine full of words and this magazine is useful"
ransom_note = "this magazine is useful"

result = can_replicate_ransom_note_magazine(magazine, ransom_note)
print(result)  # Output: Yes
