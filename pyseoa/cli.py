import argparse
from pyseoa.analyzer import BatchSEOAnalyzer, disallow_keyword, allow_keyword
import os
from typing import List

def main():
    parser = argparse.ArgumentParser('Run SEO Analysis on one or more URLs')
    parser.add_argument('urls', nargs='*', help='List of URLs to analyze')
    parser.add_argument('-f', '--file', help='Path to text or CSV file containing URLs')
    parser.add_argument('-o', '--out', default='seo_reports', help='Output directory')
    parser.add_argument('-c', '--csv', default='seo_summary.csv', help='Combined CSV export path')
    parser.add_argument('-w', '--workers', default=3, help='Number of threads')
    # v0.2.0
    parser.add_argument('-t', '--terminal', action='store_true', help='Prints the report(s) to the terminal')
    parser.add_argument('-g', '--googleapikey', help='Google API Key for PageSpeed Insights')
    
    args = parser.parse_args()

    # Load URLs from file if provided
    urls = args.urls
    if args.file:
        with open(args.file, 'r') as f:
            urls.extend([line.strip() for line in f if line.strip()])
    
    if not urls:
        print('No urls provided.')
        return
    
    # Run batch analysis
    api_key = args.googleapikey
    batch = BatchSEOAnalyzer(urls, api_key)
    batch.run_batch_analysis(max_workers=args.workers)
    
    if args.terminal:
        for url in batch.results.keys():
            header = f'Results for: {url}'
            print(header)
            print('-' * len(header))

            result = batch.results[url]
            max_key_len = max(len(str(k)) for k in result)

            for k, v in batch.results[url].items():
                line = str(k + ':').ljust(max_key_len + 2) + str(v)
                print(line)
    else:
        os.makedirs(args.out, exist_ok=True)
        batch.export_all_to_json(args.out)
        batch.export_combined_csv(args.csv)
        print(f"\nAnalysis complete. JSON reports in '{args.out}', summary CSV at '{args.csv}")
    


if __name__ == '__main__':
    main()