To set-up jupyter ipython kernel to match your environment's default python follow these instructions:

Go to this path: /usr/share/jupyter/kernels/python3

Open the kernel.json file and change the first string of argv to "/usr/bin/env python3"

What this will do is take the environmentally selected python from where python is run from
hence making it dynamic rather than static

After that close and save, and restart VSCode and kernel should work properly