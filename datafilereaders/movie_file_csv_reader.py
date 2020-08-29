import csv

from CS235FlixSkeleton.domainmodel.movie import Movie
from CS235FlixSkeleton.domainmodel.actor import Actor
from CS235FlixSkeleton.domainmodel.genre import Genre
from CS235FlixSkeleton.domainmodel.director import Director


class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                print(
                    f"Movie {index} with title: {title}, release year {release_year}")
                index += 1
