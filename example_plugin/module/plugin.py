from ..utils import *


def debug_plugin(src: CommandSource, ctx: CommandContext):
    pfx = "on_command.on_ltr_plgself"
    var_name = ctx["var_name"]
    value = globals().get(var_name)
    if value is not None:
        value = str(value)
        src.reply(tr(f"{pfx}.success").replace("%var_name%", var_name).replace("%value%", value))
    else:
        src.reply(tr(f"{pfx}.failed").replace("%var_name%", var_name))

def debug_mcdr(src: CommandSource, ctx: CommandContext):
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