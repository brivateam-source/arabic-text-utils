import re

def normalise(text):
    """Strip diacritics and unify alef, ya and ta-marbuta forms."""
    text = re.sub(r'[\u064B-\u0652]', '', text)
    text = re.sub('[إأآ]', 'ا', text)
    text = text.replace('ى', 'ي').replace('ة', 'ه')
    return re.sub(r'\s+', ' ', text).strip()

if __name__ == "__main__":
    print(normalise("  إِنَّ الْحَمْدَ  لِلَّهِ  "))
