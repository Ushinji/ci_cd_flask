# 内容
circle.ciと連携したCI/CDができるFlaskアプリサンプル

# 起動手順

イメージのビルド

```
$ docker-compose build
```

pipenv install

```
$ docker-compose run --rm app pipenv install --dev
```

DB migration

```
# DB create
$ docker-compose run --rm app python migrations/create_database.py

# DB migrate
$ docker-compose run --rm app python manage.py db upgrade
```

Start Container

```
$ docker-compose up -d
```

http://localhost:5000 にアクセスして、アプリが表示されることを確認。


コンテナーの状況を確認

```
$ docker-compose ps
```

# テストの実行

```
$ docker-compose run --rm app pipenv run test
# nosetest を実行しています。
```

# linter/formatter

コードをチェック

```
$ docker-compose run --rm app pipenv run lint
# pipenv flake8 . が実行されています。
```

自動整形

```
$ docker-compose run --rm app pipenv run fix
# autopep8 -ivr . が実行されています。
```

# CicleCIの設定

|変数名  |説明  |
|---|---|
|`AWS_ACCESS_KEY_ID`  |AWS_ACCESS_KEY_ID  |
|`AWS_SECRET_ACCESS_KEY`  |AWS_SECRET_ACCESS_KEY  |
|`CONTAINER_IMAGE`  |イメージプッシュ先のECRのブランチURL  |
