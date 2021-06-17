all: report.pdf distance_Inoue2004.dat distance_Zhang2018.dat distance_Ioka2003.dat Z_vs_DM.png distance_vs_DM.png latlon_Zhang2018.dat latlon_Ioka2003.dat latlon_Inoue2004.dat DM_heatplot_Ioka2003.png DM_heatplot_Inoue2004.png DM_heatplot_Zhang2018.png redshift_heatplot_Ioka2003.png redshift_heatplot_Inoue2004.png redshift_heatplot_Zhang2018.png latcut_Zhang2018.dat latcut_Inoue2004.dat latcut_Ioka2003.dat Z_vs_longitude.png DM_vs_longitude.png

report.pdf: refs.bib
	latexmk -pdf

distance_Inoue2004.dat: distance_calculations.py
	python3 distance_calculations.py Inoue2004

distance_Zhang2018.dat: distance_calculations.py
	python3 distance_calculations.py Zhang2018

distance_Inoue2004.dat: distance_calculations.py
	python3 distance_calculations.py Inoue2004

distance_Ioka2003.dat: distance_calculations.py
	python3 distance_calculations.py Ioka2003

Z_vs_DM.png: distance_plot.py distance_Zhang2018.dat distance_Inoue2004.dat distance_Ioka2003.dat
	python3 distance_plot.py

distance_vs_DM.png: distance_plot.py distance_Zhang2018.dat distance_Inoue2004.dat distance_Ioka2003.dat
	python3 distance_plot.py

latlon_Zhang2018.dat: latlong.py
	python3 latlong.py Zhang2018

latlon_Inoue2004.dat: latlong.py
	python3 latlong.py Inoue2004

latlon_Ioka2003.dat: latlong.py
	python3 latlong.py Ioka2003

redshift_heatplot_Zhang2018.png: heatplot.py latlon_Zhang2018.dat
	python3 heatplot.py latlon_Zhang2018.dat Z

DM_heatplot_Zhang2018.png: heatplot.py latlon_Zhang2018.dat
	python3 heatplot.py latlon_Zhang2018.dat DM


redshift_heatplot_Inoue2004.png: heatplot.py latlon_Inoue2004.dat
	python3 heatplot.py latlon_Inoue2004.dat Z

DM_heatplot_Inoue2004.png: heatplot.py latlon_Inoue2004.dat
	python3 heatplot.py latlon_Inoue2004.dat DM

redshift_heatplot_Ioka2003.png: heatplot.py latlon_Ioka2003.dat
	python3 heatplot.py latlon_Ioka2003.dat Z

DM_heatplot_Ioka2003.png: heatplot.py latlon_Ioka2003.dat
	python3 heatplot.py latlon_Ioka2003.dat DM

latcut_Ioka2003.dat: latlon_Ioka2003.dat
	awk '$$1==-9.090909090909065071e-01{print}' latlon_Ioka2003.dat > latcut_Ioka2003.dat

latcut_Inoue2004.dat: latlon_Inoue2004.dat
	awk '$$1==-9.090909090909065071e-01{print}' latlon_Inoue2004.dat > latcut_Inoue2004.dat

latcut_Zhang2018.dat: latlon_Zhang2018.dat
	awk '$$1==-9.090909090909065071e-01{print}' latlon_Zhang2018.dat > latcut_Zhang2018.dat

Z_vs_longitude.png: latlon_Zhang2018.dat latlon_Inoue2004.dat latlon_Ioka2003.dat
	python3 plot_latlongcuts.py

DM_vs_longitude.png: latlon_Zhang2018.dat latlon_Inoue2004.dat latlon_Ioka2003.dat
	python3 plot_latlongcuts.py

clean:
	latexmk -c
	rm *.dat
	rm *.png
