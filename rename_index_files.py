import os
import shutil


def move_md_files(base_path, target_path):
  # 瀏覽基礎路徑中的所有資料夾
  for folder_name in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder_name)

    # 確認是資料夾
    if os.path.isdir(folder_path):
      # 瀏覽資料夾中的所有文件
      for file_name in os.listdir(folder_path):
        if file_name.endswith('.md'):
          source_file_path = os.path.join(folder_path, file_name)
          target_file_path = os.path.join(target_path, file_name)

          # 檢查目標檔案是否已存在
          if os.path.exists(target_file_path):
            print(f'File {target_file_path} already exists, skipping.')
          else:
            shutil.move(source_file_path, target_file_path)
            print(f'Moved {source_file_path} to {target_file_path}')


# 設定基礎路徑和目標路徑
base_path = r'G:\PycharmProjects\20240617marskingx.github.io - edit\content\post'
target_path = r'G:\PycharmProjects\20240617marskingx.github.io - edit\content'

# 執行移動操作
move_md_files(base_path, target_path)
