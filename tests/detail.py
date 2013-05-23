#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import PostgreSQL

class Detail(PostgreSQL):
    clauses = dict(table='detail')
    arrange_by = ('person_id', 'key')
    squashed = arrange_by
    ident_by = ('detail_id', )

if __name__ == '__main__':

    from pprint import pprint

    print '# powerful arrange'
    for detail in Detail.arrange():
        print detail
    print

    print '# modified an email'

    mosky_detail = Detail.select(where={'person_id': 'mosky', 'key': 'email'})
    mosky_detail['val', 0] = 'this email is modified 1'
    mosky_detail['val', 0] = 'this email is modified 2'
    mosky_detail['val', 0] = 'this email is modified'
    mosky_detail.save()

    mosky_detail = Detail.select(where={'person_id': 'mosky', 'key': 'email'})
    print mosky_detail['val']
    print mosky_detail['val', 0]
    print
