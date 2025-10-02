# telegram-quest-starter

<!-- BADGES:START -->
[![CI](https://img.shields.io/github/actions/workflow/status/ex1234/telegram-quest-starter/ci.yml?branch=main)](https://github.com/ex1234/telegram-quest-starter/actions)
[![Release](https://img.shields.io/github/v/release/ex1234/=tag)](https://github.com/ex1234/telegram-quest-starter/releases)
[![Stars](https://img.shields.io/github/stars/ex1234/telegram-quest-starter)](https://github.com/ex1234/telegram-quest-starter/stargazers)
[![License](https://img.shields.io/github/license/ex1234/telegram-quest-starter)](https://github.com/ex1234/telegram-quest-starter/blob/main/LICENSE)
<!-- BADGES:END -->

Minimal starter for a Telegram quest bot + Docker quickstart.

## Quickstart (60s)
`ash
git clone https://github.com/ex1234/telegram-quest-starter
cd telegram-quest-starter
copy .env.example .env
docker compose --profile dev up -d
# open http://localhost:8080
`

## Compose profiles
- Dev: mounts ./app and runs directly
  - Start: docker compose --profile dev up -d
- Prod: build image and run
  - Start: docker compose --profile prod up -d

## Healthcheck
Container exposes GET http://localhost:8080/ returning "OK".

---
Read this in Russian: [README.ru.md](README.ru.md)