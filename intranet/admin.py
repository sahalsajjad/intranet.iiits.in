from django.contrib import admin

from intranet import models as intranet_models
from django.utils.translation import ugettext_lazy


admin.site.site_title 	= ugettext_lazy('Intranet Super Admin')
admin.site.site_header 	= ugettext_lazy('Intranet Classified Administration')
admin.site.index_title 	= ugettext_lazy('Intranet High Security Zone')


admin.site.register(intranet_models.Post)
admin.site.register(intranet_models.Notice)
admin.site.register(intranet_models.News)
admin.site.register(intranet_models.Resource)
admin.site.register(intranet_models.Application)
admin.site.register(intranet_models.Comment)
admin.site.register(intranet_models.Suggestion)
admin.site.register(intranet_models.Link)
admin.site.register(intranet_models.LeftLink)
admin.site.register(intranet_models.Section)
admin.site.register(intranet_models.Tag)
