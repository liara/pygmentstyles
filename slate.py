# -*- coding: utf-8 -*-
"""
    Slate Colorscheme
    ~~~~~~~~~~~~~~~~~

    Converted by Vim Colorscheme Converter
"""
from pygments.style import Style
from pygments.token import Token, Keyword, String, Name, Number, Generic, Operator, Comment

class SlateStyle(Style):

    background_color = '#19191f'
    styles = {
        Token:              'noinherit #ebebf4',
        Keyword:            '#89A7B1',
        Number.Float:       '#9eb2d9 bg:#c00000',
        Generic.Inserted:   'noinherit bg:#446688',
        Name.Function:      '#89A7B1',
        Name.Exception:     '#89A7B1',
        Name.Constant:      '#ffffff bg:#808080',
        Generic.Emph:       '#99ccff underline',
        Generic.Heading:    '#ebebf4 bg:#c00000',
        Operator.Word:      '#566981 bg:#008080',
        Name.Variable:      '#ebebf4',
        Generic.Error:      '#ffffff bg:#ff0000',
        Generic.Deleted:    'noinherit bg:#884444',
        String:             '#9eb2d9',
        Generic.Output:     '#ebebf4 bg:#808080',
        Name.Entity:        '#bbddff bg:#c00000',
        Generic.Traceback:  '#ff0000',
        Name.Label:         '#ffccff',
        Generic.Subheading: '#ebebf4 bg:#c00000',
        Name.Attribute:     '#89A7B1',
        Comment.Preproc:    '#ffcc99 bg:#0000c0',
        Number:             '#9eb2d9',
        Keyword.Type:       '#566981',
        Comment:            'noinherit #515166 bg:#808080',
        Name.Tag:           '#89A7B1',
    }
