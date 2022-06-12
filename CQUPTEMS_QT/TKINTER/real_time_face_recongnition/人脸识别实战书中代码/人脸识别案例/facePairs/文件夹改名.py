import os,sys
from pathlib import Path

# mark = "test_"
# path = "E:/VGGFACE2/VGG-Face2/data/vggface2_test/test"
# old_names = os.listdir(path=path)
#
# for old_name in old_names:
#     if old_name != sys.argv[0]:
#         os.rename(os.path.join(path,old_name),os.path.join(path,path.replace(mark,"")))

#下面是测试文件改名

mark = "ori_"
path = "E:/VGGFACE2/VGG-Face2/data/vggface2_test/test"
path = Path(path)
file_dirs = [x for x in path.iterdir() if x.is_dir()]
for file_dir in file_dirs:
    image_path_list = list(file_dir.glob('*.jpg'))
    for old_name in image_path_list:
        print(old_name)
        os.rename(os.path.join(path, old_name), os.path.join(path, mark + old_name))

