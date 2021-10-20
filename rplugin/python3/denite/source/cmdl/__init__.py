"""
cmdl
"""

import os
import sys

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
)

import cmdl.util as cl
from denite.source.base import Base

CMDL_HIGHLIGHT_SYNTAX = [
    {'name': 'Denite_Cmdl_Name', 'link': 'Identifier', 're': r'[^:]\+:\s'},
]

class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'cmdl'
        self.kind = 'cmdl'

    def highlight(self):
        for s in CMDL_HIGHLIGHT_SYNTAX:
            self.vim.command(
                'syntax match {0}_{1} /{2}/ contained containedin={0}'.format(
                    self.syntax_name, s['name'], s['re']
                )
            )
            self.vim.command(
                'highlight default link {0}_{1} {2}'.format(
                    self.syntax_name, s['name'], s['link']
                )
            )

    def gather_candidates(self, context):
        try:
            cmdl_dict = cl.read(self.vim)
        except FileNotFoundError:
            return []

        if not cmdl_dict:
            return []

        return [
            {
                'word': f"{v['name']}: {v['to_execute']}",
                'action__name': v['name'],
                'action__to_execute': v['to_execute'],
            }
            for v in cmdl_dict['cmdls']
        ]

def main():
    pass

if __name__ == '__main__':
    main()
