__requires__ = ['click']
import click

def optional(*decls, nilstr=False, **attrs):
    """
    Like `click.option`, but no value (not even `None`) is passed to the
    command callback if the user doesn't use the option.  If ``nilstr`` is
    true, ``--opt ""`` will be converted to either `None` or (if ``multiple``)
    ``()``.
    """
    def callback(ctx, param, value):
        if attrs.get('multiple'):
            if nilstr and value == ('',):
                ctx.params[param.name] = ()
            elif value != ():
                ctx.params[param.name] = value
        else:
            if nilstr and value == '':
                ctx.params[param.name] = None
            elif value is not None:
                ctx.params[param.name] = value
    if not attrs.get('multiple'):
        attrs['default'] = None
    return click.option(*decls, callback=callback, expose_value=False, **attrs)
