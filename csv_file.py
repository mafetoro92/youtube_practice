import csv
import typing


def make_file_csv(files:typing.List[list]):
    with open('output.csv', 'w') as f1:
        outputWriter = csv.writer(f1)
        outputWriter.writerow(['likes', 'upload date', 'url'])
        for row in files:
            outputWriter.writerow(row)
