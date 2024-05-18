import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    match = re.search(r'src="([^"]*)"', s)
    url = match.group(1) if match else None
    if url and ('youtube.com/embed' in url or 'youtu.be' in url):
        video_code = url.split("/embed/")[-1]
        return  f"https://youtu.be/{video_code}"
    else:
        return None

if __name__ == "__main__":
    main()
