# Generating ASCII art from an image
the main purpose of this repository is to get familiar with Docker. This is a simple Docker app that generates ascii art from an input image and prints it out to the terminal

# Usage
- you can pull the Docker image from docker hub by running the following command:

``` docker pull abdaloth/hello-docker:latest ```

- you can then run this command to generate the ascii art:

 ```docker run -it abdaloth/hello-docker python app.py --path sample.png```

- the following command line options exist if you'd like to change how the output looks

```Options:
  --path TEXT         path to the image file. (user will be prompted for this if not entered as an argument)
  --cols INTEGER      width of the ascii art. (120 by default)
  --font_scale FLOAT  the most appropriate scale for your terminal font. (0.43 by default)
```
