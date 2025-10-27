# Fundamentals of Programming October 2025
Berry Boessenkool
2025-10-27, 14:54

Hey everyone! Welcome to Fundamentals of Programming 2025/26!  
This is a github task in the course
[FP25](https://open.hpi.de/courses/hpi-dh-fprog2025).

*note that it is fine to not really understand the code at this point -
we’ll get to that throughout the course :)*

Please go through the new [installation
guide](https://github.com/brry/fpsetup#software-installation-guide)
first!

Due to people not pulling before pushing, we’re losing several edits.
See
e.g. [here](https://github.githistory.xyz/brry/FP25/blob/main/README.qmd)
for a nicely animated version history (works for any file on github).

## **Get weather data**

``` r
if(!requireNamespace("rdwd", quietly=TRUE))
    install.packages("rdwd")
rdwd::updateRdwd()
```

download recent weather data using
[rdwd](https://bookdown.org/brry/rdwd/)

``` r
library(rdwd)

# Define a local directory
locdir <- "~/DWDdata"

# Create it if it doesn't exist
if (!dir.exists(locdir)) {
  dir.create(locdir, recursive = TRUE)
}
link <- selectDWD("Potsdam", res="daily", var="kl", per="recent")

clim <- dataDWD(link,dir = locdir, varnames=TRUE, force=24)
```

## Visualise Recent Temperature

``` r
plotDWD(clim, "TMK.Lufttemperatur", ylab = "mean air temperature (in °C)", col = "darkgreen")
```

![](README_files/figure-commonmark/plot_clim-1.png)

## Visualise recent Wind Speed

**Recent Windspeed in years 2024 and 2025**

``` r
plotDWD(clim, "FX.Windspitze")
```

![](README_files/figure-commonmark/plot_Wind_Speed-1.png)

## Transfer to Python

``` python
clim_py = r.clim
import matplotlib
print(f"Dataset shape: {clim_py.shape[0]} rows, {clim_py.shape[1]} columns")
```

``` python
clim_py = clim_py.select_dtypes(include=['float64', 'int64'])
clim_py.hist(figsize=(20, 16), bins=5)
```

![](README_files/figure-commonmark/histograms-1.png)

## Calculate Summary Statistics And Identify Extreme Days

``` python
# Calculate and display some basic statistics
print("\n=== Summary Statistics for Temperature ===")
```


    === Summary Statistics for Temperature ===

``` python
temp_stats = clim_py['TMK.Lufttemperatur'].describe()
print(temp_stats)
```

    count    550.000000
    mean      13.027636
    std        7.069437
    min       -4.800000
    25%        8.125000
    50%       14.150000
    75%       18.700000
    max       29.200000
    Name: TMK.Lufttemperatur, dtype: float64

``` python
# Find and display the maximum and minimum temperature days
print("\n=== Extreme Temperature Days ===")
```


    === Extreme Temperature Days ===

``` python
max_temp_idx = clim_py['TMK.Lufttemperatur'].idxmax()
min_temp_idx = clim_py['TMK.Lufttemperatur'].idxmin()

print(f"Hottest day throughout the years: {r.clim.loc[max_temp_idx, 'MESS_DATUM']} with {clim_py.loc[max_temp_idx, 'TMK.Lufttemperatur']:.1f}°C")
```

    Hottest day throughout the years: 2025-07-02 with 29.2°C

``` python
print(f"Coldest day throughout the years: {r.clim.loc[min_temp_idx, 'MESS_DATUM']} with {clim_py.loc[min_temp_idx, 'TMK.Lufttemperatur']:.1f}°C")
```

    Coldest day throughout the years: 2025-02-17 with -4.8°C

    Yazan added this chunk as part of the first homework

    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    wishing everyone a good start

    I love programming

    Happy coding!

``` r
# label: matrix-example
# Matrix
n = 1:25
n
```

     [1]  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

``` r
mat = matrix(n, nrow = 5)
mat
```

         [,1] [,2] [,3] [,4] [,5]
    [1,]    1    6   11   16   21
    [2,]    2    7   12   17   22
    [3,]    3    8   13   18   23
    [4,]    4    9   14   19   24
    [5,]    5   10   15   20   25

    Whoever reads this, likes to code

    When you're reading this, it is currently: 14:54:57.

    Success!!
