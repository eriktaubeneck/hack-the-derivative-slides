# Hack the Derivative

This is the source of a presentation given for PyData 2015. The generated slides are available [here](http://slides.skien.cc/hack-the-derivative-pydata.pdf).


The functions used in this presentation are also on GitHub [here](https://github.com/eriktaubeneck/hack-the-derivative) and can be installed with `pip install hackthederivative`.

## Build

To build the slides yourself, you will need LaTeX installed. You can then build with

```
pdflatex hack-the-derivative.tex
```

If you'd like this to automatically build upon saves to the `.tex` files, you can use Watchdog. Assuming you have this installed (`pip install watchdog`), simply run

```
watchmedo tricks-from pdflatex-trick.yaml
```
