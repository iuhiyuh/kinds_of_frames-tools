# -*- coding: utf-8 -*-
import argparse


def parse_opts():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-videos_path',
        nargs='+',
        type=str,
        help='视频所在文件夹')
    parser.add_argument(
        '-target_path',
        nargs='+',
        type=str,
        help='要写入的文件夹')
    parser.add_argument(
        '-cut_start',
        nargs='+',
        default=0,
        type=int,
        help='从第几帧开始截取')
    parser.add_argument(
        '-cut_end',
        nargs='+',
        default=0,
        type=int,
        help='截取到第几帧')
    args = parser.parse_args()

    return args
