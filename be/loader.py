import os
from data_preprocess import HIVData, HIVAgeData
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def load_hiv_data(year):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "data", "全国艾滋病数据分地区", f"{year}.xlsx")
    print(f"Current working directory: {os.getcwd()}")  # 添加调试信息
    print(f"Loading data from: {data_path}")  # 添加调试信息
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"File not found: {data_path}")
    return HIVData(data_path)

def load_hiv_age_data(year):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "data", "全国艾滋病数据分年龄", f"{year}.xlsx")
    print(f"Current working directory: {os.getcwd()}")  # 添加调试信息
    print(f"Loading age data from: {data_path}")  # 添加调试信息
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"File not found: {data_path}")
    return HIVAgeData(data_path)

def load_hiv_agegroup_data(year):
    age_data = HIVAgeData.get_age_group(load_hiv_age_data(year))
    return age_data

# 初始化 hiv_data
hiv_data = None
hiv_age_data = None
hiv_agegroup_data = None

def get_hiv_data(year):
    global hiv_data
    if hiv_data is None or hiv_data.year != year:
        hiv_data = load_hiv_data(year)
    return hiv_data

def get_hiv_age_data(year):
    global hiv_age_data
    if hiv_age_data is None or hiv_age_data.year != year:
        hiv_age_data = load_hiv_age_data(year)
    return hiv_age_data

def get_hiv_agegroup_data(year):
    global hiv_agegroup_data
    if hiv_agegroup_data is None or hiv_agegroup_data.year != year:
        hiv_agegroup_data = load_hiv_agegroup_data(year)
    return hiv_agegroup_data

year = 2020

def update_year(new_year):
    global year
    print(f"Before update: {year}")
    year = new_year
    print(f"Updated year to {year}")

def get_current_year():
    return year

# 测试
if __name__ == "__main__":
    print(year)
    update_year(2014)
    print(get_current_year())
