import argparse
from urllib.parse import urlparse, parse_qs

def extract_parameters(url):
    parsed_url = urlparse(url)
    # Parse the query parameters from the URL
    parameters = parse_qs(parsed_url.query)
    return parameters

def save_results(results, filename):
    with open(filename, 'w') as file:
        for url, params in results.items():
            file.write(f"URL: {url}\n")
            if params:
                file.write("Parameters:\n")
                for param, values in params.items():
                    file.write(f"  {param}: {', '.join(values)}\n")
            else:
                file.write("No parameters found.\n")
            file.write("\n")

def main():
    parser = argparse.ArgumentParser(description='Crawl URLs and extract parameters.')
    parser.add_argument('urls', nargs='+', help='List of URLs to crawl.')
    parser.add_argument('--output', default='results.txt', help='Output file to save results.')
    args = parser.parse_args()

    results = {}
    for url in args.urls:
        params = extract_parameters(url)
        results[url] = params

    save_results(results, args.output)

if __name__ == '__main__':
    main()
