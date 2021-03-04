#!/usr/bin/env gnuplot

set terminal postscript eps  size 4.6, 2.80 \
                             enhanced color \
                             font 'Helvetica,24' \
                             linewidth 1
set output 'bovine_frequency.eps'

unset key

set xlabel 'Cutoff'
set ylabel '#Entries'
set yrange [0:350]
set ytics 50

plot 'count_bovine.dat' using 1:2 with linespoints pointtype 7 pointsize 2 linewidth 1 linecolor rgb '#003f5c'

