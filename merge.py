from pydub import AudioSegment


def merge_files(logger, sounds, destination_file):
    logger.info('started for loop to merge files')
    for place_in_list, file_path in enumerate(sounds):
        logger.info(f'Appending {file_path} to the merged file')
        if place_in_list == 0:
            merge_f = AudioSegment.from_mp3(file_path)
            continue

        audio_segment = AudioSegment.from_mp3(file_path)
        merge_f = merge_f + audio_segment
        logger.info(f'Appended {file_path} to the merged file')

    logger.info('finished for loop to merge files')

    logger.info('started export the merge file in mp3 format')
    merge_f.export(destination_file, format='mp3')
    logger.info('finished export the merge file')
