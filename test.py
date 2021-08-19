import httpimport

url = "https://raw.githubusercontent.com/SCPlusNTU/CalibrationTest/main/lib.py?token=AFN2Q6GDISMZJS7WZ33O7T3BDXD4M"
with httpimport.remote_repo(["FixTemperature_MAPS"], url):
    import lib

lib.FixTemperature_MAPS()

from httpimport import github_repo

with github_repo( 'CalibrationTest', 'calibration', ):
    import lib


with httpimport.github_repo('operatorequals', 'covertutils', branch = 'master'):
    import covertutils
# Also works with 'bitbucket_repo' and 'gitlab_repo'


from calibration import *