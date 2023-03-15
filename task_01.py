from collections import Counter


def check_poem(poem: str) -> str:
    phrases = poem.lstrip().split()
    count = tuple(map(Counter, phrases))
    count_list = tuple(map(count_vowel, count))
    if count_list.count(count_list[0]) == len(count_list):
        return 'Парам пам-пам'
    else:
        return 'Пам парам'


def count_vowel(count_letters: dict) -> int:
    count = 0
    all_vowels = ('а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')
    for letter_key in count_letters:
        if letter_key in all_vowels:
            count += count_letters.get(letter_key)
    return count


poem = 'пара-ра-рам рам-пам-папам пам-пам '
print(check_poem(poem))
