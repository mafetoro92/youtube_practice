import gspread
import typing
from oauth2client.service_account import ServiceAccountCredentials


def sheet_url()->typing.List[str]:
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scope) # can you remind me to tell you about config files?
    client = gspread.authorize(creds)
    sheet = client.open('url_python').sheet1

    data = sheet.get_all_values()
    url_values = []
    for l in data:
        url_values.extend(l) # it's better not to use extend.
    url_values.pop(0) # we don't need to use pop here.
    print(url_values) # Use logging and not printing
    return url_values
