# -*- coding: utf-8 -*-
"""
    Xyloh Colorscheme
    ~~~~~~~~~~~~~~~~~

    Converted by Vim Colorscheme Converter
"""
from pygments.style import Style
from pygments.token import Token, Number, Keyword, Generic, Comment, String, Operator, Name

class XylohStyle(Style):

    background_color = '#383a3b'
    styles = {
        Token:              '#d8dabc',
        Number.Float:       '#cc4166',
        Name.Constant:      '#ffff99 underline',
        Name.Attribute:     '#ccbe41 bold',
        Comment.Preproc:    '#78cc41 underline',
        Generic.Error:      '#d8dabc bg:#cc4166',
        Name.Variable:      '#99c2ff underline',
        Name.Label:         '#ffb964 underline',
        Keyword.Type:       '#415dcc bold underline',
        Number:             '#cc4166',
        Comment:            '#888888 bold',
        String:             '#ccff99',
        Name.Exception:     '#a241cc',
        Name.Function:      '#ccbe41 bold',
        Keyword:            '#ff99cc bold',
        Name.Tag:           '#ff99cc bold',
        Generic.Output:     '#888888',
        Operator.Word:      '#99ffcc',
        Name.Entity:        '#c299ff bold',
    }
