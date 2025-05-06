import sys
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen("http://localhost:8000/")
    if response.getcode() == 200:
        print("HEALTHCHECK: Success - HTTP 200")
        sys.exit(0)
    else:
        print(f"HEALTHCHECK: Failed - HTTP {response.getcode()}")
        sys.exit(1)
except urllib.error.URLError as e:
    print(f"HEALTHCHECK: Failed - URL Error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"HEALTHCHECK: Failed - Unexpected error: {e}")
    sys.exit(1)