ART = 'artlogo.jpg'
ICON = 'icon-default.jpg'
NAME = 'Triple J'
STREAM_URL = 'http://audiostream.c3.abc.net.au/hottest100_a_aac'

def Start():

	ObjectContainer.art = R(ART)
	ObjectContainer.title1 = NAME
	TrackObject.thumb = R(ICON)

@handler('/music/TripleJ', NAME, thumb=ICON, art=ART)
def MainMenu():

	oc = ObjectContainer()
	oc.add(CreateTrackObject(url=STREAM_URL, title=NAME))

	return oc

def CreateTrackObject(url, title, include_container=False):

	track_object = TrackObject(
		key = Callback(CreateTrackObject, url=url, title=title, include_container=True),
		rating_key = url,
		title = title,
		items = [
			MediaObject(
				parts = [
					PartObject(key=Callback(PlayAudio, url=url, ext='aac'))
				],
				container = Container.MP4,
				audio_codec = AudioCodec.AAC,
				audio_channels = 2
			)
		]
	)

	if include_container:
		return ObjectContainer(objects=[track_object])
	else:
		return track_object

def PlayAudio(url):

	return Redirect(url)
