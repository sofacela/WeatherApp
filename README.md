Weather App — GitHub Actions CI/CD (multiarch)

Opis aplikacji

Aplikacja pogodowa zbudowana przy użyciu FastAPI (Python). Użytkownik może wybrać kraj i miasto z listy, a następnie pobrać dane pogodowe z zewnętrznego API OpenWeatherMap. Interfejs użytkownika jest oparty na HTML i Tailwind CSS.

Pipeline (GitHub Actions)

Pipeline wykonuje następujące kroki:

- buduje obraz Dockera na podstawie `Dockerfile`
- wspiera dwie architektury: `linux/amd64` i `linux/arm64` (multiarch)
- wykorzystuje cache przy pomocy rejestru DockerHub (`sofiialaba/cache`)
- skanuje obraz za pomocą narzędzia Trivy pod kątem podatności (CVE)
- przerywa publikację, jeśli wykryto zagrożenia o poziomie `HIGH` lub `CRITICAL`
- publikuje obraz do GitHub Container Registry (GHCR)

Tagowanie obrazów

Obrazy są tagowane w następujący sposób:

- `ghcr.io/sofacela/weather-app:latest` – ostatnia stabilna wersja
- `ghcr.io/sofacela/weather-app:multiarch` – wersja wspierająca wiele architektur

Cache znajduje się pod adresem:  
`sofiialaba/cache:weather-app` (na DockerHub)

Wymagane sekrety (GitHub Secrets)

W repozytorium GitHub dodano w zakładce `Settings > Secrets and variables > Actions` następujące sekrety:

- `GHCR_TOKEN` – token personalny z uprawnieniami `write:packages`
- `DOCKERHUB_TOKEN` – token z DockerHub (dla cache)
- `OPENWEATHER_API_KEY` – klucz API z serwisu OpenWeatherMap

Jak uruchomić

1. Skonfiguruj sekrety w repozytorium GitHub
2. Upewnij się, że pliki projektu są obecne:  
   `app.py`, `Dockerfile`, `requirements.txt`, `healthcheck.py`, `static/`, `.github/workflows/build.yml`
3. Wykonaj `push` do gałęzi `main`
4. Pipeline automatycznie:
   - zbuduje obraz
   - wykona skan Trivy
   - opublikuje obraz do GHCR (jeśli nie ma zagrożeń)

Publiczny obraz

Można pobrać i uruchomić opublikowany obraz z GHCR:

docker pull ghcr.io/sofacela/weather-app:latest
docker run -d --env-file .env -p 8000:8000 ghcr.io/sofacela/weather-app:latest

gdzie --env-file .env oznacza, że Docker wczyta zmienne środowiskowe z pliku .env (a mianowicie klucz API oraz numer portu)

Test podatności (CVE)

Wykorzystano narzędzie Trivy do skanowania obrazu Dockera. Jeśli obraz zawiera krytyczne lub poważne podatności, proces zostaje przerwany.

Status

- Pipeline działa poprawnie (przetestowany w GitHub Actions)
- Obraz opublikowany publicznie w GHCR
- Zadanie zrealizowane zgodnie z wymaganiami

W repozytorium znajdują się także:

- screenshots/zad_2/ — zrzuty ekranu pokazujące:

       wykrycie podatności typu high vulnerability w bibliotece starlette,

       aktualizację zależności do wersji wolnej od zagrożeń,

       poprawne uruchomienie kontenera z obrazu pobranego z GHCR (ghcr.io).

- zadanie1.md — dokumentacja Zadania 1 (FastAPI + Docker + Healthcheck).

- zadanie_dodatkowe.md — opis realizacji zadania dodatkowego numer 3 Zadania 1.
