#!/usr/bin/python3
# encoding: utf-8
# this is a smith configuration file - http://scripts.sil.org/smith

# set the font name, version, licensing and description
APPNAME = 'fiati'
FAMILY = APPNAME
DESC_SHORT = 'Font with fingering diagram/chart for multiple musical instruments'
DESC_NAME = 'Fiati'

getufoinfo('source/' + FAMILY + '-regular' + '.ufo')
BUILDLABEL = 'alpha'

# set the build and test parameters
TESTSTRING = u'\uE000\uE001\uE002\uE003\uE007\uE008\uE009\uE00A\uE00E\uE010\uE012\uE014\uE015'

# hard-coded fontbakery commands for testing
testCommand('ttfcheck', cmd='${FONTBAKERY} check-profile -v -C -S ../tests/ttfcheck.py ${SRC[0].abspath()} --html ${TGT} 1> /dev/null; true', extracmds=["fontbakery"], shapers=0, ext=".html", coverage="fonts", shell=1, addfontindex='1', fontmode='all')

designspace('source/' + FAMILY + '.designspace',
            target = '${DS:STYLEMAPFAMILYNAME}-${DS:STYLEMAPSTYLENAME}.otf',
            opentype = internal(),
)

designspace('source/' + FAMILY + '.designspace',
            target = '${DS:FILENAME_BASE}.ttf',
            fret = fret(params='-r -b'),
            woff = woff(),
)

def configure(ctx) :
    ctx.find_program('fontbakery')
