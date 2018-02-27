from django.contrib import admin
from askstories.models import Askstories
from jobstories.models import Jobstories
from newstories.models import Newstories
from showstories.models import Showstories

admin.site.register(Askstories)
admin.site.register(Jobstories)
admin.site.register(Newstories)
admin.site.register(Showstories)
