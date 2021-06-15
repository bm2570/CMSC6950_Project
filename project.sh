python3 distance_calculations.py
python3 distance_plot.py
python3 latlong.py
python3 heatplot.py latlon_inoue.dat Z
python3 heatplot.py latlon_inoue.dat DM
python3 heatplot.py latlon_zhang.dat Z
python3 heatplot.py latlon_zhang.dat DM
python3 heatplot.py latlon_ioka.dat Z
python3 heatplot.py latlon_ioka.dat DM
awk '$1==-9.090909090909065071e-01 {print}' latlon_inoue.dat > latcut_inoue.dat
awk '$1==-9.090909090909065071e-01{print}' latlon_zhang.dat > latcut_zhang.dat
awk '$1==-9.090909090909065071e-01{print}' latlon_ioka.dat > latcut_ioka.dat
python3 plot_latlongcuts.py
mv *.png /report
