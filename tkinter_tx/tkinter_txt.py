import tkinter
from tkinter_tx import tkinter_solution
from PIL import ImageTk
"""窗体设置"""
# 窗体对象
root = tkinter.Tk()
# 标题
root.title("Kinter Text")
# 窗体大小
root.geometry("500x300")
# 固定窗口大小，限制用户改变,0为固定，None和True为不固定
root.resizable(None, None)
root.config(bg="white")
# 设置窗口图标
img = ImageTk.PhotoImage(file="ic.jpg") #
root.iconphoto(False, img)
# tkinter自带的只能处理gif,不能处理其他类型，其他类型需要用PIL库
# root.iconphoto(False, tkinter.PhotoImage(file="icon.png"))
# 窗口属性设置（全屏，固定，最前等等）
root.attributes("-fullscreen", False)
"""菜单栏"""
# 菜单栏容器
menubar = tkinter.Menu(root)
# 创建菜单项
# 一级菜单
filemenu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="add", command=tkinter_solution.do_it())     # command 后面跟的是方法体
filemenu.add_command(label="del", command=tkinter_solution.do_it())
filemenu.add_command(label="mod", command=tkinter_solution.do_it())
filemenu.add_command(label="get", command=tkinter_solution.do_it())
filemenu.add_separator()    # 添加一条分割线
filemenu.add_command(label="exit", command=root.quit)

# 二级菜单
submenu = tkinter.Menu(filemenu)

##### 注意注意注意，谁的菜单
filemenu.add_cascade(label="sub_list", menu=submenu, underline=0)
submenu.add_command(label="sub_do", command=tkinter_solution.do_it())
# 窗口分块

# 显示菜单栏

root.config(menu=menubar)
# 主窗体循环显示
root.mainloop()