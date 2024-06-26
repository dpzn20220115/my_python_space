import tkinter
import tkinter_solution
from PIL import ImageTk
"""窗体设置"""
# 窗体对象
root = tkinter.Tk()
# 标题
root.title("Kinter Text")
# 窗体大小
root.geometry("500x600")
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
##### 注意注意注意，谁的菜单(否则容易报错)
filemenu.add_cascade(label="sub_list", menu=submenu, underline=0)
submenu.add_command(label="sub_do", command=tkinter_solution.do_it())
# 窗口分块

# 显示菜单栏
root.config(menu=menubar)


"""窗口"""
# 坐标形式
tkinter.Label(root,text="菜单", bg='deepskyblue', font=('Arial', 10)).place(x=0, y=0, width=100, height=40)
# 左右中的方式设置窗口位置
# tkinter.Label(root,text="菜单", bg='blue', font=('Arial', 10)).pack(side=tkinter.LEFT)
# 固定的表格形式
# tkinter.Label(root,text="菜单", bg='blue', font=('Arial', 10)).grid(row=1, column=0)

# 主框架1
frame = tkinter.Frame(root)
frame.place(x=0, y=40, width=100, height=400)

tkinter.Label(frame,text="功能1",bg="lightcyan").place(x=0, y=0, width=100, height=40)
tkinter.Label(frame,text="功能2",bg="lightcyan").place(x=0, y=40, width=100, height=40)
tkinter.Label(frame,text="功能3",bg="lightcyan").place(x=0, y=80, width=100, height=40)
tkinter.Label(frame,text="功能4",bg="lightcyan").place(x=0, y=120, width=100, height=40)
tkinter.Label(frame,text="功能5",bg="lightcyan").place(x=0, y=160, width=100, height=40)

# 主窗体循环显示
root.mainloop()
