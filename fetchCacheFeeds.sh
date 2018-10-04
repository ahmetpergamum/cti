#!/bin/bash

cd /var/www
userId=1
for feedId in {10..11}
do
	echo "Feeds are being fetched from feed $feedId"
	MISP/app/Console/cake Server fetchFeed $userId $feedId  &&
	sleep 10
	echo "Feeds are being cached from feed $feedId"
	MISP/app/Console/cake Server cacheFeed $userId $feedId  &&
	sleep 10

done
