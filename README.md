# SRTFileMaker
def:非常简单粗暴的打轴辅助小玩意
凌晨极限打轴，网管也不知道一般字幕组是干什么的，所以自己写了奇怪的东西辅助生成 SRT 文件。如果有什么奇怪的错误……肯定有的因为太困了！适用于连续的演讲，字幕有切换点，记录并且生成 SRT 文件。

### 什么是 SRT ？
SRT 是一个常见的字幕文件，它的格式十分简单，如下：
1
00:02:17,440 --> 00:02:20,375
Senator, we're making
our final approach into Coruscant.

2
00:02:20,476 --> 00:02:22,501
Very good, Lieutenant.

每一小块由四个部分组合而成：
1. 这行字幕的序列号
2. 字幕持续的时间段
3. 字幕本身，可以多行
4. 空行，示意本块字幕结束

参数比想象中的少多了对吧！所以我们可以把字幕要切换的时间点记录下来——如果是演讲，那么它的字幕基本是连续的——不连续就手动改吧。

TimeLineWring.py
通过一直监测用户输入，当输入的是空行——直接敲击回车键，那么就会记录时间点。然后将它格式化成 SRT 文件的时间格式，并且存储到一个名为 TimeLine 的 txt 文件里。通过在终端输入
cd （下载脚本的文件夹）
gnome-terminal -e "python3 TimeLineWriting.py" | ffplay video
来同时打开视频与脚本，它会打开一个空白的终端。手动打开你写下的字幕，在换行的时候敲击回车键以记录时间节点。在最后一句话说完的时候也要记得敲击哦~想要退出可以随意输入一个字符——比如空格并且回车，就能退出啦

注意：ffplay 需要安装ffmpeg，在 ubuntu 里直接 sudo apt(-get) install ffmpeg 就好

WritingSRT.py
利用记录下来的时间节点，输入字幕文件，字幕文件请块与块之间空行。

然后 SRT 文件就完成了……大概吧。

a very simple py code for SRT file
