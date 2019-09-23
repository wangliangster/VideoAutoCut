####################################################################
# This script is adopted from https://zhuanlan.zhihu.com/p/57944345
# This script is modified by Wenjia Zhai
# This script is for extracting audios from videos.
####################################################################

# !brew install ffmpeg # using homebrew to install ffmpeg
# install ffmpeg
# !pip install pydub
# install pydub

import sys
sys.path.append('/path/to/ffmpeg')
import os
import glob
from pydub import AudioSegment

video_dir = '/Users/wenjiazhai/Documents/GitHub/data_science_study/work/data/records'  # Path where the videos are located
extension_list = ('*.mp4', '*.flv')

os.chdir(video_dir)
for extension in extension_list:
    for video in glob.glob(extension):
        wav_filename = os.path.splitext(os.path.basename(video))[0] + '.wav'
        if os.path.exists(wav_filename):
            next
        else:
            AudioSegment.from_file(video).export(wav_filename, format='wav')