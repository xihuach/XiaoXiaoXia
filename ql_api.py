import json
导入时间

导入请求

ql_auth_path = '/ql/config/auth.json'
# ql_auth_path = r'D：\Docker\ql\config\auth.json'
ql_url = "http://localhost:5600"


定义 __get_token（） -> str 或 无：
    with open（ql_auth_path， 'r'， encoding='utf-8'） as f：
        j_data = json。负载（f)
    返回j_data。get（'token')


防御 __get__headers（） ->字典：
    头 = {
        'Accept'： 'application/json'，
        'Content-Type'： 'application/json;charset=UTF-8'，
        "授权"："持有者"+__get_token()
    }
    返回标头


# 查询环境变量
定义get_envs（名称： str = 无） -> 列表：
    参数 = {
        't'： int（time.时间（） * 1000)
    }
    如果名称  不是"无"：
        params['searchValue'] = name
    res = 请求。get（ql_url + '/api/envs'， headers=__get__headers（）， params=params)
    j_data = 分辨率。json()
    如果 j_data['code'] == 200：
        返回j_data['数据']
    返回 []


# 新增环境变量
定义post_envs（名称： str， 值： str， 备注： str = 无） -> 列表：
    参数 = {
        't'： int（time.时间（） * 1000)
    }
    数据 = [{
        "名称"：名称，
        '值'：值
    }]
    如果备注不是  无：
        data[0]['remarks'] = 备注
    res = 请求。post（ql_url + '/api/envs'， headers=__get__headers（）， params=params， json=data)
    j_data = 分辨率。json()
    如果 j_data['code'] == 200：
        返回j_data['数据']
    返回 []


# 修改环境变量
def put_envs（_id： str， name： str， value： str， remarks： str = None） -> bool：
    参数 = {
        't'： int（time.时间（） * 1000)
    }
    数据 = {
        "名称"：名称，
        '价值'：价值，
        "_id"： _id
    }
    如果备注不是  无：
        data['remarks'] = remarks
    res = 请求。put（ql_url + '/api/envs'， headers=__get__headers（）， params=params， json=data)
    j_data = 分辨率。json()
    如果 j_data['code'] == 200：
        返回 True
    返回 False


# 禁用环境变量
防御disable_env（_id： str） ->布尔：
    参数 = {
        't'： int（time.时间（） * 1000)
    }
    数据 = [_id]
    res = 请求。put（ql_url + '/api/envs/disable'， headers=__get__headers（）， params=params， json=data)
    j_data = 分辨率。json()
    如果 j_data['code'] == 200：
        返回 True
    返回 False


# 启用环境变量
防御enable_env（_id： str） ->布尔：
    参数 = {
        't'： int（time.时间（） * 1000)
    }
    数据 = [_id]
    res = 请求。put（ql_url + '/api/envs/enable'， headers=__get__headers（）， params=params， json=data)
    j_data = 分辨率。json()
    如果 j_data['code'] == 200：
        返回 True
    返回 False
