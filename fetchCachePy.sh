#!/bin/bash

for feedId in {1..52}
do
	echo "Feeds are being fetched from feed $feedId"
	python3 fetch_events_feed.py -f $feedId
	sleep 60
	echo "Feeds are being cached from feed $feedId"
	python3 cache_events_feed.py -f $feedId
	sleep 60
done


echo "Done!!"
