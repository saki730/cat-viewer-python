todo_list = []

def show_menu():
    print("\nTodoリスト")
    print("1. タスクを追加")
    print("2. タスクを見る")
    print("3. タスクを削除")
    print("4. 終了")

def add_task():
    task = input("追加するタスクを入力してください: ")
    todo_list.append(task)
    print(f"タスク「{task}」を追加しました！")

def view_tasks():
    if not todo_list:
        print("タスクがありません。")
    else:
        print("現在のタスク一覧:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def delete_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("削除するタスク番号を入力してください: "))
            removed = todo_list.pop(task_num - 1)
            print(f"タスク「{removed}」を削除しました！")
        except (IndexError, ValueError):
            print("正しい番号を入力してください！")

while True:
    show_menu()
    choice = input("番号を選んでください: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("アプリを終了します。お疲れ様でした！")
        break
    else:
        print("1〜4の番号を入力してください！")
