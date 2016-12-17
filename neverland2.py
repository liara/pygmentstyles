# -*- coding: utf-8 -*-
"""
    Neverland2 Colorscheme
    ~~~~~~~~~~~~~~~~~~~~~~

    Converted by Vim Colorscheme Converter
"""
from pygments.style import Style
from pygments.token import Token, Keyword, Comment, Number, Generic, Operator, Name, String

class Neverland2Style(Style):

    background_color = '#121212'
    styles = {
        Token:              '#ffffff',
        Name.Function:      '#ff005f',
        Operator.Word:      '#00ff00',
        Name.Label:         'noinherit #ffffaf',
        Generic.Subheading: '#0000ff',
        Generic.Traceback:  '#ff00af bg:#121212 bold',
        Generic.Error:      '#ffafff bg:#121212',
        Comment:            '#87875f',
        Name.Attribute:     '#ff005f',
        Name.Constant:      '#af5fff bold',
        Number.Float:       '#af5fff',
        Generic.Inserted:   'bg:#121212',
        Keyword.Type:       'noinherit #5fd7ff',
        String:             '#d7af5f',
        Generic.Deleted:    '#d70087 bg:#080808',
        Comment.Preproc:    '#ffafd7',
        Keyword:            '#ffff87 bold',
        Name.Exception:     '#87ff00 bold',
        Name.Variable:      '#d75f00',
        Generic.Heading:    '#0000ff',
        Name.Tag:           '#ffff87 bold',
        Number:             '#0087ff',
        Generic.Output:     '#121212 bg:#121212',
        Name.Entity:        '#5fd7ff bg:#080808',
        Generic.Emph:       '#808080 underline',
    }
