import json

# markdown maker

"""
converts any dictionary with nested dicts up to 6 levels to markdown
by david balkcom

-----------------------------------
| Depth | Markdown Output Example |
| ----- | ----------------------- |
| 2     | `## Key`                |
| 3     | `### Subkey`            |
| 4     | `#### Deeper key`       |
| 5     | `#####`                 |
| 6     | `######`                |
| 7+    | `- Bullet with indent`  |
-----------------------------------

"""


# modular fcn to compile json content into md
def dict_to_markdown(data_to_convert, level=2):
    markdown = ''
    for key, value in data_to_convert.items():
        heading_level = min(level, 6)
        markdown += f"{'#' * heading_level} {key}\n\n"

        if isinstance(value, dict):
            markdown += dict_to_markdown(value, level + 1)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    markdown += dict_to_markdown(item, level + 1)
                else:
                    markdown += f"{'  ' * (level - 1)}- {item}\n"
        else:
            markdown += f"{'  ' * (level - 1)}- {value}\n"

        markdown += '\n'
    return markdown


# fetch source content
with open('../voc_data_dictionary.json', 'r') as f1:
    data_to_convert = json.load(f1)


# call compiler fcn
markdown_content = dict_to_markdown(data_to_convert)


# write content to markdown file
with open('../data/voc_data_markdown.md', 'w') as f:
    f.write(markdown_content)

print('Markdown file created.')
