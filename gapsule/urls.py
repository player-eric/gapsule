import tornado.web
import os

from gapsule.handlers.Main import MainHandler
from gapsule.handlers.Forums import ForumHandler
from gapsule.handlers.User import Signin, Signup
from gapsule.handlers.GitHTTP import GitHTTPHandler, GIT_URL_PATTERNS_REGEX
from gapsule.settings import settings
from gapsule.handlers.Repo import (CodeListHandler, FolderListHandler,
                                   FileContentHandler,)

routes = [
    (r"/", MainHandler),
    (r"/signin/?", Signin.SignInHandler),
    (r"/signup(/verify|/finishing)?/?", Signup.SignUpHandler),
    (r"/(?P<owner>\w+)/(?P<reponame>\w+)/issues/(?P<postid>\d+)", ForumHandler),
    (r"/static/(.*)", tornado.web.StaticFileHandler, {
        'path': settings['static_path']
    }),
    (r"/(\w+)/(\w+)(?:.git)?(" + GIT_URL_PATTERNS_REGEX + ")", GitHTTPHandler),
    (r"/(?P<username>\w+)/(?P<projectname>\w+)/?", CodeListHandler),
    (r"/(?P<username>\w+)/(?P<projectname>\w+)/tree/(?P<branch>\w+)/(?P<restpath>.*)/?", FolderListHandler),
    (r"/(?P<username>\w+)/(?P<projectname>\w+)/blob/(?P<branch>\w+)/(?P<restpath>.*)/?",
     FileContentHandler),
    (r"/.*", MainHandler),
]
