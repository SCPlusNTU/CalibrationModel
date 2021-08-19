import httpimport

url = "https://raw.githubusercontent.com/SCPlusNTU/CalibrationTest/main/lib.py?token=AFN2Q6GDISMZJS7WZ33O7T3BDXD4M"
with httpimport.remote_repo(["FixTemperature_MAPS"], url):
    import lib

lib.FixTemperature_MAPS()

from httpimport import github_repo

with github_repo( 'CalibrationTest', 'lib', ):
    import lib
