import youtube_dl


def info_url(logger, info, sound):
    file_info = []  # make this a dictionary. file_info = {}
    logger.info(f'Making information about how many likes have {sound}')
    likes_url = info['like_count']
    logger.info(f'Made the information, now append {likes_url} to a output_info')
    file_info.append(likes_url)  # file_info['likes'] = info['like_count']

    logger.info(f'Making information about when was upload {sound}')
    upload = info['upload_date']
    logger.info(f'Made the information, now append {upload} to a output_info')
    file_info.append(upload)  # file_info['upload_date'] = upload

    logger.info(f'Taking url the {sound}')
    url_video = sound
    logger.info(f'Append {url_video} to a output_info')
    file_info.append(url_video)

    return file_info


def videos_year(file_date):
    year = file_date[0:4]
    return year


def convert_filepath(file_path):
    # I want to change '10 second short music-L5CV53wCWO0.webm' to '10 second short music-L5CV53wCWO0.mp3' the .webm to .mp3
    split_file_path = file_path.rsplit('.', 1)
    new_file_path = f"{split_file_path[0]}.mp3"
    return new_file_path


def download_youtube_files(logger, files):
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

            logger.info(f'Take year the {sound} ')
            file_date = info['upload_date']
            logger.info(f'Took year the {sound} ')

            logger.info('validation if the file is the 2020')
            take_year = videos_year(file_date)
            if take_year == '2020':
                logger.info('If the file is to 2020 we start download')
                download_2020 = ydl.extract_info(sound, download=True)
                logger.info('Download ready')

                logger.info(f'Take name the {sound} ')
                file_path = ydl.prepare_filename(
                    info)  # prepare_filename es otra funcion de ydl va a retun el fiel name del url que le pasemo 10 seconds shor music
                logger.info(f'Took name the {sound} ')

                logger.info('Take information for start making csv ')
                information_files = info_url(logger, info, sound)
                logger.info('Took information for the csv ')

                logger.info(f'converting extension the {file_path}  in .mp3')
                new_file_path = convert_filepath(
                    file_path)  # call funtion, vamos a pasarle como parametro el nombre del url NO LOGGER ya que no requerimos log mens en esta funtion
                logger.info('converted with .mp3 extension ready')

                logger.info(f'Appending {new_file_path} to a output_file list')
                output_files.append(new_file_path)  # se append al empty list
                output_info.append(information_files)
                logger.info(f'Appended {new_file_path} to output_file')

    logger.info('Finished for loop for every single url')
    return output_info, output_files
