import os
cmd = "proml <input> screenout &" # 已经将proml程序放到/usr/bin/,可以直接使用
os.system(cmd)
# 需要注意的是制作这个进化树需要很长时间，需要必须要保证输出文件有内容时才可以返回
print(os.system("jobs"))
data = ""
while len(data) == 0:
    if os.path.exists("outtree"):   
        with open("outtree", mode = "r") as fp:
            data = fp.read()
# 写完之后，要把之前生成的文件删除，防止再次出现
#cmd = "rm -rf outtree outfile "
print(os.system("jobs"))
os.system(cmd)