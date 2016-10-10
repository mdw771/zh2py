# -*- coding: utf-8 -*-

import eyed3
import glob, os
from anjuke import pinyin

folder = os.getcwd() + '/'

filelist = glob.glob('*.mp3')

converter = pinyin.Converter()

for fname in filelist:
    print 'Now on: ' + fname
    f = eyed3.load(fname)
    # write title
    if f.tag.title is not None:
        temp = unicode(converter.convert(f.tag.title).title())
    else:
        temp = unicode(converter.convert(fname).title())
    f.tag.title = temp
    # write artist
    if f.tag.artist is not None:
        temp = unicode(converter.convert(f.tag.artist).title())
        f.tag.artist = temp
    # write album
    if f.tag.album is not None:
        temp = unicode(converter.convert(f.tag.album).title())
        f.tag.album = temp
    # file rename
    temp = converter.convert(fname).title()
    f.tag.save()
    os.rename(fname, temp)
print 'Done!'

