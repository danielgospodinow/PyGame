import cx_Freeze

executables = [cx_Freeze.Executable("snake_main.py")]

cx_Freeze.setup(
    name="Dancho's Sname Game",
    options={"build_exe": {"packages": ["pygame"], "include_files": ["apple_sprite_01.png",
                                                                     "danchoIcon.jpg",
                                                                     "snake_tail_01.png",
                                                                     "snakehead01.png"]}},
    description="Dancho's first pygame!",
    executables=executables
)