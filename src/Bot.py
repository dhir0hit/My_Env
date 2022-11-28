import json
import random


#
# Bot class
#
class Bot:
    def __init__(self, user=None):
        self.__fetch_data__()
        print(user)

    def command(self, _command):
        """
        getting user command to check right answer
        :param _command: user question
        :return: bot answer
        """
        _command = _command.lower().split()
        return random.choice(self.answers[self.__check_command__(_command)])

    def __check_command__(self, _command):
        """
        checking if command meet what bot can do
        returning dict of match between commands
        """
        _greeting_check = 0
        _notes_check = 0
        _reminder_check = 0
        _music_player_check = 0
        _password_manager_check = 0

        # looping through every commands given
        for element in _command:
            priority = 10
            normal = 1

            # high priority
            if element in ['note', 'notes']:
                _notes_check += priority
            if element in ['reminder', 'remind']:
                _reminder_check += priority
            if element in ['play', 'music', 'sing']:
                _music_player_check += priority
            if element in ['password', 'account']:
                _password_manager_check += priority

            # less priority
            if element in self._greeting:
                _greeting_check += 1
            if element in self._notes:
                _notes_check += 1
            if element in self._reminder:
                _reminder_check += 1
            if element in self._musicPlayer:
                _music_player_check += 1
            if element in self._passwordManager:
                _password_manager_check += 1

            # filter results
            filter_result = {'greeting': _greeting_check,
                             'notes': _notes_check,
                             'reminder': _reminder_check,
                             'musicPlayer': _music_player_check,
                             'passwordManager': _password_manager_check}

            # checking max value
            max_value = max(filter_result, key=filter_result.get)

            # Creating output variable
            _output_ = ""

            # finding correct output
            # ERROR: if max result value is less than 10 and is not a greeting
            # else otuput max value
            if filter_result[max_value] < 10 and max_value != 'greeting':
                 _output_ = "error"
            elif max_value:
                _output_ = max_value

            # returning the output
            return _output_

    def __fetch_data__(self):
        """
        Getting data from json file
        and assigning it to fields
        """
        # opening file
        with open('./utils/botCommands.json') as bot_command_file:
            # getting data
            data = json.load(bot_command_file)['commands']

            # Assigning data
            self._notes = data['questions']['notes']
            self._reminder = data['questions']['reminder']
            self._musicPlayer = data['questions']['musicPlayer']
            self._passwordManager = data['questions']['passwordManager']
            self._greeting = data['questions']['greeting']

            self.answers = data['answers']
