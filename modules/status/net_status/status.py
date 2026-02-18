import speedtest
import time
import sys
import threading

def fetcher(fetching_flag):
    dots = ["...", "..", ".", " "]
    i = 0

    while fetching_flag[0]:
        sys.stdout.write(f"\rFetching{dots[i % 4]} ")
        sys.stdout.flush()
        time.sleep(0.5)
        i += 1
    sys.stdout.write("\r" + " " * 20 + "\r")
    sys.stdout.flush()

def net_status():
    fetching_flag = [True]
    t = threading.Thread(target=fetcher, args=(fetching_flag,))
    t.start()

    try:
        st = speedtest.Speedtest(secure=True)
        st.get_best_server()
        download = round(st.download() / 1_000_000, 2)
        upload = round(st.upload() / 1_000_000, 2)
        ping = round(st.results.ping)

        fetching_flag[0] = False
        t.join()

        print("=== Network Information ===")
        print("Online: True")
        print(f"Download: {download} mbps")
        print(f"Upload: {upload} mbps")
        print(f"Ping: {ping} ms")

    except Exception as e:
        fetching_flag[0] = False
        t.join()

        print("=== Network Information ===")
        print("Online: False")
        print("Download: 0")
        print("Upload: 0")
        print("Ping: Not Available")
        # Optional: print(f"Error: {e}") for debugging

if __name__ == "__main__":
    net_status()
