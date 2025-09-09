# Fundamentals of Programming 2025
Berry Boessenkool;
2025-09-09, 21:50

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
