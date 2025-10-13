# Fundamentals of Programming 2025
Berry Boessenkool;
2025-10-13, 19:12

This is a github task in the course
[FP25](https://open.hpi.de/courses/hpi-dh-fprog2025).  

## Get weather data

``` r
if(!requireNamespace("rdwd", quietly=TRUE))
    install.packages("rdwd")
rdwd::updateRdwd()
```

    rdwd is up to date, compared to github.com/brry/rdwd. Version 1.9.3 (2025-08-18)

download recent weather data using
[rdwd](https://bookdown.org/brry/rdwd/)

``` r
library(rdwd)
link <- selectDWD("Potsdam", res="daily", var="kl", per="recent")
clim <- dataDWD(link, varnames=TRUE, force=24)
```

## visualise recent temperature

``` r
plotDWD(clim, "TMK.Lufttemperatur")
```

![](README_files/figure-commonmark/plot_clim-1.png)

## transfer to Python

I use Python via the R package reticulate. All chill on Windows; On Mac,
I needed a manual install:

``` r
install.packages("reticulate")
# check first:
reticulate::py_config()
reticulate::py_available(TRUE)
# potentially do the edit_r_environ below if you have a working Python path

# install Python if needed
reticulate::install_miniconda() # then do the tos thing in the terminal, then:
reticulate::install_miniconda(force=TRUE)
reticulate::use_miniconda(condaenv="r-reticulate", required=TRUE)
reticulate::py_config()
# Make Python choice permanent (normally happens automatically in the background):
usethis::edit_r_environ() # RETICULATE_PYTHON=~/Library/r-miniconda/envs/r-reticulate/bin/python

# Restart Rstudio, check if calling python works:
reticulate::py_available()
reticulate::py_eval("1+1")
reticulate::py_numpy_available(TRUE)
reticulate::py_numpy_available()

reticulate::py_install(c("numpy", "pandas", "matplotlib"))
```

Back to the actual code:

``` python
clim_py = r.clim
import matplotlib
print(f"Dataset shape: {clim_py.shape[0]} rows, {clim_py.shape[1]} columns")
```

``` python
clim_py = clim_py.select_dtypes(include=['float64', 'int64'])
clim_py.hist(figsize=(12, 8), bins=20)
```

![](README_files/figure-commonmark/histograms-1.png)
