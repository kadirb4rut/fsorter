## Table of contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [How to use Fsorter](#how-to-use-Fsorter)
* [Example](#Example)
* [Example 2](#example-2)
* [Note](#Note)

## General Info
This program checks the numeric values ​​at the end of the  file names in the folder and sorts the file names from the smallest number to the larger number.
	
## Technologies
Project is created with:
* Python 3.8
	
## Setup
To run this project, install it locally using pip:

```
$ pip install fsorter

```

## How to use Fsorter

```
from fsorter import fsorter

test_list = filesort('file path',['extensions'])
 
```

## Example

```
from fsorter import fsorter

test_list = filesort('C://Windows//Users//test_user//Desktop//test_folder',['jpg','png','tiff','pdf','pptx','xlsx'])
 
```

## Example 2

You can make an example like below to see how it sorts files in console output.

```

from fsorter import fileSort

dir='test'
test=fileSort(dir)

for k in test:
    print(k)
 
```

## Note

If the file extensions that need to be sorted into the Fsorter program are not entered as parameters, by default they are ['.jpg', '.png', '.jpeg', '.tif', '.tiff', '.nii', '.JPG', '. JPEG', '.TIFF', '.TIF', '.NII'] extensions sort.
 





