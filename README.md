# Some additional pygments

Generated with [vim2pygments](https://github.com/honza/vim2pygments).

```
$ python vimpygments.py codeschool.vim > codeschool.py
```

### Usage

Yeah I know it's not the correct way, but o.O

Put the style in

```
/usr/lib/pythonx.y/site-packages/pygments/styles
```
and add it to `__init__.py` in the same directory
```
'codeschool': 'codeschool::CodeschoolStyle',
```
