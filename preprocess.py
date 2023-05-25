import json
import os


class Preprocess:
    def __init__(self):
        self.base_path = 'data/暴雨洪涝/'
        title_list = os.listdir(self.base_path + '未标记暴雨洪涝')
        self.title_set = set([title[:-4] for title in title_list])
        self.label_dict = {'LOC': '受灾地点', 'DB': '承载体', 'AIAC': '受灾面积', 'AIAC2': '受灾面积2',
                           'AInP': '受灾人数', 'AHC': '损毁房屋',
                           'AMP': '失踪人数', 'ATP': '转移安置人口', 'AWP': '最大水深', 'AE': '经济损失',
                           'ATAC': '绝收面积', 'ASAC': '承灾面积',
                           'ADP': '死亡人数', 'AImP': '受灾群众', 'AWD': '积水深度', 'DS': '开始日期', 'DO': '结束日期',
                           'TS': '开始时间', 'TO': '结束时间'}
        self.result_list = []  # 抽取标签后的list

    def get_entity(self, save_path):
        """
        获取每个新闻的实体标注信息
        :param save_path: 结果保存的路径
        """
        time_title_set = set([title[:-4] for title in os.listdir(self.base_path + '时间标签')])
        # 遍历每个新闻
        for title in self.title_set:
            entity_dict = {'title': title[5:]}
            # 遍历每个子文件夹
            for sub_dir in ['暴雨洪涝位置', '承载体标签', '人口面积等标签暴雨洪涝_改', '时间标签']:
                path = self.base_path + sub_dir + '/' + title + '.txt'
                # 处理不存在文件情况
                if sub_dir == '时间标签' and title not in time_title_set:
                    continue
                with open(path, 'r', encoding='UTF-8') as f:
                    line_list = f.readlines()
                    for line in line_list:
                        split_result = line.split(' ')
                        for s in split_result:
                            find_label_result = self.find_label(s)
                            if not find_label_result[0]:
                                continue
                            # 加入集合中
                            if find_label_result[2] not in entity_dict:
                                entity_dict[find_label_result[2]] = set()
                            entity_dict[find_label_result[2]].add(find_label_result[1])
                    f.close()

            # 将set转换为list
            for key in entity_dict.keys():
                if key != 'title':
                    entity_dict[key] = list(entity_dict[key])

            # 将entity_dict加入到result_list中
            self.result_list.append(entity_dict)
        with open(save_path, 'w', encoding='UTF-8') as f:
            json.dump(self.result_list, f, ensure_ascii=False)

    def find_label(self, word):
        if len(word) <= 3:
            return [False]
        i = len(word) - 3
        while i > 0:
            if word[i] == '/':
                if word[i + 1:] in self.label_dict:
                    return [True, word[:i], self.label_dict[word[i + 1:]]]
                else:
                    break
            i -= 1
        return [False]


if __name__ == '__main__':
    a = Preprocess()
    a.get_entity(save_path='data/entity_result.json')
