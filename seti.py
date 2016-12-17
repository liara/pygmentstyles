# -*- coding: utf-8 -*-
"""
    Seti Colorscheme
    ~~~~~~~~~~~~~~~~

    Converted by Vim Colorscheme Converter
"""
from pygments.style import Style
from pygments.token import Token, String, Comment, Operator, Number, Name, Generic, Keyword

class SetiStyle(Style):

    background_color = '#151718'
    styles = {
        Token:              'noinherit #d4d7d6',
        Name.Function:      'noinherit #55b5db',
        Generic.Output:     'noinherit #2b2e28 bg:#1f2122',
        Keyword:            'noinherit #9fca56',
        Generic.Emph:       'underline',
        Number:             'noinherit #cd3f45',
        String:             'noinherit #55b5db',
        Name.Tag:           'noinherit #9fca56',
        Generic.Heading:    '#d4d7d6 bold',
        Name.Label:         'noinherit #55b5db',
        Name.Variable:      'noinherit #e6cd69',
        Generic.Traceback:  'noinherit #f8f8f8',
        Generic.Subheading: '#d4d7d6 bold',
        Comment.Preproc:    'noinherit #ff026a',
        Name.Attribute:     'noinherit #55b5db',
        Generic.Deleted:    'noinherit #870505',
        Name.Entity:        'noinherit #d4d7d6',
        Number.Float:       'noinherit #cd3f45',
        Comment:            'noinherit #41535b',
        Name.Constant:      'noinherit #cd3f45',
        Generic.Inserted:   '#d4d7d6 bg:#43800a bold',
        Operator.Word:      'noinherit #9fca56',
        Keyword.Type:       'noinherit #55b5db',
    }
