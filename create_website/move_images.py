#!/usr/bin/env python
# -*- coding: utf-8 -*-

import settings

import os

def copy_images():

    move_files_to_docs(settings.EXAMPLES_PATH)

    move_files_to_docs(settings.CHALLENGES_PATH)


def move_files_to_docs(path_chall):
    files = os.listdir(path_chall)
    for file in files:
        if '.png' in file:
            os.rename(path_chall + file, settings.WEBSITE_PATH + 'img/' + file)


