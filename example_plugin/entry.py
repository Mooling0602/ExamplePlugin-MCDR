# 简单粗暴的导入所有MCDR内置API
# 导入本地简化后的工具
from .utils import *
from .module import register_command

default_config = {
    "enabled": False
}

def on_load(server: PluginServerInterface, prev_module):
    '''
    参考[插件被加载](https://docs.mcdreforged.com/zh-cn/latest/plugin_dev/event.html#plugin-loaded)
    '''
    server.logger.info(tr("on_load"))
    server.logger.info("插件暂时只支持中文，写注释比较方便，你可以PR提交英文本地化相关的代码。")
    config = server.load_config_simple('config.json', default_config)
    if config["enabled"]:
        register_command(server)
        server.logger.info(tr("hello_world"))
    else:
        # `plgSelf.id` 即为插件ID字符串
        server.unload_plugin(plgSelf.id)

def on_server_start_pre(server: PluginServerInterface):
    '''
    参考[服务端启动前](https://docs.mcdreforged.com/zh-cn/latest/plugin_dev/event.html#server-start-pre)
    '''
    server.logger.info(tr("on_server_start_pre"))

def on_server_start(server: PluginServerInterface):
    '''
    参考[服务端启动](https://docs.mcdreforged.com/zh-cn/latest/plugin_dev/event.html#server-start)
    '''
    server.logger.info(tr("on_server_start"))

def on_server_startup(server: PluginServerInterface):
    '''
    参考[服务端启动完成](https://docs.mcdreforged.com/zh-cn/latest/plugin_dev/event.html#server-startup)
    '''
    server.logger.info(tr("on_server_startup"))

def on_server_stop(server: PluginServerInterface, server_return_code: int):
    '''
    参考[服务端终止](https://docs.mcdreforged.com/zh-cn/latest/plugin_dev/event.html#server-stop)
    '''
    if server_return_code != 0:
        server.logger.info(tr("on_server_crash"))
    else:
        server.logger.info(tr("on_server_stop"))

def on_info(server: PluginServerInterface, info: Info):
    '''
    参考[标准信息](https://docs.mcdreforged.com/zh-cn/latest/plugin_dev/event.html#general-info)
    '''
    pass

def on_user_info(server: PluginServerInterface, info: Info):
    '''
    参考[用户信息](https://docs.mcdreforged.com/zh-cn/latest/plugin_dev/event.html#user-info)
    '''
    if info.content == 'test':
        server.reply(info, tr("reply_test"))

def on_player_joined(server: PluginServerInterface, player: str, info: Info):
    '''
    参考[玩家加入](https://docs.mcdreforged.com/zh-cn/latest/plugin_dev/event.html#player-joined)
    '''
    server.logger.info(tr("on_player_joined").replace('%player%', player).replace('%info_content%', info.content))

def on_player_left(server: PluginServerInterface, player: str):
    '''
    参考[玩家离开](https://docs.mcdreforged.com/zh-cn/latest/plugin_dev/event.html#player-left)
    '''
    server.logger.info(tr("on_player_left").replace('%player%', player))

def on_unload(server: PluginServerInterface):
    '''
    参考[插件被卸载](https://docs.mcdreforged.com/zh-cn/latest/plugin_dev/event.html#plugin-unloaded)
    '''
    server.logger.info(tr("on_unload"))