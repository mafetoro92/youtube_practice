from download import download_youtube_files
from merge import merge_files
from open import open_file
from csv_file import make_file_csv
from mananger_sound import mananger_sounds
from sheet import sheet_url
from google_sheet import insert_row_col
from twitt import upload_tweet
from table_info import insert_info
import logging

def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
                        handlers=[logging.FileHandler("debug.log"), logging.StreamHandler()])

    logger = logging.getLogger(__name__)
    logger.info('start the program')

    logger.info('getting the urls')
    file= open_file()
    logger.info('got  the urls and ready to download the sounds')

    file_download= sheet_url()

    logger.info(f'got {file}, ready to download')
    download_videos = download_youtube_files(logger, file_download)
    logger.info(f'got {download_videos}, ready to merge')


    logger.info(f'start taking information for the csv file')
    list_for_csv=download_videos[0]
    make_file_csv(logger, list_for_csv)
    insert_row_col(list_for_csv)
    insert_info(logger,list_for_csv)
    logger.info(f'finished making the csv file')


    logger.info(f'starting manipulate the sounds')
    list_for_mananger = download_videos[1]
    mananger_sounds(list_for_mananger)
    merge_files(logger, list_for_mananger, 'merge_alarm.mp3')
    logger.info(f'finished merge the sounds')

    upload_tweet(list_for_mananger)

    logger.info(f'end to the program')

if __name__ == '__main__':
    main()