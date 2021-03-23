import gspread
import typing
from oauth2client.service_account import ServiceAccountCredentials
import config


def get_urls_from_googlesheet() -> typing.List[str]:
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(config.GOOGLE_CREDENTIALS,
                                                             scope)  # can you remind me to tell you about config files?
    client = gspread.authorize(creds)
    sheet = client.open(config.GOOGLE_SHEET_NAME).sheet1

    data = sheet.get_all_values()
    urls = data[1:]  # this is list of list containg the url to crawl. The firts index is a header so we are removing it.

    url_values = []
    for l in urls:
        url_values.append(l[0]) #get the string for the list
    return url_values
