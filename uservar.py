import xbmcaddon
addon_id = xbmcaddon.Addon().getAddonInfo('id')

'''#####-----Build File-----#####'''
buildfile = 'https://tveecf.github.io/program/text/builds.xml'

'''#####-----Notifications-----#####'''
notify_url  = 'https://tveecf.github.io/program/text/notify.txt'

'''#####-----Excludes-----#####'''
excludes  = [addon_id, 'packages', 'Addons33.db', 'kodi.log', 'script.module.certifi', 'script.module.chardet', 'script.module.idna', 'script.module.requests', 'script.module.urllib3', 'backups',']
