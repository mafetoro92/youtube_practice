import typing

def get_url()->typing.List[str]:
    urls = []
    with open('urls.txt') as fp:
        for row in fp:
            urls.append(row)
    return urls
