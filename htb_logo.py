#!/usr/bin/env python3
"""
Finds the logo URL for a given HackTheBox machine.
"""
import sys
import requests
from bs4 import BeautifulSoup


def get_machine_logo(machine_name):
    """
    Args:
        machine_name: Name of the HTB machine
    Returns:
        str: URL of the machine logo, or None if not found
    """
    # Fetch the main machines listing page (client-side filtering)
    url = "https://www.hackthebox.com/machines"

    try:
        # Fetch the page
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all machine divs
        machine_divs = soup.find_all('div', class_='machine')

        for machine_div in machine_divs:
            # Check if this div has a link to our machine
            link = machine_div.find('a', href=lambda x: x and machine_name.lower() in x.lower())
            if link:
                # Found the machine, now get the logo
                img = machine_div.find('img', class_='lazy')
                if img and img.get('src'):
                    src = img['src']
                    # Handle relative URLs
                    if src.startswith('//'):
                        return f"https:{src}"
                    elif src.startswith('/'):
                        return f"https://www.hackthebox.com{src}"
                    return src

        # Fallback: Try finding img by alt text matching machine name
        alt_img = soup.find('img', alt=lambda x: x and machine_name.lower() in x.lower())
        if alt_img and alt_img.get('src'):
            src = alt_img['src']
            if src.startswith('//'):
                return f"https:{src}"
            elif src.startswith('/'):
                return f"https://www.hackthebox.com{src}"
            return src

        return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error parsing page: {e}", file=sys.stderr)
        return None


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 htb_logo.py <machine_name>")
        print("Example: python3 htb_logo.py Lame")
        sys.exit(1)

    machine_name = sys.argv[1]
    logo_url = get_machine_logo(machine_name)

    if logo_url:
        print(logo_url)
    else:
        print(f"Could not find logo for machine: {machine_name}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
