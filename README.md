# Terminal Input Test

Testing code and showcase for PyCharm terminal emulation
issue at https://youtrack.jetbrains.com/issue/PY-59857/Debug-Terminal-Emulator-Input



## Details
The library used for the key reading is https://github.com/magmax/python-readchar, but previously it
was also attempted with quite similar custom code, the library is very wide realistic to historical
needs and updated so there is no need to custom simulate it


The explanation for each scenario is explained inside the `1_emulate_terminal_in_out_console.py` and
in `2_run_with_python_console-py` with comments with the expected outcomes


## Setup
Clone the project with git
`git clone https://github.com/OriDevTeam/terminal-input-test.git`

To setup the environment and install packages with Poetry
`poetry install`

To setup just the single dependency globabally with Pip
`pip install readchar`



## Reproducing
To reproduce simply select the `1_emulate_terminal_in_output_console` configuration in Run or Debug


### Reproducing the setup (in case if IDEA configuration is missing)
If they are missing or you want to make sure they are as intended, select the `1_emulate_terminal_in_output_console.py` file and edit its configuration, and check the `Emulation > Emulate terminal in output console` box
![image](https://user-images.githubusercontent.com/15692866/229255124-969000a6-5967-484a-9311-6225ca01fa11.png)



## Showcase testing

### Trying out 'Emulation > Emulate terminal with output console'

#### Run (Working as intended)
https://user-images.githubusercontent.com/15692866/229252153-67c76e09-c812-4fa0-8500-0922c027fc06.mp4


#### Debug (Not working as intended, only returns after »ENTER«(newline) is hit)
https://user-images.githubusercontent.com/15692866/229252179-fbc70ba5-3bdf-4e08-b18f-bdf5ee815be2.mp4




### Trying out 'Emulation > Run with Python Console'

#### Run
https://user-images.githubusercontent.com/15692866/229252187-352fb499-2bd4-4593-ab38-fd5356476ccd.mp4


#### Debug
https://user-images.githubusercontent.com/15692866/229252248-352e743c-b776-47c8-a5bf-bf12c51dcd3a.mp4
