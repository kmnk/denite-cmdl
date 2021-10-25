"""
denite.nvim kind: cmdl
"""

from denite.kind.base import Base

import cmdl.util as cl

class Kind(Base):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'cmdl'
        self.default_action = 'execute'

    def action_execute(self, context):
        target = context['targets'][0]
        name = target['action__name']
        to_execute = target['action__to_execute']

        self.vim.command(to_execute)

def main(): pass

if __name__ == '__main__': main()
