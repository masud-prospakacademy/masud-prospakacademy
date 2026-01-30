
def reverse_string(text):
    return text[::-1]

def count_vowels_consonants(text):
    text = text.lower()
    vowel_count = 0
    consonant_count = 0
    vowels = "aeiou"
    
    for char in text:
        if char.isalpha(): 
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
                
    return vowel_count, consonant_count

def is_palindrome(text):
    cleaned_text = ""
    for char in text.lower():
        if char.isalnum():
            cleaned_text += char
            
    return cleaned_text == cleaned_text[::-1]

phrase = input("Enter a phrase: ")

reversed_phrase = reverse_string(phrase)
print(f"Reversed phrase: {reversed_phrase}")

v_count, c_count = count_vowels_consonants(phrase)
print(f"Vowels: {v_count}, Consonants: {c_count}")

if is_palindrome(phrase):
    print("Is it a palindrome? True")
else:
    print("Is it a palindrome? False")