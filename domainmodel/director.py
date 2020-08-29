class Director:

    def __init__(self, director_full_name: str,
                 director_phone_number: str = None,
                 director_age: int = None,
                 director_email_address: str = None,
                 director_gender: int = None,
                 director_IMDB: str = None
                 ):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

        self.__director_gender = director_gender  # 1 = male, 2 = female, 3 = other
        self.__director_age = director_age
        self.__director_phone_number = director_phone_number
        self.__director_email_address = director_email_address
        self.__director_IMDB = director_IMDB

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        return self.__director_full_name == other.__director_full_name

    def __lt__(self, other):
        return self.__director_full_name < other.__director_full_name

    def __hash__(self):
        return hash(self.__director_full_name)

    # First Name
    @property
    def director_first_name(self) -> str:
        return self.director_full_name[:self.director_full_name.find(
            " ")]

    # Last Name
    @property
    def director_last_name(self) -> str:
        return self.director_full_name[self.director_full_name.rfind(
            " ")+1:]

    # Full Name
    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    @director_full_name.setter
    def director_full_name(self, director_full_name) -> str:
        self.__director_full_name = director_full_name.strip()

    # Gender
    @property
    def director_gender(self) -> int:
        return self.__director_gender

    @director_gender.setter
    def director_gender(self, director_gender) -> str:
        if director_gender in [1, 2, 3]:
            self.__director_gender = director_gender

    # Age
    @property
    def director_age(self) -> int:
        return self.__director_age

    @director_age.setter
    def director_age(self, director_age) -> int:
        self.__director_age = director_age

    # Phone Number
    @property
    def director_phone_number(self) -> str:
        return self.__director_phone_number

    @director_phone_number.setter
    def director_phone_number(self, director_phone_number) -> str:
        self.__director_phone_number = director_phone_number

    # Email Address
    @property
    def director_email_address(self) -> str:
        return self.__director_email_address

    @director_email_address.setter
    def director_email_address(self, director_email_address) -> str:
        self.__director_email_address = director_email_address

    # IMDB Page
    @property
    def director_IMDB(self) -> str:
        return self.__director_IMDB

    @director_IMDB.setter
    def director_IMDB(self, director_IMDB) -> str:
        self.__director_IMDB = director_IMDB
