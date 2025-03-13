from . import *
from .plugin import *
from .rcon import *
from ..utils import *


def register_command(server: PluginServerInterface):
    builder.arg("var_name", Text)
    builder.arg("command", QuotableText)
    builder.command("!!debug plgSelf <var_name>", debug_plugin)
    builder.command("!!debug psi <var_name>", debug_mcdr)
    builder.command("!!debug rcon <command>", debug_rcon)
    builder.register(server)
    server.register_help_message("!!debug", help_message())

# 注册帮助消息时，需要直接使用RTextMCDRTranslation组件，此时需要将`tr()`中的可选参数`return_str`设置为False以避免翻译结果被转换为str
@builder.command("!!debug")
def show_help(src: CommandSource) -> RTextList:
    pfx = "on_command.help"
    src.reply(RTextList(
        tr(f"{pfx}_title", False) + "\n",
        tr(f"{pfx}_line1", False) + "\n",
        tr(f"{pfx}_line2", False) + "\n",
        tr(f"{pfx}_line3", False) + "\n"
    ))

def help_message():
    return tr("on_command.help_message", False)