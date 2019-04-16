import requests

if __name__ == '__main__':
    url = 'http://www.lunlishipin.com/remote_control.php?time=1555429064&cv=12857fc8f18c9cda917a6d9040ca0f92&lr=0&cv2=f0daa46be344e58756fe25a1b4c3a828&file=%2Fcontents%2Fvideos%2F18000%2F18354%2F18354.mp4&cv3=37f42aaa626e69d24191da9c41a46724&cv4=4af996c827135e6c848b26763699d9bc'
    response = requests.get(url,
                            headers={'Referer': 'http://www.sejie22.com/videos/18354/fd7582da59c5e815c408cf87337937e6/',
                                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
                                     }, stream=True)
    with open('E:\pyspace\down\\test2.mp4', 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if chunk:
                file.write(chunk)
