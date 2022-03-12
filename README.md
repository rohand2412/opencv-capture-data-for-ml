# Python Data Scripts

This is a collection of data manipulation scripts for formatting and managing large sets of images and their corresponding labels. The scripts, written with ease of use in mind, are all accessible from the terminal and only require an input and output directory for images or labels depending on the script. For more information on any of the scripts, add the `--help` flag.

## Getting Started

The following instructions will get you completely set up:

1. This repository depends on `raspberry_pi_libraries`, install it [here](https://gitlab.com/rohand2412/raspberry_pi_libraries).

2. Clone this repository into the desired directory.

3. If you plan on running the Jupyter Notebooks follow the instructions below based on your platform.

## Unix

**Includes Linux and macOS, which are Unix-based.**

If your Jupyter Notebook is using the wrong python version follow these instructions:

1. Go to this directory: `/usr/share/jupyter/kernels/python3/`

2. Open the `kernel.json` file and change the first string of argv to `"/usr/bin/env python3"`

3. Close, save, and restart your IDE

Your `kernel.json` should look similar to this:

    {
     "argv": [
      "/usr/bin/env python3",
      "-m",
      "ipykernel_launcher",
      "-f",
      "{connection_file}"
     ],
     "display_name": "Python 3",
     "language": "python"
    }

Now the IPython kernel will call the environmentally selected python binary when you run a notebook instead of running the system wide selected python binary which was the incorrect python version that was previously selected.

## Windows

As long as your IPython kernel is functioning as intended, you are all set up.