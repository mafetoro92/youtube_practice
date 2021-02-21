import gspread

from oauth2client.service_account import ServiceAccountCredentials

def sheet_url():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('url_python').sheet1

    data = sheet.get_all_values()
    url_values = []
    for l in data:
        url_values.extend(l)
    url_values.pop(0)
    print(url_values)
    return url_values