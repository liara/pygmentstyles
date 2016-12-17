# -*- coding: utf-8 -*-
"""
    Behelit Colorscheme
    ~~~~~~~~~~~~~~~~~~~

    Converted by Vim Colorscheme Converter
"""
from pygments.style import Style
from pygments.token import Token, String, Name, Number, Keyword, Generic, Comment, Operator

class BehelitStyle(Style):

    background_color = '#101010'
    styles = {
        Token:              'noinherit #5fff5f',
        Name.Constant:      'noinherit #af87ff',
        String:             'noinherit #ffff87',
        Keyword:            'noinherit #d7005f bold',
        Keyword.Type:       'noinherit #5f87d7',
        Generic.Emph:       'underline',
        Number:             'noinherit #af87ff',
        Comment.Preproc:    '#87ff5f bold',
        Generic.Heading:    'noinherit #af87ff',
        Name.Entity:        'noinherit #ff5f5f',
        Name.Tag:           'noinherit #d7005f bold',
        Name.Variable:      'noinherit #5f87d7',
        Generic.Subheading: 'noinherit #af87ff',
        Generic.Inserted:   'noinherit #101010',
        Comment:            'noinherit #585858',
        Generic.Traceback:  '#d7005f bold',
        Name.Function:      'noinherit #af87ff bold',
        Name.Attribute:     'noinherit #af87ff bold',
        Generic.Error:      '#d7005f bold',
        Generic.Deleted:    'noinherit #101010 bg:#d7005f',
        Generic.Output:     'noinherit #444444 bg:#101010',
    }
