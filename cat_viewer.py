import requests
import webbrowser

print("猫ちゃんを表示します！")


def get_random_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        cat_image_url = data[0]['url']
        print(f"猫の画像URL: {cat_image_url}")
        webbrowser.open(cat_image_url)
    else:
        print("猫の画像を取得できませんでした。")

if __name__ == "__main__":
    get_random_cat_image()
