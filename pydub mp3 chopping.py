'''
This is an example of using pydub for chopping. I forget who authored pydub
but it's available on github.com. This is part 3 of the stuff I use commonly
for extracting audio from youtube videos. To use pydub you need to install a
libav tools binary (essentially download the binary, unzip/rar it if necessary,
copy it to a folder somewhere, then add that folder to your environment variables)
'''

from pydub import AudioSegment
import eyed3
import os

inpth = "C:/Users/m/Downloads"
outpth = "C:/Users/m/Downloads/At the Drive-in - Relationshihp of Command"
filename = "At the Drive-In - Relationship of Command (full album + promo spot).mp3"
art_alb_dict = {'artist': 'At The Drive-In', 'album': 'Relationship of Command'}
song = AudioSegment.from_mp3(os.path.join(inpth,filename))

tracks_times = [['Arcarsenal','1:00'],['Pattern Against User','3:52'],['One Armed Scissor','7:08'],['Sleepwalk Capsules','10:53'],['Invalid Litter Dept.','14:52'],['Mannequin Republic','20:56'],['Enfilade','24:29'],['Rolodex Propaganda','29:02'],['Quarantined','31:55'],['Cosmonaut','37:06'],['Non-Zero Possibility','40:41'],['Incetardis','46:14'],['Extracurricular','53:35']]

tracks_times2 = list(tracks_times)
for i in range(len(tracks_times)):
	# this handles time strings like 'hh:mm:ss', even if 'hh:' is missing
	tracks_times2[i][1] = sum([float(x)*60**(tracks_times[i][1].count(':')-i) for i, x in enumerate(tracks_times[i][1].split(':'))])*1000

for i in range(len(tracks_times2)-1):
	fl = song[tracks_times2[i][1]:tracks_times2[i+1][1]].export(os.path.join(outpth,'{0}.mp3'.format(tracks_times2[i][0])),format='mp3',tags=art_alb_dict)
	audiofile = eyed3.load(os.path.join(outpth,'{0}.mp3'.format(tracks_times2[i][0])))
	audiofile.tag.title = u"{0}".format(tracks_times2[i][0])
	audiofile.tag.track_num = i + 1
	audiofile.tag.save()
	
fl = song[tracks_times2[-1][1]:len(song)].export(os.path.join(outpth,'{0}.mp3'.format(tracks_times2[-1][0])),format='mp3',tags=art_alb_dict)
audiofile = eyed3.load(os.path.join(outpth,'{0}.mp3'.format(tracks_times2[-1][0])))
audiofile.tag.title = u"{0}".format(tracks_times2[-1][0])
audiofile.tag.track_num = len(tracks_times2)
audiofile.tag.save()

fl.close
del fl