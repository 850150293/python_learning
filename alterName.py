#labelimg标签有错需要替换所以就这样改
#修改xml标签内容
#修改后写入新的xml文件中
#为什么不能就直接在原来的xml中修改然后保存呢，没有找到方法
#路径千万不要用中文，不然会带来麻烦，比如说新建的xml编码用utf-8中文路径会乱码，用gb2312python不能解析

# coding=utf-8
import os
import os.path
import xml.dom.minidom

#获得文件夹中所有文件
FindPath = 'H:\\car\\xml'
FileNames = os.listdir(FindPath)
s = []
classes_list = []
#修改后保存的路径
xml_path = 'H:\\car\\xml3'
for file_name in FileNames:
    if not os.path.isdir(file_name):  # 判断是否是文件夹,不是文件夹才打开
        print (file_name)

    #读取xml文件
    dom = xml.dom.minidom.parse(os.path.join(FindPath,file_name))

    root = dom.documentElement

    # 获取标签对name之间的值
    name = root.getElementsByTagName('name')
    for i in range(len(name)):
        # print (name[i].firstChild.data)
        if name[i] .firstChild.data== 'minibus':
                    name[i].firstChild.data = 'van'
                    print ('修改后的 name')
                    print (name[i].firstChild.data)
        if name[i] .firstChild.data== 'SUV':
                    name[i].firstChild.data = 'suv'
                    print ('修改后的 name')
                    print (name[i].firstChild.data)
        if name[i] .firstChild.data== 'sdan':
                    name[i].firstChild.data = 'sedan'
                    print ('修改后的 name')
                    print (name[i].firstChild.data)
        if name[i] .firstChild.data== 'SEDAN':
                    name[i].firstChild.data = 'sedan'
                    print ('修改后的 name')
                    print (name[i].firstChild.data)
        if name[i] .firstChild.data== 'mnibus':
                    name[i].firstChild.data = 'van'
                    print ('修改后的 name')
                    print (name[i].firstChild.data)
        if name[i] .firstChild.data== 'minius':
                    name[i].firstChild.data = 'van'
                    print ('修改后的 name')
                    print (name[i].firstChild.data)
        if name[i] .firstChild.data== 'miniubs':
                    name[i].firstChild.data = 'van'
                    print ('修改后的 name')
                    print (name[i].firstChild.data)
        if name[i] .firstChild.data== 'hatcgvack':
                    name[i].firstChild.data = 'hatchback'
                    print ('修改后的 name')
                    print (name[i].firstChild.data)			
    #将修改后的xml文件保存
	
    with open(os.path.join(xml_path, file_name), 'w') as fh:
        dom.writexml(fh,encoding="gb2312")
        print('写入name/pose OK!')
    print(classes_list)
    print(len(classes_list))
