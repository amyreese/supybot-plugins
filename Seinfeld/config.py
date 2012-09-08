# Copyright (c) 2012 John Reese
# Licensed under the MIT License

import supybot.conf as conf
import supybot.registry as registry

def configure(advanced):
    from supybot.questions import output, yn
    conf.registerPlugin('Seinfeld', True)
    output("""The Seinfeld plugin has the ability to search a database
              of Seinfeld quotes and print them to a channel on request.""")

Seinfeld = conf.registerPlugin('Seinfeld')
conf.registerGlobalValue(Seinfeld, 'databasePath',
    registry.String('seinfeld.db', """Determines where the plugin will look for
    the quote database."""))

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
