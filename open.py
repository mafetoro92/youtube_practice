urls = []

def open_file():
    with open('urls.txt') as fp:
       fp = open('urls.txt')
       for row in fp:
            urls.append(row)
    return urls