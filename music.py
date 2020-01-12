#!/usr/bin/env python3

import csv
import wikipedia
import re
import sys
import json

artists = []
with open('/Users/syoung/Downloads/Music.txt','r') as f:
    next(f)
    reader = csv.reader(f, delimiter='\t')
    for line in reader:
        if line[3] == 'Voice Memos':
            continue
        artist = line[1]
        if artist not in artists:
            artists.append(artist)

artists = sorted(artists)
canadian = []
canada = []

artists_new = []

with open('/Users/syoung/Downloads/Music_results.txt', 'w') as results:
    sys.stdout = results
    count = 0
    for artist in artists:
        count += 1

        print(count)

        if artist == '':
            continue

        wiki_search = wikipedia.search(artist + ' band')
        print(artist)

        try:
            if len(wiki_search) == 0:
                print('No wiki results')
                print('\n')
                print('-' * 40)
                continue
            else:
                wiki_page = wikipedia.page(wiki_search[0])
                print(wiki_search[0])
        except:
            print('{0:30}: {1:30} {2}'.format(artist, wiki_search[0], 'ERROR'))
            print('\n')
            print('-' * 40)
            continue

            print(wiki_search[0])
            print(wiki_search)

        for wiki_summary_line in wiki_page.summary.split('.'):
            if re.match('.*canadian.*', wiki_summary_line, re.IGNORECASE):
                print('\t>>' + wiki_summary_line)

            if re.match('.*canada.*', wiki_summary_line, re.IGNORECASE):
                print('\t>>' + wiki_summary_line)


        print('\n')
        print('-' * 40)

        sys.stdout.flush()
