from django.shortcuts import render
import sys, os, shutil, tweepy, collections
from tweepy import API
import json
from io import StringIO


# Create your views here.

auth = tweepy.OAuthHandler("Axt0mv2kupxboLs30wSlWy73s", "JCBmN0ykBiHr7XFSVFJI1JGrfwtXlWnGNFA56tXIdx1aXXxAET")

auth.set_access_token("781216035936538625-tsdTVa15PPxts0bWcJaABAm43HewBCg", "	9kkCjBXXhROi1gXvxWxZgHlhn1iMPFg0DZI7Jj2ZApq76")

api = tweepy.API(auth)

def convert(data):
    if isinstance(data, basestring):
	return str(data)
    elif isinstance(data, collections.Mapping):
	return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
	return type(data)(map(convert, data))
    else:
	return data

def tweets_index(request):
	if os.path.isfile('/home/akeem/NewYorkFatalities/Casualties/affected.json'):
		shutil.move('/home/akeem/NewYorkFatalities/Casualties/affected.json', "/home/akeem/NewYorkFatalities/affected.json")
		json_file = open(r'affected.json').read()
		converted_json_file = StringIO(unicode(json_file))
		json_dictionary = json.load(converted_json_file)
	
	else:
		json_file = open(r'affected.json').read()
                converted_json_file = StringIO(unicode(json_file))
                json_dictionary = json.load(converted_json_file)

	mod_json_dictionary = [convert(json_dictionary[x].items()) for x in range(0, len(json_dictionary))]
	dates = [mod_json_dictionary[x][0][1] for x in range(0, len(mod_json_dictionary))]

		
	killed=[int(mod_json_dictionary[x][3][1]) for x in range(0, len(mod_json_dictionary))]
	
	state = [mod_json_dictionary[x][4][1] for x in range(0,len(mod_json_dictionary))]
	
	state_by_state = []

	states = {'name': []}

	iterobject = iter(json_dictionary)
				
	for row in json_dictionary:
		next_item = iterobject.next()
		if not states['name'].__contains__(next_item['state']):
			state_by_state.append(next_item)
			states['name'].append(next_item['state'])
		else:
			for index in state_by_state:
				if index['state'] == next_item['state']:
					index['losses'] = str(int(index['losses']) + int(next_item['losses']))
				else:
					pass 
						
					
	
	mod_state_by_state = [convert(state_by_state[x].items()) for x in range(0, len(state_by_state))]

	
	sbs_killed=[int(mod_state_by_state[x][3][1]) for x in range(0, len(mod_state_by_state))]
	
	sbs_states = [mod_state_by_state[x][4][1] for x in range(0,len(mod_state_by_state))]
	context = {
			"tragedies": mod_json_dictionary,
			"states": state,
			"killed": killed,
			"dates": list(set(dates)),
			"state_by_state": mod_state_by_state,
			"total_by_state": sbs_killed,
			"cum_states": sbs_states
		}
	
	return render(request, "home.html", context)
	
	
	
