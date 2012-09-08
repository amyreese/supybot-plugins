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

    def find_quote(self, topic):
        return topic

    def seinfeld(self, irc, msg, args, text):
        """<seinfeld> <subject>

        Returns a random Seinfeld quote containing the subject.
        """
        text = re.sub(r'^\s*me\s*', '', text)
        data = self.find_quote(text)
        if data:
            irc.reply(data)
        else:
            irc.reply('No matching quotes found.')
    seinfeld = wrap(seinfeld, ['text'])

Class = Seinfeld


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
