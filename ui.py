GENRE = 3


def get_input(message):
    user_input = input(message)
    return user_input


def genre(message, albums):
    while True:
        try:
            genre = input(message)
            if genre not in [album[GENRE] for album in albums]:
                raise ValueError
        except(ValueError):
            error_message = "There isn't such genre"
            display_error_message(error_message)
        else:
            return genre


def print_album_info(album):
    artist_index = 0
    name_index = 1

    print('Album: {} by {}'.format(album[name_index], album[artist_index]))
    print(' | '.join(album[2:]))


def print_albums_list(albums_data):
    for album in albums_data:
        print(' | '.join(album))


def print_program_menu(menu_commands):
    for option in menu_commands:
        print(str(menu_commands.index(option)) + '----->' + option)


def print_command_result(message):
    vertical_spacing = 2
    print(vertical_spacing * '\n' + message)


def display_messsge(message):
    print(message)


def print_list(result):
    print(result)


def print_list_element_in_line(result):
    for element in result:
        print(element)


def display_error_message(message):
    print(display_colored_text(ORANGE, (f'ERROR: {message}')))


#  coloring function
BLUE = '34m'
CYAN = '96m'
GREEN = '92m'
ORANGE = '33m'
RED = '91m'
YELLOW = '93m'


def display_colored_text(color, message):
    colored_text = (f"\033[{color}{message}\033[00m")
    return colored_text
