# telegram-quest-starter

РњРёРЅРё-СЃС‚Р°СЂС‚РµСЂ РєРІРµСЃС‚-Р±РѕС‚Р° (Telegram) + Docker quickstart.

## Р‘С‹СЃС‚СЂС‹Р№ СЃС‚Р°СЂС‚ (60 СЃРµРєСѓРЅРґ)
`ash
git clone https://github.com/ex1234/telegram-quest-starter
cd telegram-quest-starter
copy .env.example .env
docker compose --profile dev up -d
# РѕС‚РєСЂРѕР№ http://localhost:8080
`

## РџСЂРѕС„РёР»Рё Compose
- Dev: РјРѕРЅС‚РёСЂСѓРµС‚ ./app Рё Р·Р°РїСѓСЃРєР°РµС‚ РЅР°РїСЂСЏРјСѓСЋ
  - Р—Р°РїСѓСЃРє: docker compose --profile dev up -d
- Prod: СЃРѕР±РёСЂР°РµС‚ РѕР±СЂР°Р· Рё Р·Р°РїСѓСЃРєР°РµС‚
  - Р—Р°РїСѓСЃРє: docker compose --profile prod up -d

## Healthcheck
РљРѕРЅС‚РµР№РЅРµСЂ РѕС‚РґР°С‘С‚ GET http://localhost:8080/ СЃРѕ СЃС‚СЂРѕРєРѕР№ "OK".