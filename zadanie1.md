Zadanie 1 - Weather App

1. Opis aplikacji

Aplikacja Weather App to serwer internetowy oparty na FastAPI (Python), który umożliwia wybór kraju i miasta z predefiniowanej listy oraz wyświetla aktualną pogodę dla wybranej lokalizacji, pobierając dane z API OpenWeatherMap. Aplikacja spełnia wymagania zadania:

Wyświetla w logach datę uruchomienia, imię i nazwisko autora oraz port TCP.

Posiada interfejs użytkownika z walidacją (np. Kraków można wybrać tylko dla Polski).

Jest zoptymalizowana pod kątem rozmiaru obrazu Docker i zawiera HEALTHCHECK.

2. Kod aplikacji

app.py
Komentarz: Kod używa FastAPI dla lekkości i automatycznej dokumentacji API. Walidacja na serwerze zapewnia poprawność danych. Logi generowane przy starcie zawierają datę, autora i port, zgodnie z punktem 1a.

static/index.html
Komentarz: Interfejs używa Tailwind CSS dla estetyki. Walidacja na kliencie zapobiega wysyłaniu niepoprawnych żądań. Kod JavaScript asynchroniczny, co zapewnia płynność.

requirements.txt
Komentarz: Stabilne wersje bibliotek

.env
Komentarz: Plik .env nie jest umieszczany w repozytorium(tutaj api oraz port)

3. Dockerfile

Komentarz:
Multi-stage build: Etap builder instaluje zależności i kopiuje kod, etap końcowy tylko uruchamia aplikację.

Bazowy obraz: python:3.12-alpine (~50 MB) dla minimalizacji rozmiaru.

Kompilacja: Dodano gcc, musl-dev, linux-headers dla instalacji zależności.

Optymalizacja cache: requirements.txt kopiowany jako pierwszy, aby warstwy z zależnościami były cache'owane.

Minimalizacja warstw: Jedna komenda COPY dla kodu aplikacji.

Metadane OCI: Zawierają autora, opis i wersję.

Rozmiar: 105 MB dzięki python:3.12-alpine.

4. Polecenia

a. Budowa obrazu

docker build -t weather-app:latest .

Komentarz: Buduje obraz o nazwie weather-app:latest. Rozmiar: 105 MB.

b. Uruchomienie kontenera

docker run -d -p 8000:8000 --env-file .env --name weather-container weather-app:latest

Komentarz: Uruchamia kontener, mapuje port 8000 i ładuje zmienne środowiskowe z .env. Aplikacja dostępna pod http://localhost:8000.

c. Pobranie logów

docker logs weather-container

Komentarz: Wyświetla logi z informacją o dacie uruchomienia, autorze i porcie

d. Sprawdzenie warstw i rozmiaru

docker images weather-app:latest
docker history weather-app:latest

Komentarz:

docker images: Pokazuje rozmiar (105 MB).

docker history: Wyświetla warstwy (w tym apk add, COPY, RUN, CMD).

e. Sprawdzenie HEALTHCHECK

docker inspect --format='{{.State.Health.Status}}' weather-container

Komentarz: Powinno wyświetlić healthy po ~30-40 sekundach od uruchomienia.

