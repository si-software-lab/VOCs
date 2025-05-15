import re


# transform given text string into a URL-friendly slug
def slugify(text):
    return re.sub(r'[^\w\- ]', '', text).lower().replace(' ', '-')
