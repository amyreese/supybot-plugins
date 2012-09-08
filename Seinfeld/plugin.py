# Copyright (c) 2012 John Reese
# Licensed under the MIT License

import re
import cgi
import time
import socket
import urllib
import random
import sqlite3

import supybot.conf as conf
import supybot.utils as utils
import supybot.world as world
from supybot.commands import *
import supybot.ircmsgs as ircmsgs
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

class Seinfeld(callbacks.PluginRegexp):
    threaded = False

    def db(self):
        try:
            db = getattr(self, '_db')
        except:
            db = sqlite3.connect(str(conf.supybot.plugins.Seinfeld.databasePath))
            self._db = db
        return db

    def find_quote(self, topic):
        data = []

        c = self.db().cursor()
        c.execute('SELECT utterance_id FROM sentence WHERE text LIKE ? ORDER BY RANDOM()\
            LIMIT 1', ('%{0}%'.format(topic),))

        result = c.fetchone()
        if result is None:
            return None

        utterance_id, = result

        c.execute('SELECT episode_id, utterance_number FROM utterance WHERE id = ?', (utterance_id,))
        episode_id, utterance_number = c.fetchone()

        c.execute('SELECT season_number, episode_number, title FROM episode WHERE id = ?', (episode_id,))
        season_number, episode_number, episode_title = c.fetchone()

        data.append('s{0}e{1}: {2}'.format(season_number, episode_number, episode_title))

        utterance_start = utterance_number - 2 if utterance_number > 2 else 1
        utterance_end = utterance_start + 4

        c.execute('SELECT id, speaker FROM utterance WHERE episode_id = ? AND\
            utterance_number >= ? AND utterance_number <= ?',
            (episode_id, utterance_start, utterance_end))

        for utterance_id, speaker in c.fetchall():
            c.execute('SELECT text FROM sentence WHERE utterance_id = ?\
                ORDER BY sentence_number', (utterance_id,))
            utterance = ' '.join([text for text, in c.fetchall()])
            data.append('{}: {}'.format(speaker, utterance))

        return data

    def seinfeld(self, irc, msg, args, text):
        """<seinfeld> <subject>

        Returns a random Seinfeld quote containing the subject.
        """
        text = re.sub(r'^\s*me\s*', '', text)
        data = self.find_quote(text)
        if data is None:
            irc.reply('No matching quotes found.')
        else:
            for line in data:
                irc.reply(line)
    seinfeld = wrap(seinfeld, ['text'])

Class = Seinfeld


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
