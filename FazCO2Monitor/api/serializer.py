from rest_framework import serializers
from .models import PPMData, NowPPM

import datetime
from django.core.mail import EmailMessage

lastAlertDate = datetime.datetime.strptime('1900-1-1 00:00:00', '%Y-%m-%d %H:%M:%S')

class PPMDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PPMData
        fields = ('value', 'date',)

class NowPPMSerializer(serializers.ModelSerializer):
    class Meta:
        model = NowPPM
        fields = ('value',)

    def update(self, instance, validated_data):
        instance.value = validated_data.get('value', instance.value)
        instance.save()

        global lastAlertDate
        now = datetime.datetime.now()
        if((validated_data['value'] > 2000 or validated_data['value'] < 300) and abs(lastAlertDate - now) >= datetime.timedelta(minutes=30)):
            EmailMessage(u'Danger!',u'nowPPM is ' + str(validated_data['value']) + '!' + '\n' + 'Please ventilate',to=['your@gmail.adress']).send()
            lastAlertDate = datetime.datetime.now()

        return instance
