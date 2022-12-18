# Convert Remarkable exports for Google Drive

At the moment, The exported pdfs from the remarkable 2 tablet 
cannot be indexed by Google Drive.

This is because the remarkable produces native pdfs that include an image
for each page in the notebook. But on the other hand, Google Drive does not run 
OCR on the images included in a pdf.

This package provides a solution, which is to: 

* export a notebook as png from the remarkable application. This creates a folder
with png files inside
* run `rk_to_pdf` to create a single pdf from all images in this folder

## Prerequisites

* A Linux-based system
* python 3.10 (though it will probably work with previous versions of python)

## Installation

* Clone this package
* Install : 

```shell
pip install -r requirements.txt
pip install . 
```

## Run 

An example output from remarkable is provided in 
[tests/data/lambdas]

```shell
rk_to_pdf tests/data/lambdas
```

You should get a file `lambdas.pdf` next to the input directory.

You can now upload this file to google drive and it will be indexed. 







