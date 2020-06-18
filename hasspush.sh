#!/bin/bash
HASSACCESSTOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJmOTU0YTVkMjNhNmY0NGZkOTg0ZWM5ZTE0MjI0MGQ4YiIsImlhdCI6MTU5MjUwODUxMSwiZXhwIjoxOTA3ODY4NTExfQ.xpHSsN9QDK92dz5XZKQHjhzruRgaMn8QmOrGvmRO2sM"
UUID=$(cat /proc/sys/kernel/random/uuid)
timestamp=$(date +"%Y/%m/%d/%H%M%S")
celcius=$(cat /sys/bus/w1/devices/28-00000b81f10e/w1_slave | tail -n 1 | awk -F'=' '{print $2/1000}')
fahrenheit=$(awk -v c="$celcius" 'BEGIN {print c * 9/5 + 32}')

jsonhass="{\"state\": \"$fahrenheit\", \"attributes\": {\"unit_of_measurement\": \"°F\", \"friendly_name\": \"Pool Temp\"}}"

curl -X POST -H "Authorization: Bearer $HASSACCESSTOKEN" \
	-H "Content-Type: application/json" \
	-d "$jsonhass" \
	http://hassio.local:8123/api/states/sensor.pool_temp

# json="{\"timestamp\": $(date +'%s'), \"celcius\": $celcius, \"fahrenheit\": $fahrenheit}"

# touch /tmp/$UUID
# echo $json > /tmp/$UUID
# /usr/local/bin/aws s3api put-object --profile iot-s3-writer --region us-east-2 --bucket edsw-iot --key "pool/${timestamp}.json" --body /tmp/$UUID
# rm /tmp/$UUID
