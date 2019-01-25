import sys, os
sys.path.append(os.getcwd())
import pytest,yaml

def get_data():
    # 返回yaml文件数据[(),(),()]
    # 存储读取数据
    data_list = []
    with open('./Data' + os.sep +'sum.yml',"r") as f:
    # with open(".\Data" + os.sep +"sum.yaml","r") as f:
        datas = yaml.load(f)
        print(datas)
        for data in datas.get("Sum_Data").values():

            # print(data)
            # for content in data:
                # print(content)
                data_list.append((data.get('a'),data.get('b'),data.get('expect')))
                print(data_list)
    return data_list

class Test_sum:
# class Test_data:
    @pytest.mark.parametrize("a, b,expect", get_data())
    def test_sum(self, a, b, expect):
        assert a + b == expect
# if __name__ == '__main__':
#     pytest.main(['test_sum.py'])