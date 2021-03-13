import typing

def open_file()->typing.List[str]:
    urls = []
    with open('urls.txt') as fp:
        for row in fp:
            urls.append(row)
    return urls
