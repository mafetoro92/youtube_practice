import sqlite3
import typing
from logging import Logger


def insert_info(logger: Logger, record_info: typing.List[list[str]]) -> None:
    logger.info('Start our conection with database')
    connection = sqlite3.connect('youtube_database.db')

    c = connection.cursor()
    logger.info('Star insert many records into the table')

    c.executemany("INSERT INTO customers VALUES (?,?,?)", record_info)
    connection.commit()
    logger.info('Finished insert records into the table')

    c.execute("SELECT * FROM customers")
    items = c.fetchall()
    for i in items:
        print(i)
    connection.commit()
    connection.close()
    logger.info('Finished our conection with database')
