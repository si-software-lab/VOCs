import re

def slugify(text):
    return re.sub(r'[^\w\- ]', '', text).lower().replace(' ', '-')

def generate_toc(markdown_text):
    toc_lines = []
    for line in markdown_text.splitlines():
        match = re.match(r'^(#{2,6}) (.+)', line)
        if match:
            level = len(match.group(1)) - 1  # Indent by level
            title = match.group(2).strip()
            slug = slugify(title)
            toc_lines.append(f"{'  ' * level}- [{title}](#{slug})")
    return '\n'.join(toc_lines)

# Example usage
with open('../README.md', 'r', encoding='utf-8') as f:
    markdown_content = f.read()

toc = generate_toc(markdown_content)
print("# Table of Contents\n\n" + toc)



