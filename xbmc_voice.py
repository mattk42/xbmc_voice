#import android
from urllib2 import urlopen
from urllib import quote_plus
from string import join
from json import loads,dumps

#initialize a few things
#droid = android.Android()

#Settings that define the connection to XBMC
ip="192.168.0.3"
port="8080"
url="http://"+ip+":"+port+"/jsonrpc?request="


#Method to send JsonRPC request to the XBMC API
def callJsonRPC(request):
	req=quote_plus(dumps(request))
	content = urlopen(url+req).read()
	return content

#Method to create request objects.
def createRequest(method,params):
	req = {}
	req['jsonrpc']="2.0"
	req['method']=method
	req['params']=params
	req['id']=1
	return req
	

#Returns the tvshowid for specified tv show
def getShowID(title):
	filter = {}
	filter['field']="title"
	filter['operator']="is"
	filter['value']=title

	params = {}
	params['filter']=filter

	req=createRequest("VideoLibrary.GetTVShows",params)

	content=callJsonRPC(req)
	return loads(content)['result']['tvshows'][0]['tvshowid']

#Returns the movieid for specified movie
def getMovieID(title):
        filter = {}
        filter['field']="title"
        filter['operator']="is"
        filter['value']=title

        params = {}
        params['filter']=filter

	req = createRequest("VideoLibrary.GetMovies",params)
        content=callJsonRPC(req)
        return loads(content)['result']['movies'][0]['movieid']

#Plays an episode of the given tv show, -1 for the latest episode. -1 For all seasons.
def playEpisode(title, episode=-1, unwatched=False, season=-1):
	#Find the episode
	showid=getShowID(title)

        params = {}
	params['tvshowid']=showid
	params['properties'] = ["playcount","episode"]

	if unwatched:
		filter = {}
		filter['field'] = "playcount"
		filter['operator'] = "lessthan"
		filter['value'] = str(1)
        	params['filter']=filter

        if episode != -1:
		filter = {}
                filter['field']="episode"
                filter['operator']="is"
                filter['value']=str(episode)
        	params['filter']=filter


	if season != -1:
		params['season']=season

        req = createRequest("VideoLibrary.GetEpisodes",params)
	print req
	content = callJsonRPC(req)
	print content

	episodeID = loads(content)['result']['episodes'][0]['episodeid']

	#Play the episode
	params = {}
	params['item'] = { "episodeid": episodeID }
	req = createRequest("Player.Open",params)
	content= callJsonRPC(req)

#Plays a movie given a title
def playMovie(title):
        movieID=getMovieID(title)
	params = {}
	params['item'] = { "movieid": movieID }
	req = createRequest("Player.Open",params)
        content= callJsonRPC(req)

#Get the voice command and parse
#
#Acceptable commands are:
# xbmc watch movie the shining - Will play the movie The Shining
# xbmc watch latest the simpsons - Will play the latest episode of The Simpsons
# xbmc watch next family guy - Will play the earliest unwatched episode of Family Guy
# xbmc watch season 1 episode 5 of futurama - Will play S01E05 of Futurama
# xbmc pause - Will play/pause whatever is playing
# xbmc play - Will play/pause whatever is playing.
# xbmc stop - Will stop whatever is playing
# xbmc refesh - Will refresh the video library
#command=droid.getIntent().result[u'extras'][u'%avcomm'].split(' ');
if command[1] == "watch":
	if command[2] == "movie":
		playMovie(join(command[3:]))
	elif command[2] == "latest":
		playEpisode(join(command[3:]))
	elif command[2] == "next":
		playEpisode(join(command[3:]),unwatched=True)
	elif command[2] == "season":
		season=int(command[3])
		episode=int(command[5])
		playEpisode(join(command[7:]), season=season, episode=episode)
elif command[1] == "pause" or command[1] == "play":
	content=callJsonRPC({"jsonrpc":"2.0","method":"Player.PlayPause","params": {"playerid": 1},"id":1})
	print content
elif command[1] == "stop":
	content=callJsonRPC({"jsonrpc":"2.0","method":"Player.Stop","params": {"playerid": 1},"id":1})
elif command[1] == "refresh":
	content=callJsonRPC({"jsonrpc":"2.0","method":"VideoLibrary.scan","id":1})
