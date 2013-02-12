#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SQL(dict):

    @classmethod
    def insert(cls, table):
        sql = cls(
            ('insert into', '<table>'),
            ('<columns>', ),
            ('values', '<values>')
        )
        return sql

    @classmethod
    def select(cls, *fields):
        sql = cls(
            ('select', '<select>'),
            ('from', '<table>'),
            ('where', '<where>'),
            ('order by', '<order_by>'),
            ('<asc>', ),
            ('<desc>', ),
            ('limit', '<limit>'),
            ('offset', '<offset>')
        )
        return sql

    @classmethod
    def update(cls, table):
        sql = cls(
            ('update', '<table>'),
            ('set', '<set>'),
            ('where', '<where>')
        )
        return sql

    @classmethod
    def delete(cls, table):
        sql = cls(
            ('delete from', '<table>'),
            ('where', '<where>')
        )
        return sql

    def __init__(self, *template_groups):
        self.template_groups = template_groups

    def __str__(self):
        pass

if __name__ == '__main__':
    pass
