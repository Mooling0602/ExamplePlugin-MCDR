from ..utils import *


def debug_rcon(src: CommandSource, ctx: CommandContext):
    src.reply(psi.rcon_query(ctx["command"]))