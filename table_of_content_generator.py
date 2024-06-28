import re
from collections import defaultdict


def get_table_of_content_entry(text: str) -> str:
    level = text.count('#')
    space = '  ' * (level - 2) + '* '
    link_text = text.split('#')[-1][1:]

    # Remove extra spaces
    link_text = " ".join(link_text.split())
    # Remove all the links
    link_text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", link_text)
    # Remove the special characters
    link_path = re.sub("[^a-zA-Z0-9\s\u4e00-\u9fff\-]+", "", link_text)
    # Add hyphens and transform to lowercase
    link_path = link_path.replace(' ', '-').lower()

    return f'{space}[{link_text}](#{link_path})'


if __name__ == '__main__':
    with open('README.md', 'rb') as f:
        raw_content = f.read()

    lines = raw_content.decode().replace('\r', '')
    lines = lines.split('\n')
    beginning_index = lines.index('<!-- Beginning of the table of content --> ')
    end_index = lines.index('<!-- End of the table of content --> ')

    content = lines[end_index:]

    level_counter = defaultdict(int)
    table_of_content = []
    for line in content:
        if line.startswith('#'):
            entry = get_table_of_content_entry(line)
            table_of_content.append(entry)

    lines[beginning_index+1:end_index] = table_of_content
    test = '\n'.join(lines)
    with open('README.md', "w", encoding="utf-8") as f:
        f.write(test)
