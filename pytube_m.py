'''
I got the idea for this from N Ficano's git repo for pytube.
I know the description formatting doesn't show up right when you
use "python pytube_m.py -h", sorry, I'll fix it someday.
In any case, use this to download mp4s (or whatever format you
prefer) from www.youtube.com.
'''

from pytube import YouTube
import argparse
import os

parser = argparse.ArgumentParser(description='''
This is my command line implementation of pytube's tools. \n
Examples \n
	This command will list the files available for download from the specified URL: \n
		python .\pytube_m.py "https://www.youtube.com/watch?v=UDmurhScvno" \n\n
	
	This command will download the video with the specified quality and extension \n
	from the specified URL to the specified directory: \n
		$URL = "https://www.youtube.com/watch?v=UDmurhScvno" \n
		python .\pytube_m.py $URL -ext "mp4" -qual "720p" -dir "C:/users/m/Downloads"
''')
parser.add_argument('URL', type=str, default=None,
                    help='A URL to download videos from')
parser.add_argument('-ext', type=str, default=None,
                    help='Extension to download. Example: "mp4", "mp3"')
parser.add_argument('-qual', type=str, default=None,
                    help='Quality to download. Example: "720p", "1080p"')
parser.add_argument('-dir', type=str, default=os.getcwd(),
                    help='Directory to download to. Default is current directory.')

args = parser.parse_args()
if args.URL != None:
	yt = YouTube(args.URL)
	if (args.qual == None) & (args.ext == None):
		for x in yt.get_videos():
			print(x)
	else:
		yt.get(args.ext,args.qual).download(args.dir)
else:
	print('Must at least provide URL')