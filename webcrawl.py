import argparse
from urllib.parse import urlparse, parse_qs

# Function to extract parameters from a URL
def extract_parameters(url):
    parsed_url = urlparse(url)
    # Parse the query parameters from the URL
    parameters = parse_qs(parsed_url.query)
    return parameters

# Function to save the extracted results to output.txt
def save_results(results, filename='output.txt'):
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

# Main function to handle command-line arguments and workflow
def main():
    parser = argparse.ArgumentParser(description='Crawl URLs and extract parameters.')
    parser.add_argument('urls', nargs='+', help='List of URLs to crawl.')  # URLs are required
    args = parser.parse_args()

    results = {}
    # Process each URL and extract its parameters
    for url in args.urls:
        params = extract_parameters(url)
        results[url] = params

    # Save the results to output.txt
    save_results(results)

if __name__ == '__main__':
    main()
