from django import template
import locale
register = template.Library()
@register.filter()
def format_price(val):
    locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
    val = locale.format_string("%d", val, grouping=True)
    return val