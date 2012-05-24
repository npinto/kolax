Kolax
Photo Collages

Random notes:
-------------
* to resize the smaller edge to 256: `convert in.jpg -resize "256^>" out.jpg`
* to resize the larger edge to 256: `convert in.jpg -resize "256>" out.jpg`
* to resize and crop at the center: `export SIZE=64; convert babou.jpg -resize "$SIZE^>" -gravity center -crop ${SIZE}x${SIZE}+0+0 out.jpg`
