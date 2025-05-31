Weather App — GitHub Actions CI/CD (multiarch)

Opis aplikacji

Aplikacja pogodowa oparta na FastAPI (Python), pozwala użytkownikowi wybrać miasto i kraj i otrzymać dane pogodowe z API OpenWeather.

Pipeline (GitHub Actions)

Ten pipeline:

- Buduje obraz wieloarchitekturny (amd64 i arm64)
- Używa cache z DockerHub
- Wysyła obraz do GitHub Container Registry (GHCR)
- Skanuje obraz na obecność podatności (CVE) przy użyciu Trivy
- Przerywa deployment, jeśli wykryto poważne zagrożenia

Tagowanie obrazów

Obrazy są tagowane jako:

- `ghcr.io/sofacela/weather-app:latest` — ostatni stabilny build
- `ghcr.io/sofacela/weather-app:multiarch` — wersja multiarch

Cache znajduje się pod: `sofiialaba/cache:weather-app`

Wymagane sekrety (GitHub Secrets)

- `GHCR_TOKEN` – token z uprawnieniami `write:packages`
- `DOCKERHUB_TOKEN` – token z DockerHub
- `OPENWEATHER_API_KEY` – klucz API do OpenWeatherMap

Jak uruchomić

1. Utwórz sekrety w GitHub (Settings > Secrets)
2. Pushnij kod do gałęzi `main`
3. Pipeline zbuduje, przeskanuje i opublikuje obraz
