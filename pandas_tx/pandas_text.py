import pandas as pd

example1 = {
    '第一组': {'号码': ['15608896578', '15608896580'],
               '模式': ['一对一', '轮显']},
    '第二组': {'号码': ['18964823487', '18964823537', '18964949478'],
               '模式': ['一对一', '解决', 'ji']},
    '第三组': {'号码': ['18964823570'],
               '模式': ['一对一']},
    '第四组': {'号码': ['18964949412'],
               '模式': ['一对一']}
}
"""
DataFrame 可以一对多？
"""
example2 = {
    '第一组': {'号码': ['15608896578', '15608896580'],
               '模式': '一对一'},
    '第二组': {'号码': ['18964823487', '18964823537', '18964949478'],
               '模式': '一对一'},
    '第三组': {'号码': ['18964823570'],
               '模式': '一对一'},
    '第四组': {'号码': ['18964949412'],
               '模式': '一对一'}
}

# ex = {"号码": ["15101416214"], "模式": ["一对一"]}

# ex_list = pd.DataFrame(ex)
# 符合控制台输出格式的字符串
# ex_list = pd.DataFrame(ex).to_string(index=False)
# ex_list.to_excel("test.xlsx",index=False)

# ExcelWriter 可能不直接支持作为上下文管理器。
# with pd.ExcelWriter as writer:
#     for group, data in example1.items():
#         df = pd.DataFrame(data)
#         df.to_excel(writer, sheet_name=group, index=False)

writer = pd.ExcelWriter('test.xlsx')
for group, data in example2.items():
    df = pd.DataFrame(data)
    df.to_excel(writer, sheet_name=group,index=False)
    df.dropna(axis=0, how='any') # 按行删除，存在该行，即删除
    df.dropna(axis=0, how='all') # 按行删除，该行全为空就删除
    df.dropna(axis='columns', thresh=5) # 按列删除，该列空值小于等于5个
writer.close()

# pd.dropna() 丢弃空值的行，并将新的DataFrame作为新的值返回
