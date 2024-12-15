# 这个工具能提高插件之间代码的可迁移性，提高开发速度

from typing import Optional
# 简单粗暴的导入所有MCDR内置API
from mcdreforged.api.all import *

# 通用接口，避免反复传server参数。
psi = ServerInterface.psi()
# MCDR的配置信息
MCDRConfig = psi.get_mcdr_config()
# 插件的元数据
plgSelf = psi.get_self_metadata()
# 服务端根目录
serverDir = MCDRConfig["working_directory"]
# 插件的配置目录
configDir = psi.get_data_folder()
# [简易命令构建器](https://docs.mcdreforged.com/zh-cn/latest/plugin_dev/command.html#simple-command-builder)
builder = SimpleCommandBuilder()

def tr(tr_key: str, return_str: Optional[bool] = True):
    '''
    对`ServerInterface.rtr()`进行优化，提高翻译效率。

    参数:
        tr_key (str): 原始或简化后的翻译键名称
        return_str (可选[bool]): 是否尝试转换成字符串减少出错

    返回:
        translation: RTextMCDRTranslation组件
        或tr_to_str: 字符串
    '''
    if tr_key.startswith(f"{plgSelf.id}"):
        translation = psi.rtr(f"{tr_key}")
    else:
        # 使用此前缀代表非本插件的翻译键，则翻译时不会附加本插件的ID，避免错误。
        if tr_key.startswith("#"):
            translation = psi.rtr(tr_key.replace("#", ""))
        else:
            translation = psi.rtr(f"{plgSelf.id}.{tr_key}")
    if return_str:
        tr_to_str: str = str(translation)
        return tr_to_str
    else:
        return translation