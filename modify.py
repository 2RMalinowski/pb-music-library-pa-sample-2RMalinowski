import ui
import music_reports

ARTIST = 0
TITLE = 1
CONFIRM_COLOR = ui.GREEN


def delete_album_from(albums):
    while True:
        music_reports.get_genre_list(albums)
        genre = ui.get_input('Enter genre or number: ')
        for album in albums:
            if genre == album[GENRE]:
                albums.remove(album)
            ui.display_messsge(ui.display_colored_text(CONFIRM_COLOR, 'Genre deleted'))
        else:
            ui.display_error_message("There isn't such genre!")
        break
