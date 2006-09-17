from django.conf.urls.defaults import *
from django.conf import settings
from oj.problem.models import Problem
from oj.judge.models import Judge
from oj.volume.models import ProblemVolume
from django.contrib.auth.models import User

urlpatterns = patterns('',
    # Example:

    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}),

    (r'^problem/', include('oj.problem.urls')),

    (r'^volume/', include('oj.volume.urls')),

    (r'^users/', include('oj.userprofile.urls')),

    (r'^judge/', include('oj.judge.urls')),

    (r'^images/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.STATIC_PATH}),

    (r'^admin/', include('django.contrib.admin.urls')),
)
