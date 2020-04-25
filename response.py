def merge_request(data):
    message = f"""{len(data)} merge requests avec le label 'for review'"""
    return message


def details(data):
    """Should return string in markdown format."""
    message = ''
    i = 1
    for d in data:
        message += (
            f'-------{i}--------\n'
            f'Author: {d["author"]} \n'
            f'Title: {d["title"]} \n'
            f'Squash: {d["squash"]} & Delete branch: {d["delete_branch"]} \n'
            f'Url: {d["url"]} \n'
            ' '
        )
        i += i

    return message
