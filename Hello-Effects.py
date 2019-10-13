#		python code
#		script_name:
#
#		author:
#		description:
#

from earsketch import *

init()
setTempo(120)
soundOne = ELECTRO_ANALOGUE_LEAD_002
soundTwo = RD_ROCK_POPRHYTHM_MAINDRUMS_20
soundThree = RD_ROCK_POPLEADSTRUM_GUITAR_3
soundFour = RD_ROCK_POPRHYTHM_MAINDRUMS_1
fitMedia(soundOne, 1, 1, 5)
fitMedia(soundTwo, 2, 1, 5)
fitMedia(soundThree, 3, 9, 17)
fitMedia(soundFour, 4, 5, 16)


finish()
