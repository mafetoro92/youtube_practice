import gspread
from oauth2client.service_account import ServiceAccountCredentials
import typing
import config


def insert_row_col(info_sheet: typing.List[typing.Dict[str, str]]) -> None:
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(config.GOOGLE_CREDENTIALS, scope)
    client = gspread.authorize(creds)
    sheet = client.open(config.GOOGLE_SHEET_NAME)
    worksheet2 = sheet.worksheet('Sheet2')

    header = ['likes', 'upload_date', 'url']

    l = []
    l.append(header)
    for row in info_sheet[1:]:
        for m in row.values():
            l.append(m)

    worksheet2.update(l)
