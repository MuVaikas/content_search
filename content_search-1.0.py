import os

def file_search(dir_path, text):
    print("[Loading] 正在遍历目录并查询内容中....")
    for root, _, files in os.walk(dir_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                with open(file_path, "rb") as f:
                    for line in f:
                        if text in str(line):
                            return f"[Success] 内容存在于文件：{filename},路径为：{file_path}"
            except UnicodeDecodeError:
                print(f"文件 {filename} 编码错误，跳过")
            except PermissionError:
                print(f"文件 {filename} 读取权限不足，跳过")
            except Exception as e:
                print(f"文件 {filename} 读取时发生错误：{e}，跳过")
    return "[End] 查询完毕，内容不存在！"

def main():
    dir_path = input("请输入需要遍历的目录：")
    if not os.path.isdir(dir_path):
        print(f"目录 {dir_path} 不存在，请重新输入。")
        return
    text = input("请输入需要查询的内容：")
    result = file_search(dir_path, text)
    print(result)

if __name__ == "__main__":
    main()
    input()