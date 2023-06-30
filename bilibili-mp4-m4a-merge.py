import os
import subprocess
input_folder = "C:/Users/SkyHi/Downloads/"
output_folder = "C:/Users/SkyHi/OneDrive/Video/BIliBIliBeloved/"
files = []
for file in os.listdir(input_folder):
    # 忽略非mp4和m4a后缀的文件
    if file.endswith(".mp4") or file.endswith(".m4a"):
        files.append(os.path.join(input_folder, file))

file_groups = {}
for file in files:
    prefix = os.path.splitext(os.path.basename(file))[0].split("_")[0]
    if prefix in file_groups:
        file_groups[prefix].append(file)
    else:
        file_groups[prefix] = [file]

for prefix, group in file_groups.items():
    if len(group) == 2:  # 只有一组中有两个文件才合并
        # 输出文件名为前缀部分加上"_merged.mp4"
        output_file = os.path.join(output_folder, prefix + "_merged.mp4")
        subprocess.call(['ffmpeg', '-i', group[0], '-i', group[1], '-c', 'copy', output_file])
        print("文件合并成功：", output_file)
