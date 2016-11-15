from django.shortcuts import render, HttpResponse
import sys, os, shutil, tweepy, collections, json, re
from tweepy import API
from time import *
from django.core import mail
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt

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

@xframe_options_exempt
def tweets_index(request):

	json_file = open(r'affected.json')
	empty_list = [] #This will be for inserting/dumping json objects into the array
	if os.path.isfile('/home/akeem/NewYorkFatalities/Casualties/affected.json'):
		shutil.copyfile('/home/akeem/NewYorkFatalities/Casualties/affected.json', '/home/akeem/NewYorkFatalities/affected.json')
		shutil.move('/home/akeem/NewYorkFatalities/Casualties/affected.json', "/home/akeem/NewYorkFatalities/tweets/affected.json")
		try:
			for line in json_file:
				line = line.strip() #remove newline breaks
				if re.search("\,\Z", line):
					empty_list.append(json.loads(line[0:-1]))
				else:
					empty_list.append(json.loads(line))
		except:	
			return HttpResponse("<h1>Server Crashed Sorry About That</h1>")
	else:
		try:
			for line in json_file:
				line = line.strip() #remove newline breaks
				if re.search("\,\Z", line):
					empty_list.append(json.loads(line[0:-1]))
				else:
					empty_list.append(json.loads(line))
		except:
			return HttpResponse("<h1>Server Crashed Sorry About That</h1>")
	
	json_dictionary = empty_list #list will  now represent json_dictionary

	
	###########################################################

	
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
	
	
	
