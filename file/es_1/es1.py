#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Leggere il file testo.txt e mostrane il contenuto a video.

f = open("testo.txt", "r")

cont = f.read()

f.close()

print(cont)
