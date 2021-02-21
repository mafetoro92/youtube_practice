import csv

def make_file_csv(logger, files):
    with open('output.csv', 'w') as f1:
        outputWriter = csv.writer(f1)
        outputWriter.writerow(['likes', 'upload date', 'url'])
        for row in files:
            outputWriter.writerow(row)