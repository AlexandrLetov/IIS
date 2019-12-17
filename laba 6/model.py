notes = {}


def get_item(id):
    if id in notes:
        return notes[id]
    return "NO NOTE FOUND"


def save(id, note):
    notes[id] = note


def get_items():
    return notes


def delete_item(id):
    notes.pop(id)
