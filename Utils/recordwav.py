#!/usr/bin/env python3

# https://blog.csdn.net/zzZ_CMing/article/details/81739193
# coding：utf-8
# author：zzZ_CMing  CSDN address:https://blog.csdn.net/zzZ_CMing
# 2018/07/12; 15:19
# python3.5

# 2019/09/05
# modified my Wenjia Zhai:
# 1. Now it can store any records, not overwite the existing one anymore;
# 2. Now it can record audioes with any length;
# 3. Now it doesn't ask for confirmation of recording anymore.

import re
import wave
####################################################################
################### generte record file name #######################
###################### modified by Wenjia ##########################
from os import listdir
from os.path import isfile, join

import pyaudio

output_filepath = "/Users/liang/Documents/kkb/wav/"  # 输出件的path
file_list = [f for f in listdir(output_filepath) if isfile(join(output_filepath, f))]
nums = [re.findall(r'\d+', f) for f in file_list if f.endswith('.wav')]
# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
if not nums:
    new_num = 0
else:
    new_num = max([int(f[0]) for f in nums]) + 1
output_filename = "output_" + str(new_num) + ".wav"  # 麦克风采集的语音输入
out_path = output_filepath + output_filename


####################################################################

def get_audio(filepath):
    CHUNK = 256
    FORMAT = pyaudio.paInt16
    CHANNELS = 1  # 声道数
    # RATE = 11025                # 采样率
    RATE = 16000  # 采样率
    RECORD_SECONDS = int(input('设置录音时长:\t'))
    WAVE_OUTPUT_FILENAME = out_path
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("*" * 10, f"开始录音：请在{RECORD_SECONDS}秒内输入语音")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("*" * 10, "录音结束\n")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


# 联合上一篇博客代码使用，就注释掉下面，单独使用就不注释
get_audio(out_path)
