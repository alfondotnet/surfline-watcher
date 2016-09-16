from SurflineWatcher import SurflineWatcher

def main():
    watcher = SurflineWatcher("http://www.surfline.com/surf-report/ocean-beach-sf-northern-california_4127/")
    print (watcher.get_conditions())

if __name__ == "__main__":
    main()
