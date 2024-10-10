import pandas as pd

# HIV分地区数据
class HIVData:
    def __init__(self, file_path):
        self.year = None
        self.data = pd.read_excel(file_path, header=None)
        self.data = self.data.iloc[:, 1:6]
        self.data = self.data.drop(self.data.index[:3])
        self.data = self.data.drop(self.data.index[-1:])
        self.data.columns = ['地区', '发病数', '死亡数', '发病率(1/10万)', '死亡率(1/10万)']
        self.result_dict = {}
        self.new_keys = {
            '内蒙古': '内蒙古自治区',
            '西    藏': '西藏自治区',
            '新疆': '新疆维吾尔自治区',
            '广    西': '广西壮族自治区',
            '宁夏': '宁夏回族自治区',
            '宁    夏': '宁夏回族自治区',
        }

        self._process_data()

    def _process_data(self):
        for index, row in self.data.iterrows():
            region = row['地区']
            values = [row['发病数'], row['死亡数'], float(row['发病率(1/10万)']), float(row['死亡率(1/10万)'])]
            if region == '全    国':
                self.result_dict['全    国'] = values
            else:
                self.result_dict[region] = values

        # 更新自治区全称
        for old_key, new_key in self.new_keys.items():
            if old_key in self.result_dict:
                self.result_dict.update({new_key: self.result_dict.pop(old_key)})

        # 对发病率和死亡率进行三位小数保留
        for key in self.result_dict.keys():
            try:
                for i in range(2, 4):
                    self.result_dict[key][i] = round(self.result_dict[key][i], 3)
            except TypeError:
                print(f"Key '{key}' has a None value.")

    # 获取发病人数
    def get_cases(self):
        return {k: v[0] for k, v in self.result_dict.items()}

    # 获取死亡人数
    def get_death(self):
        return {k: v[1] for k, v in self.result_dict.items()}

    # 对发病数前十进行排列
    def get_top_n_cities_by_cases(self, n=10):
        cases = self.get_cases()
        sorted_cases = sorted(list(cases.items())[1:], key=lambda x: x[1], reverse=True)
        return sorted_cases[:n]

    # 对死亡数前十进行排列
    def get_top_n_cities_by_death(self, n=10):
        death = self.get_death()
        sorted_cases = sorted(list(death.items())[1:], key=lambda x: x[1], reverse=True)
        return sorted_cases[:n]

    # 获取发病率和死亡率
    def get_rate(self):
        country_values = self.result_dict['全    国']
        return [country_values[2], country_values[3]]
    def get_data(self):
        return self.result_dict

# HIV分年龄数据
class HIVAgeData:
    def __init__(self, file_path):
        self.year = None
        self.data = pd.read_excel(file_path, header=None)
        self.data = self.data.iloc[:, 1:6]
        self.data = self.data.drop(self.data.index[:3])
        self.data = self.data.drop(self.data.index[-1:])
        self.data.columns = ['年龄分组', '发病数', '死亡数', '发病率(1/10万)', '死亡率(1/10万)']
        self.result_dict = {}
        self.age_group_dict = {
            '0-20岁': [],
            '20-30岁': [],
            '30-40岁': [],
            '40-60岁': [],
            '60-80岁': [],
            '80岁及以上': []
        }

        self._process_data()
        self._age_data()

    def _process_data(self):
        for index, row in self.data.iterrows():
            age = row['年龄分组']
            values = [row['发病数'], row['死亡数'], float(row['发病率(1/10万)']), float(row['死亡率(1/10万)'])]
            self.result_dict[age] = values

        # 对发病率和死亡率进行三位小数保留
        for key in self.result_dict.keys():
            try:
                for i in range(2, 4):
                    self.result_dict[key][i] = round(self.result_dict[key][i], 3)
            except TypeError:
                print(f"Key '{key}' has a None value.")

    # 按年龄段分组统计发病人数
    def _age_data(self):
        for k ,v in self.result_dict.items():
            age_str = k[:-1] # 去除'-'
            if age_str == '85及以':
                age_str = '85'
            elif age_str == '不':
                continue
            age = int(age_str)
            if  0 <= age < 20:
                self.age_group_dict['0-20岁'].append(v[:2])
            elif 20 <= age < 30:
                self.age_group_dict['20-30岁'].append(v[:2])
            elif 30 <= age < 40:
                self.age_group_dict['30-40岁'].append(v[:2])
            elif 40 <= age < 60:
                self.age_group_dict['40-60岁'].append(v[:2])
            elif 60 <= age < 80:
                self.age_group_dict['60-80岁'].append(v[:2])
            elif age_str == '85':
                self.age_group_dict['80岁及以上'].append(v[:2])

        for k in self.age_group_dict.keys():
            if self.age_group_dict[k]:
                total_cases = sum(x[0] for x in self.age_group_dict[k])
                total_deaths = sum(x[1] for x in self.age_group_dict[k])
                self.age_group_dict[k] = [total_cases, total_deaths]

    def get_data(self):
        return self.result_dict

    # 获得年龄分组
    def get_age_group(self):
        return self.age_group_dict

