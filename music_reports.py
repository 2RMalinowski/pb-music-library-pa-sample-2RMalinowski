import ui

ARTIST = 0
TITLE = 1
YEAR = 2
GENRE = 3
DURATION = 4
SEC_IN_MIN = 60
RESULT_COLOR = ui.CYAN


def get_albums_by_genre(albums, genre):
    """
    Get albums by genre

    :param list albums: albums' data
    :param str genre: genre to filter by

    :returns: all albums of given genre
    :rtype: list
    """
    result = [album for album in albums if album[GENRE] == genre]
    ui.print_albums_list(result)


def convert_time_to_sec(duration):
    int_min_sec = [int(element) for element in duration.split(':')]
    return int_min_sec[0] * SEC_IN_MIN + int_min_sec[1]  # 0, 1 indicate indexes of minutes/seconds


def make_duration_list(albums):
    duration_list = [convert_time_to_sec(album[DURATION]) for album in albums]
    return duration_list


def get_longest_album(albums):
    """
    Get album with biggest value in length field.
    If there are more than one such album return the first (by original lists' order)

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """
    duration_list = make_duration_list(albums)
    longest_duration = max(duration_list)
    for album in albums:
        if longest_duration == convert_time_to_sec(album[DURATION]):
            ui.print_list(ui.display_colored_text(RESULT_COLOR, ' '.join(album)))


def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18
    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """
    total_duration_sec = sum(make_duration_list(albums))
    time_in_min = total_duration_sec / SEC_IN_MIN
    ui.print_list(ui.display_colored_text(RESULT_COLOR, round(time_in_min, 2)))


def sort_by_duration(albums):
    albums.sort(key=lambda album: album[DURATION])
    ui.print_albums_list(albums)


def get_genre_list(albums):
    list_of_genre = list(set([album[GENRE] for album in albums]))
    ui.print_list_element_in_line(list_of_genre)
