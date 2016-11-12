from django.shortcuts import render, HttpResponse
import sys, os, shutil, tweepy, collections
from tweepy import API
import json
from io import StringIO
from time import *
from django.core import mail

#Convert the unix default time zone to EST because we are in New York


# import the tweets model

from models import *


# Create your views here.

def convert(data):
    if isinstance(data, basestring):
	return str(data)
    elif isinstance(data, collections.Mapping):
	return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
	return type(data)(map(convert, data))
    else:
	return data


auth = tweepy.OAuthHandler("40Q6VBaRf0TMBFZZo9jzuOKJZ", "lugG7Pq8vIjXOGRLqo6ssGCzPVin8vmlQsOzjHs6kYiRbCFfd3")

auth.set_access_token("781216035936538625-vJIOI1oz643ExxLaEsl7AUdrojD8Soz", "3rd4h4oNmfTfTHQGqrtjdiZlMCgl69706yoo67DuVQvuu")

api = tweepy.API(auth)

def tweets_index(request):
	if os.path.isfile('/home/akeem/NewYorkFatalities/Casualties/affected.json'):
		shutil.copyfile('/home/akeem/NewYorkFatalities/Casualties/affected.json', '/home/akeem/NewYorkFatalities/affected.json')
		shutil.move('/home/akeem/NewYorkFatalities/Casualties/affected.json', "/home/akeem/NewYorkFatalities/tweets/affected.json")
		json_file = open(r'affected.json').read()
		converted_json_file = StringIO(unicode(json_file))
		try:
			json_dictionary = json.load(converted_json_file)
		except ValueError:
			#re-collect statistics
			print "errors are occuring"	
			return HttpResponse("<h1>Server Crashed Sorry About That</h1>")
	else:
		try:
			json_file = open(r'affected.json').read()
		except ValueError:
			print "errors are occuring"
			return HttpResponse("<h1>Server Crashed Sorry About That</h1>")
                converted_json_file = StringIO(unicode(json_file))
                json_dictionary = json.load(converted_json_file)

	
	state_by_state = []

	states = {'name': []}

	iterobject = iter(json_dictionary)
	
	tzset()	

	os.environ['TZ'] = 'US/Eastern'

	tzset()

	for row in json_dictionary:
		
		date_conversion = strptime(row['date'], "%B %d, %Y")

		try:
			Tweet.objects.get(uid=int(row['uid']))
		except:
			print tzname
			if strftime("%B %d, %Y", date_conversion) == strftime("%B %d, %Y"):
				Tweet.objects.create(uid=int(row['uid']), source=row['source'], date=strftime("%Y-%m-%d", strptime(
				str(row['date']), "%B %d, %Y")))

				api.update_status("A loss of " + row['losses'] + " occurred today, full report at " + row['source'])
	
	

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

	dates = [str(json_dictionary[x]['date']) for x in range(0, len(json_dictionary)-1)]

		
	killed=[str(json_dictionary[x]['losses']) for x in range(0, len(json_dictionary)-1)]
	
	state = [str(json_dictionary[x]['state']) for x in range(0,len(json_dictionary)-1)]
	
				
						
					
	
	mod_state_by_state = [dict(convert(state_by_state[x].items())) for x in range(0, len(state_by_state)-1)]

	
	sbs_killed=[mod_state_by_state[x]['losses'] for x in range(0, len(mod_state_by_state)-1)]
	
	sbs_states = [mod_state_by_state[x]['state'] for x in range(0,len(mod_state_by_state)-1)]
	context = {
			"tragedies": json_dictionary,
			"states": state,
			"killed": killed,
			"dates": list(set(dates)),
			"state_by_state": mod_state_by_state,
			"total_by_state": sbs_killed,
			"cum_states": sbs_states
		}	

	return render(request, "home.html", context)
	
	
	
