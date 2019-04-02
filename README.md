# split frame from video

## 从视频中切分单帧图片
### 说明：
1. main.py：切分目录中所有视频
```bash
python main.py -videos_path "C:\Users\admin\Desktop" \
               -target_path "C:\Users\admin\Desktop\result" \
               -cut_start 10 \
               -cut_end 20
```
2. main_single.py: 切分单个视频
```bash
python main.py -videos_path "C:\Users\admin\Desktop\dog.avi" \
               -target_path "C:\Users\admin\Desktop\result" \
               -cut_start 10 \
               -cut_end 20
```

# excel合并相同行
1. excel.py
```bash
python excel.py "C:\Users\admin\Desktop\dog.csv" "C:\Users\admin\Desktop\result.csv"
```

2. demo
<p>
<img src="utils/demo.gif"\>
</p>

# Check empty directories
如果你想检测root_path下的两层子目录是否为空
1. chake_empty_dir.py 
```python
# 删除空目录
python chake_empty_dir.py "root_path" 1"
# 不删除空目录
python chake_empty_dir.py "root_path" 0"
```