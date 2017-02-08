# -*- coding: utf-8 -*-
"""
    pygments.styles.mukluk
    ~~~~~~~~~~~~~~~~~~~~~~~

    Mukluk because they are boots with flat soles (and it is a fun word to say).
    Ported from http://phaedryx.github.io/2015/03/01/mukluk-a-dark-theme-for-pygments/
    Based on bootflat color scheme https://bootflat.github.io/documentation.html.

    by liara
"""

from pygments.style import Style
from pygments.token import (Keyword, Name, Comment, String, Error, Text,
                            Number, Operator, Generic, Whitespace, Punctuation,
                            Other, Literal)


class MuklukStyle(Style):
    """
    This style mimics bootflat color scheme.
    """

    background_color = "#434A54"  # 272822
    highlight_color = "#CCD1D9"  # 49483e

    styles = {
        # No corresponding class for the following:
        Text:                      "#F5F7FA",  # class:  '' #f8f8f2
        Whitespace:                "",         # class: 'w'
        Error:                     "#ED5565",  # class: 'err'
        Other:                     "",         # class 'x'

        Comment:                   "#CCD1D9 italic",  # class: 'c'
        Comment.Multiline:         "#656D78 italic",  # class: 'cm'
        Comment.Preproc:           "#656D78 italic",  # class: 'cp'
        Comment.Single:            "#656D78 italic",  # class: 'c1'
        Comment.Special:           "#656D78 italic bold",  # class: 'cs'

        Keyword:                   "#FC6E51",  # class: 'k'
        Keyword.Constant:          "#FFCE54",  # class: 'kc'
        Keyword.Declaration:       "#FFCE54",  # class: 'kd'
        Keyword.Namespace:         "",  # class: 'kn'
        Keyword.Pseudo:            "#FFCE54",  # class: 'kp'
        Keyword.Reserved:          "#FFCE54",  # class: 'kr'
        Keyword.Type:              "#5D9CEC",  # class: 'kt'

        Operator:                  "#F5F7FA",  # class: 'o'
        Operator.Word:             "bold",     # class: 'ow' - like keywords

        Punctuation:               "#F5F7FA",  # class: 'p' #f8f8f2

        Name:                      "#F5F7FA",  # class: 'n'
        Name.Attribute:            "#4FC1E9",  # class: 'na' - to be revised
        Name.Builtin:              "#48CFAD",  # class: 'nb'
        Name.Builtin.Pseudo:       "#CCD1D9",  # class: 'bp'
        Name.Class:                "#ED5565",  # class: 'nc' - to be revised
        Name.Constant:             "#ED5565",  # class: 'no' - to be revised
        Name.Decorator:            "",  # class: 'nd' - to be revised
        Name.Entity:               "#ED5565",  # class: 'ni'
        Name.Exception:            "#F5F7FA",  # class: 'ne'
        Name.Function:             "#FFCE54",  # class: 'nf'
        Name.Property:             "",        # class: 'py'
        Name.Label:                "",        # class: 'nl'
        Name.Namespace:            "#CCD1D9",  # class: 'nn' - to be revised
        Name.Other:                "#ED5565",  # class: 'nx'
        Name.Tag:                  "#5D9CEC",  # class: 'nt' - like a keyword
        Name.Variable:             "#4FC1E9",  # class: 'nv' - to be revised
        Name.Variable.Class:       "#ED5565",  # class: 'vc' - to be revised
        Name.Variable.Global:      "#ED5565",  # class: 'vg' - to be revised
        Name.Variable.Instance:    "#4FC1E9",  # class: 'vi' - to be revised

        Number:                    "#ED5565",  # class: 'm'
        Number.Float:              "#5D9CEC",  # class: 'mf'
        Number.Hex:                "#5D9CEC",  # class: 'mh'
        Number.Integer:            "#5D9CEC",  # class: 'mi'
        Number.Integer.Long:       "#5D9CEC",  # class: 'il'
        Number.Oct:                "#5D9CEC",  # class: 'mo'

        Literal:                   "#ED5565",  # class: 'l'
        Literal.Date:              "",  # class: 'ld'

        String:                    "#A0D468",  # class: 's'
        String.Backtick:           "#A0D468",  # class: 'sb'
        String.Char:               "#A0D468",  # class: 'sc'
        String.Doc:                "#A0D468",  # class: 'sd' - like a comment
        String.Double:             "#A0D468",  # class: 's2'
        String.Escape:             "#A0D468",  # class: 'se'
        String.Heredoc:            "#A0D468",  # class: 'sh'
        String.Interpol:           "#A0D468",  # class: 'si'
        String.Other:              "#A0D468",  # class: 'sx'
        String.Regex:              "#EC87C0",  # class: 'sr'
        String.Single:             "#A0D468",  # class: 's1'
        String.Symbol:             "#AC92EC",  # class: 'ss'

        Generic:                   "",        # class: 'g'
        Generic.Deleted:           "bg:#CCD1D9 #656D78",  # class: 'gd',
        Generic.Emph:              "italic",  # class: 'ge'
        Generic.Error:             "#AC92EC",  # class: 'gr'
        Generic.Heading:           "#656D78",  # class: 'gh'
        Generic.Inserted:          "bg:#CCD1D9 #434A54",  # class: 'gi'
        Generic.Output:            "#656D78",  # class: 'go'
        Generic.Prompt:            "#656D78",  # class: 'gp'
        Generic.Strong:            "bold",     # class: 'gs'
        Generic.Subheading:        "#F5F7FA",  # class: 'gu'
        Generic.Traceback:         "#ED5565",  # class: 'gt'
    }
