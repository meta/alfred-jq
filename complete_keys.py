#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

from __future__ import print_function, unicode_literals, absolute_import

import sys
from workflow import Workflow, web, ICON_WARNING
import json

USER_AGENT = 'Alfred-JQ/{version} ({url})'


def main(wf):
    queries = wf.args
    q = queries[0].strip()
    error_code = queries[-1]
    if error_code != '0':
        wf.add_item('Invalid JSON String in clipboard.', 
                    valid=False,
                    icon='error.png')
        wf.send_feedback()
        return 0

    keys = queries[1:-1]
    url = None
    for k in keys:
        if q[-1] != '.':
            full_q = q + '.' + k
        else:
            full_q = q + k
        wf.add_item(k,
                    arg=full_q,
                    autocomplete=full_q,
                    valid=True,
                    icon='icon.png')
    wf.send_feedback()
    return 0
        
if __name__ == '__main__':
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
