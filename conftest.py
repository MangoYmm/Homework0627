from typing import List


#修改pytest_collection_modifyitems hook函数
#收集上来所有的测试用例之后，修改items的方法
#一般hook 会放在conftest.py函数
#conftest.py是被预先加载的，所以使用这个文件的东西不需要导入这个文件
def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)
    for item in items:
        # item.name测试用例的名字，item.nodeid测试用例的路径
        print(item.name)
        print(item.nodeid)
        # 修改测试用例的编码
        item.name=item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')