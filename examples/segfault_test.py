import concurrent.futures
import requests

URL = 'http://localhost:8000'

session = requests.Session()
session.mount('http://', requests.adapters.HTTPAdapter(pool_maxsize=20))


def fetch(url):
    resp = session.get(url)
    return resp.status_code


def main():
    urls = [URL] * 50
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        results = list(executor.map(fetch, urls))
    print('Fetched', len(results), 'responses')


if __name__ == '__main__':
    main()
