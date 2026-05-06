*Interactive Dask performance report quick links:*
- [02 - DESI x Gaia](https://olivialynn.github.io/DESI-Crossmatch-Project/02%20-%20DESI%20x%20Gaia/crossmatch_report.html)
- 03 - DESI x LSST DP1
  - [03 - DESI x LSST DP1 object](https://olivialynn.github.io/DESI-Crossmatch-Project/03%20-%20DESI%20x%20LSST%20DP1/crossmatch_report_obj.html)
  - [03 - DESI x LSST DP1 dia_object](https://olivialynn.github.io/DESI-Crossmatch-Project/03%20-%20DESI%20x%20LSST%20DP1/crossmatch_report_dia_obj.html)
- 04 (in progress)
- 05 (in progress)

---

## 01 - DESI Data
- A 700GiB catalog called `desi-dr1-main-dark` at `/global/cfs/cdirs/cosmo/users/olynn/`
  - covers DESI's **main** survey, **dark** program
- A call to `is_valid_catalog` returns True, 
  - with `5769 partitions` found 
  - and `Approximate coverage is 33.39 % of the sky.`
- Notably we are missing coverage of the galactic plane, 
  - but since our decision (co-working meeting 4/29) to skip the main/bright program and only use main/dark, this is unsurprising

### MOC: DESI Main Survey Dark Program
<img width="805" height="440" alt="Image" src="https://github.com/user-attachments/assets/6de43034-c34c-49fa-b308-377538f50d3c" />

### First 2 rows
<table id="T_ebded">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_ebded_level0_col0" class="col_heading level0 col0" >TARGETID</th>
      <th id="T_ebded_level0_col1" class="col_heading level0 col1" >TARGET_RA</th>
      <th id="T_ebded_level0_col2" class="col_heading level0 col2" >TARGET_DEC</th>
      <th id="T_ebded_level0_col3" class="col_heading level0 col3" >Z</th>
      <th id="T_ebded_level0_col4" class="col_heading level0 col4" >ZERR</th>
      <th id="T_ebded_level0_col5" class="col_heading level0 col5" >spectra_b</th>
      <th id="T_ebded_level0_col6" class="col_heading level0 col6" >spectra_r</th>
      <th id="T_ebded_level0_col7" class="col_heading level0 col7" >spectra_z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_ebded_level0_row0" class="row_heading level0 row0" >24531778214</th>
      <td id="T_ebded_row0_col0" class="data row0 col0" >39627785483846048</td>
      <td id="T_ebded_row0_col1" class="data row0 col1" >45.014136</td>
      <td id="T_ebded_row0_col2" class="data row0 col2" >0.019739</td>
      <td id="T_ebded_row0_col3" class="data row0 col3" >1.308415</td>
      <td id="T_ebded_row0_col4" class="data row0 col4" >0.000399</td>
      <td id="T_ebded_row0_col5" class="data row0 col5" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3600.0</td>
      <td>2.924896</td>
      <td>0.327872</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2750 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_ebded_row0_col6" class="data row0 col6" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5760.0</td>
      <td>1.965631</td>
      <td>7.795724</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2325 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_ebded_row0_col7" class="data row0 col7" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>7520.0</td>
      <td>0.379682</td>
      <td>23.513329</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2880 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
    </tr>
    <tr>
      <th id="T_ebded_level0_row1" class="row_heading level0 row1" >76347715933</th>
      <td id="T_ebded_row1_col0" class="data row1 col0" >39627785483846390</td>
      <td id="T_ebded_row1_col1" class="data row1 col1" >45.027565</td>
      <td id="T_ebded_row1_col2" class="data row1 col2" >0.029181</td>
      <td id="T_ebded_row1_col3" class="data row1 col3" >0.884491</td>
      <td id="T_ebded_row1_col4" class="data row1 col4" >0.000116</td>
      <td id="T_ebded_row1_col5" class="data row1 col5" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3600.0</td>
      <td>-3.560856</td>
      <td>0.253497</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2750 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_ebded_row1_col6" class="data row1 col6" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5760.0</td>
      <td>0.741585</td>
      <td>0.270924</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2325 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_ebded_row1_col7" class="data row1 col7" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>7520.0</td>
      <td>-0.305626</td>
      <td>5.653226</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2880 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table>
2 rows x 8 columns

## 02 - DESI x Gaia
- A 71 GiB catalog called `desi_x_gaia` at `/global/cfs/cdirs/cosmo/users/olynn/`
  - a crossmatch of DESI Main Survey (dark program) DR1 with Gaia DR3
- MOC appears functionally identical to the MOC included in the section above, "01 - DESI Data"
- An interactive Dask Performance Report is available [here](https://olivialynn.github.io/DESI-Crossmatch-Project/02%20-%20DESI%20x%20Gaia/crossmatch_report.html)

### First 2 rows
<table id="T_0b2e5">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_0b2e5_level0_col0" class="col_heading level0 col0" >TARGETID</th>
      <th id="T_0b2e5_level0_col1" class="col_heading level0 col1" >TARGET_RA</th>
      <th id="T_0b2e5_level0_col2" class="col_heading level0 col2" >TARGET_DEC</th>
      <th id="T_0b2e5_level0_col3" class="col_heading level0 col3" >Z</th>
      <th id="T_0b2e5_level0_col4" class="col_heading level0 col4" >ZERR</th>
      <th id="T_0b2e5_level0_col5" class="col_heading level0 col5" >spectra_b</th>
      <th id="T_0b2e5_level0_col6" class="col_heading level0 col6" >spectra_r</th>
      <th id="T_0b2e5_level0_col7" class="col_heading level0 col7" >spectra_z</th>
      <th id="T_0b2e5_level0_col8" class="col_heading level0 col8" >source_id</th>
      <th id="T_0b2e5_level0_col9" class="col_heading level0 col9" >ra</th>
      <th id="T_0b2e5_level0_col10" class="col_heading level0 col10" >dec</th>
      <th id="T_0b2e5_level0_col11" class="col_heading level0 col11" >_dist_arcsec</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_0b2e5_level0_row0" class="row_heading level0 row0" >1748843556674</th>
      <td id="T_0b2e5_row0_col0" class="data row0 col0" >39627791523645551</td>
      <td id="T_0b2e5_row0_col1" class="data row0 col1" >45.075505</td>
      <td id="T_0b2e5_row0_col2" class="data row0 col2" >0.152316</td>
      <td id="T_0b2e5_row0_col3" class="data row0 col3" >2.225343</td>
      <td id="T_0b2e5_row0_col4" class="data row0 col4" >0.000244</td>
      <td id="T_0b2e5_row0_col5" class="data row0 col5" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3600.0</td>
      <td>2.246889</td>
      <td>0.117146</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2750 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_0b2e5_row0_col6" class="data row0 col6" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5760.0</td>
      <td>0.119673</td>
      <td>6.244492</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2325 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_0b2e5_row0_col7" class="data row0 col7" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>7520.0</td>
      <td>1.12132</td>
      <td>22.01815</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2880 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_0b2e5_row0_col8" class="data row0 col8" >3470333738112</td>
      <td id="T_0b2e5_row0_col9" class="data row0 col9" >45.075505</td>
      <td id="T_0b2e5_row0_col10" class="data row0 col10" >0.152316</td>
      <td id="T_0b2e5_row0_col11" class="data row0 col11" >0.000927</td>
    </tr>
    <tr>
      <th id="T_0b2e5_level0_row1" class="row_heading level0 row1" >2652981825998</th>
      <td id="T_0b2e5_row1_col0" class="data row1 col0" >39627791519454588</td>
      <td id="T_0b2e5_row1_col1" class="data row1 col1" >44.925441</td>
      <td id="T_0b2e5_row1_col2" class="data row1 col2" >0.149561</td>
      <td id="T_0b2e5_row1_col3" class="data row1 col3" >0.000010</td>
      <td id="T_0b2e5_row1_col4" class="data row1 col4" >0.000004</td>
      <td id="T_0b2e5_row1_col5" class="data row1 col5" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3600.0</td>
      <td>-0.806199</td>
      <td>0.40013</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2750 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_0b2e5_row1_col6" class="data row1 col6" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5760.0</td>
      <td>5.079622</td>
      <td>7.327995</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2325 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_0b2e5_row1_col7" class="data row1 col7" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>7520.0</td>
      <td>3.271897</td>
      <td>17.164492</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2880 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_0b2e5_row1_col8" class="data row1 col8" >5295694864384</td>
      <td id="T_0b2e5_row1_col9" class="data row1 col9" >44.925444</td>
      <td id="T_0b2e5_row1_col10" class="data row1 col10" >0.149559</td>
      <td id="T_0b2e5_row1_col11" class="data row1 col11" >0.012942</td>
    </tr>
  </tbody>
</table>
2 rows x 12 columns

## 03a - DESI x Rubin DP1 object
- A 534M catalog called `desi_x_lsst_dp1_object` at `/global/cfs/cdirs/cosmo/users/olynn/`
  - a crossmatch of DESI Main Survey (dark program) DR1 with LSST DP1 object
- MOC is fairly tiny, which is unsurprising, as dp1 obj is a few scattered blobs mostly in the southern hemisphere (and DESI is mostly northern)
- An interactive Dask Performance Report is available [here](https://olivialynn.github.io/DESI-Crossmatch-Project/03%20-%20DESI%20x%20LSST%20DP1/crossmatch_report_obj.html), 
  - and key metrics are described and analyzed at the bottom of the [section notebook](https://github.com/olivialynn/DESI-Crossmatch-Project/blob/main/03%20-%20DESI%20x%20LSST%20DP1/3.0%20-%20DESI%20x%20DP1.ipynb)

### MOC
<img width="803" height="452" alt="Image" src="https://github.com/user-attachments/assets/910b41d1-4a46-4e9a-82f9-29d5396d7531" />

### First 2 rows
<table id="T_8d097">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_8d097_level0_col0" class="col_heading level0 col0" >TARGETID</th>
      <th id="T_8d097_level0_col1" class="col_heading level0 col1" >TARGET_RA</th>
      <th id="T_8d097_level0_col2" class="col_heading level0 col2" >TARGET_DEC</th>
      <th id="T_8d097_level0_col3" class="col_heading level0 col3" >Z</th>
      <th id="T_8d097_level0_col4" class="col_heading level0 col4" >ZERR</th>
      <th id="T_8d097_level0_col5" class="col_heading level0 col5" >spectra_b</th>
      <th id="T_8d097_level0_col6" class="col_heading level0 col6" >spectra_r</th>
      <th id="T_8d097_level0_col7" class="col_heading level0 col7" >spectra_z</th>
      <th id="T_8d097_level0_col8" class="col_heading level0 col8" >coord_dec</th>
      <th id="T_8d097_level0_col9" class="col_heading level0 col9" >coord_decErr</th>
      <th id="T_8d097_level0_col10" class="col_heading level0 col10" >coord_ra</th>
      <th id="T_8d097_level0_col11" class="col_heading level0 col11" >coord_raErr</th>
      <th id="T_8d097_level0_col12" class="col_heading level0 col12" >g_psfFlux</th>
      <th id="T_8d097_level0_col13" class="col_heading level0 col13" >g_psfFluxErr</th>
      <th id="T_8d097_level0_col14" class="col_heading level0 col14" >g_psfMag</th>
      <th id="T_8d097_level0_col15" class="col_heading level0 col15" >g_psfMagErr</th>
      <th id="T_8d097_level0_col16" class="col_heading level0 col16" >i_psfFlux</th>
      <th id="T_8d097_level0_col17" class="col_heading level0 col17" >i_psfFluxErr</th>
      <th id="T_8d097_level0_col18" class="col_heading level0 col18" >i_psfMag</th>
      <th id="T_8d097_level0_col19" class="col_heading level0 col19" >i_psfMagErr</th>
      <th id="T_8d097_level0_col20" class="col_heading level0 col20" >objectId</th>
      <th id="T_8d097_level0_col21" class="col_heading level0 col21" >patch</th>
      <th id="T_8d097_level0_col22" class="col_heading level0 col22" >r_psfFlux</th>
      <th id="T_8d097_level0_col23" class="col_heading level0 col23" >r_psfFluxErr</th>
      <th id="T_8d097_level0_col24" class="col_heading level0 col24" >r_psfMag</th>
      <th id="T_8d097_level0_col25" class="col_heading level0 col25" >r_psfMagErr</th>
      <th id="T_8d097_level0_col26" class="col_heading level0 col26" >refBand</th>
      <th id="T_8d097_level0_col27" class="col_heading level0 col27" >refFwhm</th>
      <th id="T_8d097_level0_col28" class="col_heading level0 col28" >shape_flag</th>
      <th id="T_8d097_level0_col29" class="col_heading level0 col29" >shape_xx</th>
      <th id="T_8d097_level0_col30" class="col_heading level0 col30" >shape_xy</th>
      <th id="T_8d097_level0_col31" class="col_heading level0 col31" >shape_yy</th>
      <th id="T_8d097_level0_col32" class="col_heading level0 col32" >tract</th>
      <th id="T_8d097_level0_col33" class="col_heading level0 col33" >u_psfFlux</th>
      <th id="T_8d097_level0_col34" class="col_heading level0 col34" >u_psfFluxErr</th>
      <th id="T_8d097_level0_col35" class="col_heading level0 col35" >u_psfMag</th>
      <th id="T_8d097_level0_col36" class="col_heading level0 col36" >u_psfMagErr</th>
      <th id="T_8d097_level0_col37" class="col_heading level0 col37" >x</th>
      <th id="T_8d097_level0_col38" class="col_heading level0 col38" >xErr</th>
      <th id="T_8d097_level0_col39" class="col_heading level0 col39" >y</th>
      <th id="T_8d097_level0_col40" class="col_heading level0 col40" >y_psfFlux</th>
      <th id="T_8d097_level0_col41" class="col_heading level0 col41" >y_psfFluxErr</th>
      <th id="T_8d097_level0_col42" class="col_heading level0 col42" >y_psfMag</th>
      <th id="T_8d097_level0_col43" class="col_heading level0 col43" >y_psfMagErr</th>
      <th id="T_8d097_level0_col44" class="col_heading level0 col44" >yErr</th>
      <th id="T_8d097_level0_col45" class="col_heading level0 col45" >z_psfFlux</th>
      <th id="T_8d097_level0_col46" class="col_heading level0 col46" >z_psfFluxErr</th>
      <th id="T_8d097_level0_col47" class="col_heading level0 col47" >z_psfMag</th>
      <th id="T_8d097_level0_col48" class="col_heading level0 col48" >z_psfMagErr</th>
      <th id="T_8d097_level0_col49" class="col_heading level0 col49" >objectForcedSource</th>
      <th id="T_8d097_level0_col50" class="col_heading level0 col50" >_dist_arcsec</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_8d097_level0_row0" class="row_heading level0 row0" >9194458135247551</th>
      <td id="T_8d097_row0_col0" class="data row0 col0" >39627930157977284</td>
      <td id="T_8d097_row0_col1" class="data row0 col1" >38.098532</td>
      <td id="T_8d097_row0_col2" class="data row0 col2" >5.974584</td>
      <td id="T_8d097_row0_col3" class="data row0 col3" >0.945108</td>
      <td id="T_8d097_row0_col4" class="data row0 col4" >0.000020</td>
      <td id="T_8d097_row0_col5" class="data row0 col5" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3600.0</td>
      <td>-5.854908</td>
      <td>0.133759</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2750 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_8d097_row0_col6" class="data row0 col6" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5760.0</td>
      <td>2.640895</td>
      <td>0.064621</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2325 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_8d097_row0_col7" class="data row0 col7" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>7520.0</td>
      <td>-0.092549</td>
      <td>21.761997</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2880 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_8d097_row0_col8" class="data row0 col8" >5.974598</td>
      <td id="T_8d097_row0_col9" class="data row0 col9" >0.000032</td>
      <td id="T_8d097_row0_col10" class="data row0 col10" >38.098499</td>
      <td id="T_8d097_row0_col11" class="data row0 col11" >0.000021</td>
      <td id="T_8d097_row0_col12" class="data row0 col12" >847.094604</td>
      <td id="T_8d097_row0_col13" class="data row0 col13" >119.024414</td>
      <td id="T_8d097_row0_col14" class="data row0 col14" >24.080170</td>
      <td id="T_8d097_row0_col15" class="data row0 col15" >0.153572</td>
      <td id="T_8d097_row0_col16" class="data row0 col16" ><NA></td>
      <td id="T_8d097_row0_col17" class="data row0 col17" ><NA></td>
      <td id="T_8d097_row0_col18" class="data row0 col18" ><NA></td>
      <td id="T_8d097_row0_col19" class="data row0 col19" ><NA></td>
      <td id="T_8d097_row0_col20" class="data row0 col20" >648369431235264528</td>
      <td id="T_8d097_row0_col21" class="data row0 col21" >9</td>
      <td id="T_8d097_row0_col22" class="data row0 col22" ><NA></td>
      <td id="T_8d097_row0_col23" class="data row0 col23" ><NA></td>
      <td id="T_8d097_row0_col24" class="data row0 col24" ><NA></td>
      <td id="T_8d097_row0_col25" class="data row0 col25" ><NA></td>
      <td id="T_8d097_row0_col26" class="data row0 col26" >g</td>
      <td id="T_8d097_row0_col27" class="data row0 col27" >0.858885</td>
      <td id="T_8d097_row0_col28" class="data row0 col28" >False</td>
      <td id="T_8d097_row0_col29" class="data row0 col29" >6.586972</td>
      <td id="T_8d097_row0_col30" class="data row0 col30" >-7.739595</td>
      <td id="T_8d097_row0_col31" class="data row0 col31" >15.490450</td>
      <td id="T_8d097_row0_col32" class="data row0 col32" >10464</td>
      <td id="T_8d097_row0_col33" class="data row0 col33" ><NA></td>
      <td id="T_8d097_row0_col34" class="data row0 col34" ><NA></td>
      <td id="T_8d097_row0_col35" class="data row0 col35" ><NA></td>
      <td id="T_8d097_row0_col36" class="data row0 col36" ><NA></td>
      <td id="T_8d097_row0_col37" class="data row0 col37" >28242.600806</td>
      <td id="T_8d097_row0_col38" class="data row0 col38" >0.383504</td>
      <td id="T_8d097_row0_col39" class="data row0 col39" >2054.114638</td>
      <td id="T_8d097_row0_col40" class="data row0 col40" ><NA></td>
      <td id="T_8d097_row0_col41" class="data row0 col41" ><NA></td>
      <td id="T_8d097_row0_col42" class="data row0 col42" ><NA></td>
      <td id="T_8d097_row0_col43" class="data row0 col43" ><NA></td>
      <td id="T_8d097_row0_col44" class="data row0 col44" >0.570869</td>
      <td id="T_8d097_row0_col45" class="data row0 col45" ><NA></td>
      <td id="T_8d097_row0_col46" class="data row0 col46" ><NA></td>
      <td id="T_8d097_row0_col47" class="data row0 col47" ><NA></td>
      <td id="T_8d097_row0_col48" class="data row0 col48" ><NA></td>
      <td id="T_8d097_row0_col49" class="data row0 col49" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>band</th>
      <th>coord_dec</th>
      <th>...</th>
      <th>psfMagErr</th>
      <th>visit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>g</td>
      <td>5.974598</td>
      <td>...</td>
      <td>0.175911</td>
      <td>2024112600118</td>
    </tr>
    <tr>
      <td><i>+0 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_8d097_row0_col50" class="data row0 col50" >0.129209</td>
    </tr>
    <tr>
      <th id="T_8d097_level0_row1" class="row_heading level0 row1" >9194470120764197</th>
      <td id="T_8d097_row1_col0" class="data row1 col0" >39627930157977720</td>
      <td id="T_8d097_row1_col1" class="data row1 col1" >38.119619</td>
      <td id="T_8d097_row1_col2" class="data row1 col2" >5.969811</td>
      <td id="T_8d097_row1_col3" class="data row1 col3" >-0.000010</td>
      <td id="T_8d097_row1_col4" class="data row1 col4" >0.000083</td>
      <td id="T_8d097_row1_col5" class="data row1 col5" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3600.0</td>
      <td>14.706098</td>
      <td>0.042153</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2750 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_8d097_row1_col6" class="data row1 col6" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5760.0</td>
      <td>2.254704</td>
      <td>2.631673</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2325 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_8d097_row1_col7" class="data row1 col7" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>7520.0</td>
      <td>1.311252</td>
      <td>5.532307</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2880 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_8d097_row1_col8" class="data row1 col8" >5.969770</td>
      <td id="T_8d097_row1_col9" class="data row1 col9" >0.000001</td>
      <td id="T_8d097_row1_col10" class="data row1 col10" >38.119650</td>
      <td id="T_8d097_row1_col11" class="data row1 col11" >0.000001</td>
      <td id="T_8d097_row1_col12" class="data row1 col12" >38055.558594</td>
      <td id="T_8d097_row1_col13" class="data row1 col13" >200.798843</td>
      <td id="T_8d097_row1_col14" class="data row1 col14" >19.948956</td>
      <td id="T_8d097_row1_col15" class="data row1 col15" >0.005729</td>
      <td id="T_8d097_row1_col16" class="data row1 col16" ><NA></td>
      <td id="T_8d097_row1_col17" class="data row1 col17" ><NA></td>
      <td id="T_8d097_row1_col18" class="data row1 col18" ><NA></td>
      <td id="T_8d097_row1_col19" class="data row1 col19" ><NA></td>
      <td id="T_8d097_row1_col20" class="data row1 col20" >648369431235265544</td>
      <td id="T_8d097_row1_col21" class="data row1 col21" >9</td>
      <td id="T_8d097_row1_col22" class="data row1 col22" ><NA></td>
      <td id="T_8d097_row1_col23" class="data row1 col23" ><NA></td>
      <td id="T_8d097_row1_col24" class="data row1 col24" ><NA></td>
      <td id="T_8d097_row1_col25" class="data row1 col25" ><NA></td>
      <td id="T_8d097_row1_col26" class="data row1 col26" >g</td>
      <td id="T_8d097_row1_col27" class="data row1 col27" >0.876047</td>
      <td id="T_8d097_row1_col28" class="data row1 col28" >False</td>
      <td id="T_8d097_row1_col29" class="data row1 col29" >5.210234</td>
      <td id="T_8d097_row1_col30" class="data row1 col30" >-0.492065</td>
      <td id="T_8d097_row1_col31" class="data row1 col31" >4.914106</td>
      <td id="T_8d097_row1_col32" class="data row1 col32" >10464</td>
      <td id="T_8d097_row1_col33" class="data row1 col33" ><NA></td>
      <td id="T_8d097_row1_col34" class="data row1 col34" ><NA></td>
      <td id="T_8d097_row1_col35" class="data row1 col35" ><NA></td>
      <td id="T_8d097_row1_col36" class="data row1 col36" ><NA></td>
      <td id="T_8d097_row1_col37" class="data row1 col37" >27863.990168</td>
      <td id="T_8d097_row1_col38" class="data row1 col38" >0.020303</td>
      <td id="T_8d097_row1_col39" class="data row1 col39" >1966.683019</td>
      <td id="T_8d097_row1_col40" class="data row1 col40" ><NA></td>
      <td id="T_8d097_row1_col41" class="data row1 col41" ><NA></td>
      <td id="T_8d097_row1_col42" class="data row1 col42" ><NA></td>
      <td id="T_8d097_row1_col43" class="data row1 col43" ><NA></td>
      <td id="T_8d097_row1_col44" class="data row1 col44" >0.018366</td>
      <td id="T_8d097_row1_col45" class="data row1 col45" ><NA></td>
      <td id="T_8d097_row1_col46" class="data row1 col46" ><NA></td>
      <td id="T_8d097_row1_col47" class="data row1 col47" ><NA></td>
      <td id="T_8d097_row1_col48" class="data row1 col48" ><NA></td>
      <td id="T_8d097_row1_col49" class="data row1 col49" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>band</th>
      <th>coord_dec</th>
      <th>...</th>
      <th>psfMagErr</th>
      <th>visit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>g</td>
      <td>5.96977</td>
      <td>...</td>
      <td>0.006436</td>
      <td>2024112600118</td>
    </tr>
    <tr>
      <td><i>+0 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_8d097_row1_col50" class="data row1 col50" >0.184922</td>
    </tr>
  </tbody>
</table>
2 rows x 51 columns

## 03b - DESI x Rubin DP1 dia object
- A 27M catalog called `desi_x_lsst_dp1_dia_object` at `/global/cfs/cdirs/cosmo/users/olynn/`
  - a crossmatch of DESI Main Survey (dark program) DR1 with LSST DP1 dia object
- MOC is fairly tiny here as well
- An interactive Dask Performance Report is available [here](https://olivialynn.github.io/DESI-Crossmatch-Project/03%20-%20DESI%20x%20LSST%20DP1/crossmatch_report_obj.html), 
  - and key metrics are described and analyzed at the bottom of the [section notebook](https://github.com/olivialynn/DESI-Crossmatch-Project/blob/main/03%20-%20DESI%20x%20LSST%20DP1/3.0%20-%20DESI%20x%20DP1.ipynb)

### MOC
Appears the same as the MOC above

### First 2 rows
<table id="T_e1d28">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_e1d28_level0_col0" class="col_heading level0 col0" >TARGETID</th>
      <th id="T_e1d28_level0_col1" class="col_heading level0 col1" >TARGET_RA</th>
      <th id="T_e1d28_level0_col2" class="col_heading level0 col2" >TARGET_DEC</th>
      <th id="T_e1d28_level0_col3" class="col_heading level0 col3" >Z</th>
      <th id="T_e1d28_level0_col4" class="col_heading level0 col4" >ZERR</th>
      <th id="T_e1d28_level0_col5" class="col_heading level0 col5" >spectra_b</th>
      <th id="T_e1d28_level0_col6" class="col_heading level0 col6" >spectra_r</th>
      <th id="T_e1d28_level0_col7" class="col_heading level0 col7" >spectra_z</th>
      <th id="T_e1d28_level0_col8" class="col_heading level0 col8" >diaObjectId</th>
      <th id="T_e1d28_level0_col9" class="col_heading level0 col9" >ra</th>
      <th id="T_e1d28_level0_col10" class="col_heading level0 col10" >dec</th>
      <th id="T_e1d28_level0_col11" class="col_heading level0 col11" >_dist_arcsec</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_e1d28_level0_row0" class="row_heading level0 row0" >9194470120764197</th>
      <td id="T_e1d28_row0_col0" class="data row0 col0" >39627930157977720</td>
      <td id="T_e1d28_row0_col1" class="data row0 col1" >38.119619</td>
      <td id="T_e1d28_row0_col2" class="data row0 col2" >5.969811</td>
      <td id="T_e1d28_row0_col3" class="data row0 col3" >-0.000010</td>
      <td id="T_e1d28_row0_col4" class="data row0 col4" >0.000083</td>
      <td id="T_e1d28_row0_col5" class="data row0 col5" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3600.0</td>
      <td>14.706098</td>
      <td>0.042153</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2750 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_e1d28_row0_col6" class="data row0 col6" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5760.0</td>
      <td>2.254704</td>
      <td>2.631673</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2325 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_e1d28_row0_col7" class="data row0 col7" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>7520.0</td>
      <td>1.311252</td>
      <td>5.532307</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2880 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_e1d28_row0_col8" class="data row0 col8" >648369431235264515</td>
      <td id="T_e1d28_row0_col9" class="data row0 col9" >38.119650</td>
      <td id="T_e1d28_row0_col10" class="data row0 col10" >5.969770</td>
      <td id="T_e1d28_row0_col11" class="data row0 col11" >0.183285</td>
    </tr>
    <tr>
      <th id="T_e1d28_level0_row1" class="row_heading level0 row1" >9196142493359154</th>
      <td id="T_e1d28_row1_col0" class="data row1 col0" >39627930162168188</td>
      <td id="T_e1d28_row1_col1" class="data row1 col1" >38.177732</td>
      <td id="T_e1d28_row1_col2" class="data row1 col2" >6.097595</td>
      <td id="T_e1d28_row1_col3" class="data row1 col3" >-0.000078</td>
      <td id="T_e1d28_row1_col4" class="data row1 col4" >0.000004</td>
      <td id="T_e1d28_row1_col5" class="data row1 col5" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3600.0</td>
      <td>16.388857</td>
      <td>0.045339</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2750 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_e1d28_row1_col6" class="data row1 col6" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5760.0</td>
      <td>21.66119</td>
      <td>0.57832</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2325 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_e1d28_row1_col7" class="data row1 col7" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>wavelength</th>
      <th>flux</th>
      <th>ivar</th>
      <th>mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>7520.0</td>
      <td>15.090705</td>
      <td>1.642342</td>
      <td>0</td>
    </tr>
    <tr>
      <td><i>+2880 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_e1d28_row1_col8" class="data row1 col8" >648370049710555147</td>
      <td id="T_e1d28_row1_col9" class="data row1 col9" >38.177748</td>
      <td id="T_e1d28_row1_col10" class="data row1 col10" >6.097579</td>
      <td id="T_e1d28_row1_col11" class="data row1 col11" >0.082570</td>
    </tr>
  </tbody>
</table>
2 rows x 12 columns
