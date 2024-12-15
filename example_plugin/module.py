# 将不适合塞进入口点的方法独立出一个模块出来进行管理，可以分多个模块
# 模块中的方法最终需要直接或间接的在入口点被使用，`from .module import <func_name>` 即可。
# 下面对使用[简易命令构建器](https://docs.mcdreforged.com/zh-cn/latest/plugin_dev/command.html#simple-command-builder)进行示例，命令的注册需在此模块中完成，并在入口点导入，入口点不能直接注册命令
from .utils import *

def register_command(server: PluginServerInterface):
    builder.arg("var_name", Text)
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

@builder.command("!!debug plgSelf <var_name>")
def debug_plugin(src: CommandSource, ctx: CommandContext):
    pfx = "on_command.on_ltr_plgself"
    var_name = ctx["var_name"]
    value = globals().get(var_name)
    if value is not None:
        value = str(value)
        src.reply(tr(f"{pfx}.success").replace("%var_name%", var_name).replace("%value%", value))
    else:
        src.reply(tr(f"{pfx}.failed").replace("%var_name%", var_name))

@builder.command("!!debug si <var_name>")
def debug_plugin(src: CommandSource, ctx: CommandContext):
    pfx = "on_command.on_ltr_si"
    var_name = ctx["var_name"]
    value = getattr(psi, var_name, None)
    try:
        if value is not None:
            src.reply(tr(f"{pfx}.success").replace("%var_name%", var_name).replace("%value%", value))
        else:
            src.reply(tr(f"{pfx}.failed").replace("%var_name%", var_name))
    except TypeError:
        if callable(value):
            result = value()
            if result is not None:
                if isinstance(result, str):
                    src.reply(tr(f"{pfx}.success").replace("%var_name%", var_name).replace("%value%", result))
                elif isinstance(result, bool):
                    if result is True:
                        src.reply(tr(f"{pfx}.success").replace("%var_name%", var_name).replace("%value%", "True"))
                    else:
                        src.reply(tr(f"{pfx}.success").replace("%var_name%", var_name).replace("%value%", "False"))
                else:
                    if isinstance(str(result), str):
                        src.reply(tr(f"{pfx}.success").replace("%var_name%", var_name).replace("%value%", str(result)))
                    else:
                        src.reply(tr(f"{pfx}.failed").replace("%var_name%", var_name))
            else:
                src.reply(tr(f"{pfx}.failed").replace("%var_name%", var_name))
        else:
            src.reply(tr(f"{pfx}.failed").replace("%var_name%", var_name))
