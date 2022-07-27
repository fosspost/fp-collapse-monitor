from setuptools import setup

data_files = [ ("/usr/share/fp-collapse-monitor", ["ui/ui.glade"]),
                    ("/usr/share/pixmaps", ["data/fp-collapse-monitor.png"]),
                     ("/usr/share/applications", ["data/fp-collapse-monitor.desktop"]) ] 
                     
setup(name = "fp-collapse-monitor",
      version = "1.0",
      description = "Simple out-of-the-box browser for collapse maps worldwide.",
      author = "Muhammed Hanny Sabbagh", 
      author_email = "email@mhsabbagh.com",
      url = "https://github.com/fosspost/fp-collapse-monitor",
      license='GPLv3',
      py_modules=[],
      scripts=['fp-collapse-monitor'],
      data_files=data_files)

