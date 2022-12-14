# START

class Profile:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        # count_of_digits = 0
        # count_of_uppert_letters = 0
        # for char in str(value):
        #     if char.isdigit():
        #         count_of_digits += 1
        #     elif char.isupper:
        #         count_of_uppert_letters += 1
        #
        # if count_of_digits < 1 or count_of_uppert_letters < 1 or len(value) < 8:
        #     raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        is_length_valid = len(value) >= 8
        is_upper_case_present = any([True for char in value if char.isupper()])
        is_numeric_present = any([True for char in value if char.isdigit()])

        if is_upper_case_present and is_numeric_present and is_length_valid:
            self.__password = value
            return

        raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        # astericks_result = ["*" for _ in range(len(self.password))]
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


test_profile = Profile("cccciiii", "AAAA1212")
print(test_profile)

# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')

correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
