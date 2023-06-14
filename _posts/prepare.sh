#!/bin/bash
lyx_file="$1.lyx"
tex_file="$1.tex"
lyx --force-overwrite --export pdflatex $lyx_file
creationdate=`grep -rw CreatedInfo $tex_file |  awk 'BEGIN { FS = ":" } ; {print $2}' | sed 's/^[ \t]*//;s/[ \t]*$//'`
title=`grep -rw TitleInfo: $tex_file |  awk 'BEGIN { FS = ":" } ; {print $2}'| sed 's/^[ \t]*//;s/[ \t]*$//'`

sed -i '/CreatedInfo/d' $tex_file
sed -i '/TitleInfo/d' $tex_file
rm -rf gg.md
pandoc -t markdown-citations -s $tex_file -o gg.md  --mathjax --bibliography Bibliography.bib
out_file="$creationdate-$1.md"
rm -rf $out_file
cat ~/GIT/goravjindal.github.io/_posts/pre.txt gg.md >>  $out_file
sed -i "s/fill_date/$creationdate/g" $out_file
sed -i "s/fill_title/$title/g" $out_file
sed -i "s/fill_des/$title/g" $out_file

cp -rf $out_file ~/GIT/goravjindal.github.io/_posts/


