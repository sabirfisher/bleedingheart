from driver_setup import init_driver
from scraper import search_target, scroll_and_collect
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='STLKR <3')
    parser.add_argument('target', type=str, help='Name of the target to search. Use + to separate words')
    parser.add_argument('--output', type=str, default=f'data/links.txt', help='Output file to save links')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    driver = init_driver()
    try:
        search_target(driver, args.target)
        all_links = scroll_and_collect(driver, args.target, args.output)
        print(f"Found {len(all_links)} unique links across all pages.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
