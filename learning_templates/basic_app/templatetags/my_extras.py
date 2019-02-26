from django import template

register = template.Library()

@register.filter(name='cut')

def cut(self,arg):
    """
      this cut out all values of arg  from the string
    """
    return self.replace(arg,'')

#register.filter('cut',cut)
