import os
import sys

from moviepy.editor import *

if __name__ == '__main__':
    title = "权力的游戏S7"
    file_name = "权力的游戏S7.flv"
    root_dir = os.path.join(sys.path[0], 'bilibili_video', title)
    # 载入视频
    video = VideoFileClip(root_dir + "\\" + file_name)
    # 添加到数组
    L = [video]
    # 拼接视频
    final_clip = concatenate_videoclips(L)
    # 生成目标视频文件
    final_clip.to_videofile(os.path.join(root_dir, r'{}.mp4'.format(title)), fps=24, remove_temp=False)
