# 内容
circle.ciと連携したCI/CDができるFlaskアプリサンプル

# 起動手順


DB migration

```
# DB create
docker-compose exec app python migrations/create_database.py

# DB migrate
docker-compose exec app python manage.py db upgrade
```



# CicleCIの設定

|変数名  |説明  |
|---|---|
|`AWS_ACCESS_KEY_ID`  |AWS_ACCESS_KEY_ID  |
|`AWS_SECRET_ACCESS_KEY`  |AWS_SECRET_ACCESS_KEY  |
|`CONTAINER_IMAGE`  |イメージプッシュ先のECRのブランチURL  |