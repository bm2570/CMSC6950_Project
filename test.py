import fruitbat

FRB180110 = fruitbat.Frb(715.7, gl="7.8", gb="-51.9", name="FRB180110")
test_calc=FRB180110.calc_dm_galaxy()
print(test_calc)
FRB180110.calc_redshift(method="Zhang2018", cosmology="Planck18")
