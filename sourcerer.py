# -*- coding: utf-8 -*-
"""
    Sourcerer Colorscheme
    ~~~~~~~~~~~~~~~~~~~~~

    Converted by Vim Colorscheme Converter
"""
from pygments.style import Style
from pygments.token import Token, Keyword, Comment, Name, Number, Operator, Generic, String

class SourcererStyle(Style):

    background_color = '#222222'
    styles = {
        Token:              'noinherit #c2c2b0',
        Name.Attribute:     'noinherit #faf4c6',
        Comment.Preproc:    'noinherit #528b8b',
        Name.Variable:      'noinherit #9ebac2',
        Keyword:            'noinherit #90b0d1',
        Number:             'noinherit #cc8800',
        Keyword.Type:       'noinherit #7e8aa2',
        Comment:            'noinherit #686858 italic',
        Generic.Error:      'noinherit',
        Generic.Traceback:  '#ff6a6a bold',
        Generic.Subheading: '#528b8b bold',
        Name.Tag:           'noinherit #90b0d1',
        Generic.Inserted:   'noinherit #000000 bg:#3cb371',
        Generic.Output:     'noinherit #404050',
        Name.Entity:        'noinherit #719611',
        Name.Constant:      'noinherit #ff9800',
        Generic.Emph:       'underline',
        Generic.Heading:    '#528b8b bold',
        String:             'noinherit #779b70',
        Name.Function:      'noinherit #faf4c6',
        Generic.Deleted:    'noinherit #000000 bg:#aa4450',
    }
