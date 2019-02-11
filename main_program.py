"""
The main program should use functions from music_reports and display modules
"""
import sys

import file_handling
import modify
import music_reports
import ui

MESSAGE_COLOR = ui.ORANGE
ALBUMS_BY_GENRE = '1'
LONGEST_ALBUM = '2'
TOTAL_ALBUM_LENGTH = '3'
DELETE_ALBUM = '4'


def choose_options_menu(albums):
    user_choice = input('Your choice: ')
    if user_choice == '0':
        sys.exit()
    elif user_choice == ALBUMS_BY_GENRE:
        genre = ui.genre('Enter genre of music: ', albums)
        music_reports.get_albums_by_genre(albums, genre)
    elif user_choice == LONGEST_ALBUM:
        music_reports.get_longest_album(albums)
    elif user_choice == TOTAL_ALBUM_LENGTH:
        music_reports.get_total_albums_length(albums)
    elif user_choice == DELETE_ALBUM:
        modify.delete_album_from(albums)
    else:
        ui.display_messsge(ui.display_colored_text(MESSAGE_COLOR, "There isn't such option"))


def display_menu():
    menu_commands = ['Quit',
                     'Albums by genre',
                     'Longest album',
                     'Total album length',
                     'Delete album']
    ui.print_program_menu(menu_commands)


def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should repeat displaying menu and asking for
    input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """


albums = file_handling.import_data('albums_data.txt')
while True:
    display_menu()
    choose_options_menu(albums)

if __name__ == '__main__':
    main()
