from setuptools import setup

data_files = [ ("/usr/share/fp-collapse-monitor", ["ui.glade"]),
                    ("/usr/share/pixmaps", ["fp-collapse-monitor.png"]),
                     ("/usr/share/applications", ["fp-collapse-monitor.desktop"]) ] 
                     
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

