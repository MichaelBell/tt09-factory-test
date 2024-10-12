import os
import volare
import openlane.common.misc
PDK_VERSION = openlane.common.misc.get_opdks_rev()

if "PDK_ROOT" in os.environ:
    volare.enable(
        os.environ["PDK_ROOT"],
        {"sky130A": "sky130"}[os.environ["PDK"]],
        PDK_VERSION,
        include_libraries=["sky130_fd_sc_hs",]
    )
