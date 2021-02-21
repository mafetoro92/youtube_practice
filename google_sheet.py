import gspread
from oauth2client.service_account import ServiceAccountCredentials


def insert_row_col(info_sheet):
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('url_python')
    worksheet2 = sheet.worksheet('Sheet2')

    header = ['likes', 'upload_date', 'url']

    l = []
    l.append(header)
    for row in info_sheet:
        l.append(row)

    worksheet2.update(l)