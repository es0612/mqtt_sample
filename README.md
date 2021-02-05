# MQTT sample code

## about MQTT
ref: https://qiita.com/shohei1913/items/b355ad7d1bb27141176b

![MQTT Image](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F90680%2Ff4e88576-028b-e350-5a09-8fb3116ade2b.png?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&s=85f3489f362204fa5ce5311d7dc6dbd0)


## mqtt broker
https://www.emqx.io/mqtt/public-mqtt5-broker

テストのため上記の公開サーバを利用する。

（**本番では使わないこと**）

## use terminal
1. install mosquitto
https://mosquitto.org/download/

2. open 2 terminal

3. subscribe command
```
mosquitto_sub -h broker.emqx.io -t "/test" -v
```

4. publish command
```
mosquitto_pub -h broker.emqx.io -t "/test" -m "this is test"
```

5. check result

## use python code

- subscriber [subscriber.py](./subscriber.py)
- publisher [publisher.py](./publisher.py)