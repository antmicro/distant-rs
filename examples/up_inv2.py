from distantrs import Invocation
from pathlib import Path

example_log = "{}/build.log".format(str(Path.home())) 

i = Invocation()
i.open()
i.announce_target("funky_town")
i.send_file_target("funky_town", "test.log", example_log)
i.send_file_target("funky_town", "test2.log", example_log)
i.finalize_target("funky_town", 0)
i.announce_target("cool_target")
i.finalize_target("cool_target", 1)
i.update_status(5)
i.send_file('build.log', example_log)
i.close()

print(i.targets)
print(f"https://source.cloud.google.com/results/invocations/{i.invocation_id}")
