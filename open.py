def open_file():
    urls = []
    with open('urls.txt') as fp:
        for row in fp:
            urls.append(row)
    return urls
