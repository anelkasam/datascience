import re
SKIP_TAGS = ['file', 'media', 'image']
TAGS = ['category']


def get_link(link: str):
    """
    Parse all in [[some]]. Remove tags, labels etc.
    """
    if link:
        link = link.split('|')[0].lower()
        if re.match(r'^:[a-z]{2}:', link):
            link = link[4:]

        if link.startswith(':'):
            link = link[1:]

        parts = link.split(':', 1)
        if parts[0] in SKIP_TAGS:
            return ''

        if len(parts) > 1:
            link = ':'.join(parts[1:])

    return link


def parse_links(text: str):
    res = []
    start = text.find('[[')
    if start < 0:
        return []

    while start > 0:
        text = text[start + 2:]
        start = text.find('[[')
        close = text.find(']]')
        if 0 < start < close:
            balance = 2
            for i, ch in enumerate(text):
                balance += ch == '['
                balance -= ch == ']'
                if not balance:
                    close = i - 1
                    break
        link = get_link(text[:close])
        if link:
            res.append(link)
        start = text[close+2:].find('[[')

    return res


if __name__ == '__main__':
    with open('text.txt', 'r') as f:
        text = f.read()

    for l in parse_links(text):
        print(l)
