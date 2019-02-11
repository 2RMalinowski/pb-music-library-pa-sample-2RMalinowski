import ui

ARTIST = 0
TITLE = 1
CONFIRM_COLOR = ui.GREEN


def delete_album_from(albums):
    while True:
        artist = ui.get_input('Enter artist name: ')
        # title = ui.get_input('Enter album title: ')
        for album in albums:
            if artist == album[ARTIST]:  # and title == album[TITLE]:
                albums.remove(album)
                ui.display_messsge(ui.display_colored_text(CONFIRM_COLOR, 'Album deleted'))
            else:
                ui.display_error_message("There isn't such artist or album title!")
            break
