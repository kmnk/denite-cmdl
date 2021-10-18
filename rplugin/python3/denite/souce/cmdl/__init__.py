"""
cmdlauncher
"""

import os
import sys

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
)

import cmdlauncher.util as cl
from denite.source.base import Base

CMDLAUNCHER_HIGHLIGHT_SYNTAX = [
    {'name': 'Denite_Cmdlauncher_Name', 'link': 'Statement', 're': r'\[.*\]\ze\s'}
]


class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'cmdlauncher'
        self.kind = 'cmdlauncher'

    def highlight(self):
        for syn in CMDLAUNCHER_HIGHLIGHT_SYNTAX:
            self.vim.command(
                'syntax match {0}_{1} /{2}/ contained containedin={0}'.format(
                    self.syntax_name, syn['name'], syn['re']
                )
            )
            self.vim.command(
                'highlight default link {0}_{1} {2}'.format(
                    self.syntax_name, syn['name'], syn['link']
                )
            )

    def gather_candidates(self, context):
        # TODO: get by comma separated group names
        group = (
            context['args'][0]
            if len(context['args']) >= 1
            else cl.get_default_group(self.vim)
        )

        if not group or group == '':
            raise ValueError('group value is invalid:{}'.format(group))

        try:
            cmdlauncher_dict = cl.read(self.vim)
        except FileNotFoundError:
            return []

        group_dict = cmdlauncher_dict['group'].get(group, None)

        if not group_dict:
            return []

        return [
            {
                'word': f"[{v['name']}] {v['path']}",
                'action__name': v['name'],
                'action__group': group,
                'action__path': v['path'],
            }
            for v in group_dict['cmdlaunchers']
        ]


def main():
    pass


if __name__ == '__main__':
    main()
