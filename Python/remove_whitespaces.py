def delete(delete_string):
    pass


def remove_spaces(to_remove):
    removed_string = ''
    for char in to_remove:
        if char != ' ':
            removed_string += char
    return removed_string


def remove_spaces_old(to_remove):
    """

    :type to_remove: str
    """
    initial = len(to_remove)
    for char in to_remove:
        if char != ' ':
            to_remove += char
    return to_remove.replace(to_remove[initial:],'')



print(remove_spaces_old('Hello'))