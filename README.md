# FazCO2Monitor


##SETUP


###STEP1

pipRequired.txtに記述してあるmoduleをすべてインストールしてください．


###STEP2

/FazCO2Monitor/FazCO2Monitor/setting.pyの147,148行目で，警告メールを送るためのgmailのメールアドレスとパスワードをあなたのものに変更してください．


###STEP3

/FazCO2Monitor/serializer.py26行目で，警告メールを受け取るためのメールアドレスをあなたのものに変更してください．


###STEP4

python manage.py makemigration　と　python manage.py migrate　を実行してください．


###STEP5

python manage.py createsuperuser でアドミンを作成してください．


###STEP6

python manage.py runserver　でサーバーを立ててください．


###STEP7

http://127.0.0.1:8000/admin　のアドミンページで，STEP5で作成したアカウントを使用してログインしてください．


###STEP8

アドミンページで，新しく1つだけnowppmを作成してください．valueは0にしておいてください．


###STEP9

http://127.0.0.1:8000/apiAuth　にアクセスして，tokenを入手し，メモしておいてください．


###STEP10

サーバーを止めてください．


###STEP11

/FazCO2MonitorHardwareの5行目のクオーテーションの間を先程メモしたtokenに置き換えてください．


###STEP12

/FazCO2MonitorHardwareの31,36行目のrunningServerAdressの部分を今後あなたがサーバーを立てるアドレスに変更しておいてください．
今後も内部サーバーを使用する場合は127.0.0.1:8000です．


###STEP13

※内部サーバーを使用する場合はこの作業は必要ありません．
/FazCO2Monitor/FazCO2Monitor/setting.pyの28行目で今後あなたがサーバーを立てるアドレスを大カッコの間に，シングルクオーテーションで囲って入力してください．


###STEP14

※この作業はraspberrypiの電源を切ってから行ってください．
raspberrypiとmhz14aがシリアル通信(UART)できるようにジャンパー線などで接続してください．

raspberrypiのPin配置	https://pinout.xyz/
mhz14aのPin配置		https://www.winsen-sensor.com/d/files/infrared-gas-sensor/mh-z14a_co2-manual-v1_01.pdf


###STEP15

FazCO2Monitorのサーバーを立て，/FazCO2Monitor/main.pyを実行して終了です．
お疲れ様でした．