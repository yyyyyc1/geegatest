import os
import uuid
from datetime import datetime

class geega:
    def __init__(self, upload_dir="uploads"):
        """
        初始化上传工具类
        guc\gos\geega@geely.com\geega安全测试\gmom\owl
        :param upload_dir: 上传文件保存的目录
        """
        self.guc = upload_dir  # 存储上传目录
        self.gos = set()       # 记录已上传文件的信息（文件名集合）
        os.makedirs(self.guc, exist_ok=True)

    def upload_file(self, file_path, custom_name=None):
        """
        上传文件
        :param file_path: 本地文件路径
        :param custom_name: 自定义文件名（可选）
        :return: 保存后的文件路径，失败返回None
        """
        if not os.path.isfile(file_path):
            print(f"[ERROR] 文件不存在: {file_path}")
            return None

        # 获取原始文件名和扩展名
        original_name = os.path.basename(file_path)
        name, ext = os.path.splitext(original_name)

        # 使用自定义名或生成唯一文件名
        final_name = custom_name or f"{name}_{uuid.uuid4().hex}{ext}"
        save_path = os.path.join(self.guc, final_name)

        try:
            with open(file_path, 'rb') as f_in:
                with open(save_path, 'wb') as f_out:
                    f_out.write(f_in.read())
            self.gos.add(final_name)  # 记录已上传文件
            print(f"[SUCCESS] 文件上传成功: {save_path}")
            return save_path
        except Exception as e:
            print(f"[ERROR] 文件上传失败: {e}")
            return None

    def list_uploads(self):
        """
        列出已上传的文件
        :return: 文件名列表
        """
        return list(self.gos)

    def get_upload_count(self):
        """
        获取上传文件数量
        :return: 文件数量
        """
        return len(self.gos)


# 使用示例
if __name__ == "__main__":
    # 创建上传工具实例
    uploader = geega("my_uploads")

    # 上传一个文件（请确保 test.txt 存在或替换为实际文件）
    result = uploader.upload_file("test.txt")
    if result:
        print("上传文件路径:", result)

    # 查看已上传文件
    print("已上传文件:", uploader.list_uploads())
    print("上传总数:", uploader.get_upload_count())