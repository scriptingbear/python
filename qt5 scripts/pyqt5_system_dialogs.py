from PyQt5.QtWidgets import *


def msgInfo(widget, title, text, tags=""):
    if tags.strip():
        text = insert_tags(tags, text)
    QMessageBox.information(widget, title, text, QMessageBox.Ok)


def msgAsk(widget, title, text, tags=""):
    if tags.strip():
        text = insert_tags(tags, text)
    result = QMessageBox.question(widget, title, text,
                                  QMessageBox.Yes | QMessageBox.No | QMessageBox.No)
    return result


def msgAttention(widget, title, text, tags=""):
    if tags.strip():
        text = insert_tags(tags, text)
    QMessageBox.warning(widget, title, text)


def msgStop(widget, title, text, tags=""):
    if tags.strip():
        text = insert_tags(tags, text)
    QMessageBox.critical(widget, title, text)


def insert_tags(tags: str, text: str):
    tag_list = tags.split(',')
    open_tags = ""
    close_tags = ""
    for tag in tag_list:
        open_tags += f"<{tag}>"
        close_tags += f"</{tag}>"
    return f"{open_tags}{text}{close_tags}"
