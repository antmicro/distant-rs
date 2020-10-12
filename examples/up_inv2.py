from distantrs import Invocation
from pathlib import Path

i = Invocation()
i.open()
i.announce_target("funky_town")
i.update_status(5)
i.send_file('build.log', "{}/build.log".format(str(Path.home())))
i.close()

print(f"https://source.cloud.google.com/results/invocations/{i.invocation_id}")
