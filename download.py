import youtube_dl
from logging import Logger
import typing


def info_url(logger: Logger, info: typing.Dict[str, str], sound: str) -> typing.Dict[str, str]:
    file_info = {}  # make this a dictionary. file_info = {}
    logger.info(f'Making information about how many likes have {sound}')
    likes_url = info['like_count']
    logger.info(f'Made the information, now append {likes_url} to a output_info')
    file_info['likes'] = likes_url

    logger.info(f'Making information about when was upload {sound}')
    upload = info['upload_date']
    logger.info(f'Made the information, now append {upload} to a output_info')
    file_info ['upload_date'] = upload

    logger.info(f'Taking url the {sound}')
    url_video = sound
    logger.info(f'Append {url_video} to a output_info')
    file_info ['url'] = url_video

    return file_info


def videos_year(file_date: str) -> str:
    year = file_date[0:4]
    return year


def look_year(logger: Logger, take_year: str) -> bool:
    if take_year == '2020':
        logger.info('If the file is to 2020 will be True')
        return True
    logger.info('If the file is not 2020 will be False')
    return False


def convert_filepath(file_path: str) -> str:
    # I want to change '10 second short music-L5CV53wCWO0.webm' to '10 second short music-L5CV53wCWO0.mp3' the .webm to .mp3
    split_file_path = file_path.rsplit('.', 1)
    new_file_path = f"{split_file_path[0]}.mp3"
    return new_file_path


def download_youtube_files(logger: Logger,files:typing.List[str])->typing.Tuple[typing.List[typing.Dict[str,str]], typing.List[str]]:

    logger.info('writing ydl options')

    ydl_opts = {
        'format': 'bestaudio/best',
        'nocheckcertificate': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }]
    }

    logger.info('Wrote YDL options')
    logger.info('Starting for loop for every single url')

    output_files = []
    output_info = []

    for sound in files:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            logger.info(f'making ydl information the {sound}')
            info = ydl.extract_info(sound,
                                    download=False)  # extract_info es una funcion de ydk que va a return un dictionari con informacin de ese url
            logger.info(f'made ydl information the {sound}')

            logger.info(f'Take name the {sound} ')
            file_path = ydl.prepare_filename(
                info)  # prepare_filename es otra funcion de ydl va a retun el fiel name del url que le pasemo 10 seconds shor music
            logger.info(f'Took name the {sound} ')

            logger.info(f'converting extension the {file_path}  in .mp3')
            new_file_path = convert_filepath(file_path)  # call funtion, vamos a pasarle como parametro el nombre del url NO LOGGER ya que no requerimos log mens en esta funtion
            logger.info('converted with .mp3 extension ready')

            logger.info(f'Take upload date the {sound} ')
            file_date = info['upload_date']
            logger.info(f'Took upload date the {sound} ')

            logger.info(f'Take  years from {sound}')
            take_year = videos_year(file_date)
            logger.info(f'Took years from {sound} ')

            logger.info('Validation if year is 2020')
            validation = look_year(logger, take_year)

            if not validation:
                continue

            logger.info('Start download the videos 2020')
            ydl.extract_info(sound, download=True)

            logger.info('Take information for start making csv file videos 2020 ')
            information_files = info_url(logger, info, sound)
            logger.info('Took information for the csv files videos 2020 ')

            logger.info(f'Appending {new_file_path} to a output_file list')
            output_files.append(new_file_path)  # se append al empty list
            output_info.append(information_files)
            logger.info(f'Appended {new_file_path} to output_file')

    logger.info('Finished for loop for every single url')
    return output_info, output_files
