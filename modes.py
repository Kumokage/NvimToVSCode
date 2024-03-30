from enum import Enum

class Modes(Enum):
    N = "vim.normalModeKeyBindings"
    V = "vim.visualModeKeyBindings"
    I = "vim.insertModeKeyBindings"
    C = "vim.commandLineModeKeyBindings"
