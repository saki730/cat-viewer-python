import random
import string

def generate_password(length):
    # 使う文字のセット（英小文字、英大文字、数字、記号）
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("パスワードの長さを入力してください（例: 12）: "))
        password = generate_password(length)
        print(f"生成されたパスワード: {password}")
    except ValueError:
        print("数字を入力してください！")

if __name__ == "__main__":
    main()
