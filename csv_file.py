import csv
import typing
import config


def make_file_csv(files: typing.List[typing.Dict[str, str]]) -> None:
    with open(config.CSV_NAME, 'w') as fp:
        outputwriter = csv.DictWriter(fp, fieldnames=['likes', 'upload_date', 'url'])
        outputwriter.writeheader()
        for row in files:
            outputwriter.writerow(row)
