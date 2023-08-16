import hashlib
from typing import Any


def return_json_data(data: list[dict[str:Any], ...] | dict[str:Any], is_fail: bool = False, msg_text: None | str = None,
                     allow_null: bool = False, permission: bool = True) -> dict:
    """
    构建返回给前端的数据结构
    :param data: 需要返回的数据
    :param is_fail:  是否是否有问题
    :param msg_text:  数据描述
    :param allow_null:  是否允许数据为空值
    :param permission:  拥有访问权限
    :return:
    """
    if is_fail:
        return {"msgCode": -1, "msgText": 'error' if not msg_text else msg_text, "msgObj": data}
    if not data and not allow_null:
        return {"msgCode": -3, "msgText": '未查询到任何数据' if not msg_text else msg_text, "msgObj": ""}
    if not permission:
        return {"msgCode": -2, "msgText": "没有访问权限" if not msg_text else msg_text, "msgObj": data}
    return {"msgCode": 1, "msgText": "success" if not msg_text else msg_text, "msgObj": data}


def set_password(password: str) -> str:
    # 加密
    m = hashlib.md5()
    m.update(password.encode())
    result = m.hexdigest()
    return result
