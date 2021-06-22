from django.forms import ModelForm
from producto.models import Producto
from django.utils.translation import gettext_lazy as _

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'description', 'precio')
        labels = {
            'nombre': _('Nombre'),
            'description': _('Descripcion'),
            'precio': _('Precio'),
        }
        help_texts = {
            'nombre': _('Nombre del producto y modelo.'),
            'description': _('Una descripcion detallada de no mas de 252 caracteres'),
            'precio': _('Favor no exageres tu precio'),
        }
        error_messages = {
            'nombre': {
                'max_length': _("nombre demasiado largo!!."),
            },
            'description': {
                'max_length': _("descripcion demasiada largo!!."),
            },
            'precio': {
                'max_length': _("precio demasiado largo!!."),
            }
        }
       
    
