Zrealizowane kroki (zadanie dodatkowe nr 3)

1. Utworzenie buildera z docker-container

2. Utworzenie i użycie pliku openweather_api_key.txt jako sekretu

Plik zawiera prywatny klucz API dla serwisu OpenWeather. Został wykorzystany za pomocą funkcji --secret i RUN --mount=type=secret w Dockerfile:

3. Budowanie obrazu wieloplatformowego z repozytorium GitHub

4. Weryfikacja manifestu multiarch

docker buildx imagetools inspect weather-app:multiarch

Wynik zawiera wpisy dla platform linux/amd64 oraz linux/arm64.

5. Przesłanie obrazu do lokalnego rejestru (na porcie 5050)

docker tag weather-app:multiarch localhost:5050/weather-app:multiarch
docker push localhost:5050/weather-app:multiarch

6. Przesłanie obrazu na DockerHub

Komentarze

Cache registry (tryb max) był używany lokalnie, ale z powodu błędów HTTPS i ograniczeń localhost rejestru, został pominięty przy przesyłaniu do DockerHub.

Projekt został zbudowany całkowicie na bazie kodu zdalnego (GitHub), spełniając wymóg frontend buildkit + git source.

Wszystkie polecenia zostały wykonane z sukcesem, a manifest został poprawnie wygenerowany.

Pliki umieszczone w repozytorium

Dockerfile

app.py

healthcheck.py

static/ (folder statycznych plików HTML/CSS)

requirements.txt

zadanie1.md, zadanie_dodatkowe.md (sprawozdania)