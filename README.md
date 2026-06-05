*Interactive Dask performance report quick links:*
- [02 - DESI x Gaia](https://olivialynn.github.io/DESI-Crossmatch-Project/02%20-%20DESI%20x%20Gaia/crossmatch_report.html)
- 03 - DESI x LSST DP1
  - [03 - DESI x LSST DP1 dia_object](https://olivialynn.github.io/DESI-Crossmatch-Project/03%20-%20DESI%20x%20LSST%20DP1/crossmatch_report_dia_obj.html)
  - [03 - DESI x LSST DP1 object](https://olivialynn.github.io/DESI-Crossmatch-Project/03%20-%20DESI%20x%20LSST%20DP1/crossmatch_report_obj.html)
- [04 - DESI DR1 x DESI Legacy](https://olivialynn.github.io/DESI-Crossmatch-Project/04%20-%20DESI%20DR1%20x%20DESI%20Legacy/crossmatch_report.html)
- 05 - DESI x LSST DP2
  - [05a - DESI x LSST DP2 dia object](https://olivialynn.github.io/DESI-Crossmatch-Project/05%20-%20DESI%20x%20LSST%20DP2/crossmatch_report_dia_obj.html)
  - [05b - DESI x LSST DP2 object](https://olivialynn.github.io/DESI-Crossmatch-Project/05%20-%20DESI%20x%20LSST%20DP2/crossmatch_report_object.html)

---

## 01 - DESI Data
- A 700GiB catalog called `desi-dr1-main-dark` at `/global/cfs/cdirs/cosmo/www/users/olynn/`
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
- A call to `is_valid_catalog` returns True,
  - with `5764` partitions found
  - and `Approximate coverage is 33.38 % of the sky.`
- MOC appears functionally identical to the MOC included in the section above, "01 - DESI Data"
- An interactive Dask Performance Report is available [here](https://olivialynn.github.io/DESI-Crossmatch-Project/02%20-%20DESI%20x%20Gaia/crossmatch_report.html)

### MOC
Appears very similar to the MOC above

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
- A call to `is_valid_catalog` returns True,
  - with `60` partitions found
  - and `Approximate coverage is 0.01 % of the sky.`
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
- A call to `is_valid_catalog` returns True,
  - with `7` partitions found
  - and `Approximate coverage is 0.01 % of the sky.`
- MOC is fairly tiny here as well
- An interactive Dask Performance Report is available [here](https://olivialynn.github.io/DESI-Crossmatch-Project/03%20-%20DESI%20x%20LSST%20DP1/crossmatch_report_obj.html), 
  - and key metrics are described and analyzed at the bottom of the [section notebook](https://github.com/olivialynn/DESI-Crossmatch-Project/blob/main/03%20-%20DESI%20x%20LSST%20DP1/3.0%20-%20DESI%20x%20DP1.ipynb)

### MOC
Appears very similar to the MOC above

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

## 04 - DESI DR1 x DESI Legacy
- A 561G GiB catalog called `desi_dr1_x_desi_legacy` at `/global/cfs/cdirs/cosmo/users/olynn/`
  - a crossmatch of DESI Main Survey (dark program) DR1 with DESI Legacy Survey DR 10.1
- A call to `is_valid_catalog` returns True,
  - with `19,221` partitions found
  - and `Approximate coverage is 21.77 % of the sky.`
- An interactive Dask Performance Report is available [here](https://olivialynn.github.io/DESI-Crossmatch-Project/04%20-%20DESI%20DR1%20x%20DESI%20Legacy/crossmatch_report.html), 
  - and key metrics are described and analyzed at the bottom of the [section notebook](https://github.com/olivialynn/DESI-Crossmatch-Project/blob/main/04%20-%20DESI%20DR1%20x%20DESI%20Legacy/4.0%20-%20DESI%20DR1%20x%20DESI%20Legacy.ipynb)

### MOC
<img width="815" height="457" alt="Image" src="https://github.com/user-attachments/assets/917910bc-d9a8-4358-854c-9b5ff3f016a0" />

### First 2 rows
<table id="T_57548">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_57548_level0_col0" class="col_heading level0 col0" >TARGETID</th>
      <th id="T_57548_level0_col1" class="col_heading level0 col1" >TARGET_RA</th>
      <th id="T_57548_level0_col2" class="col_heading level0 col2" >TARGET_DEC</th>
      <th id="T_57548_level0_col3" class="col_heading level0 col3" >Z</th>
      <th id="T_57548_level0_col4" class="col_heading level0 col4" >ZERR</th>
      <th id="T_57548_level0_col5" class="col_heading level0 col5" >spectra_b</th>
      <th id="T_57548_level0_col6" class="col_heading level0 col6" >spectra_r</th>
      <th id="T_57548_level0_col7" class="col_heading level0 col7" >spectra_z</th>
      <th id="T_57548_level0_col8" class="col_heading level0 col8" >RELEASE</th>
      <th id="T_57548_level0_col9" class="col_heading level0 col9" >BRICKID</th>
      <th id="T_57548_level0_col10" class="col_heading level0 col10" >BRICKNAME</th>
      <th id="T_57548_level0_col11" class="col_heading level0 col11" >OBJID</th>
      <th id="T_57548_level0_col12" class="col_heading level0 col12" >TYPE</th>
      <th id="T_57548_level0_col13" class="col_heading level0 col13" >RA</th>
      <th id="T_57548_level0_col14" class="col_heading level0 col14" >DEC</th>
      <th id="T_57548_level0_col15" class="col_heading level0 col15" >RA_IVAR</th>
      <th id="T_57548_level0_col16" class="col_heading level0 col16" >DEC_IVAR</th>
      <th id="T_57548_level0_col17" class="col_heading level0 col17" >DCHISQ</th>
      <th id="T_57548_level0_col18" class="col_heading level0 col18" >EBV</th>
      <th id="T_57548_level0_col19" class="col_heading level0 col19" >FLUX_G</th>
      <th id="T_57548_level0_col20" class="col_heading level0 col20" >FLUX_R</th>
      <th id="T_57548_level0_col21" class="col_heading level0 col21" >FLUX_I</th>
      <th id="T_57548_level0_col22" class="col_heading level0 col22" >FLUX_Z</th>
      <th id="T_57548_level0_col23" class="col_heading level0 col23" >FLUX_W1</th>
      <th id="T_57548_level0_col24" class="col_heading level0 col24" >FLUX_W2</th>
      <th id="T_57548_level0_col25" class="col_heading level0 col25" >FLUX_W3</th>
      <th id="T_57548_level0_col26" class="col_heading level0 col26" >FLUX_W4</th>
      <th id="T_57548_level0_col27" class="col_heading level0 col27" >FLUX_IVAR_G</th>
      <th id="T_57548_level0_col28" class="col_heading level0 col28" >FLUX_IVAR_R</th>
      <th id="T_57548_level0_col29" class="col_heading level0 col29" >FLUX_IVAR_I</th>
      <th id="T_57548_level0_col30" class="col_heading level0 col30" >FLUX_IVAR_Z</th>
      <th id="T_57548_level0_col31" class="col_heading level0 col31" >FLUX_IVAR_W1</th>
      <th id="T_57548_level0_col32" class="col_heading level0 col32" >FLUX_IVAR_W2</th>
      <th id="T_57548_level0_col33" class="col_heading level0 col33" >FLUX_IVAR_W3</th>
      <th id="T_57548_level0_col34" class="col_heading level0 col34" >FLUX_IVAR_W4</th>
      <th id="T_57548_level0_col35" class="col_heading level0 col35" >MW_TRANSMISSION_G</th>
      <th id="T_57548_level0_col36" class="col_heading level0 col36" >MW_TRANSMISSION_R</th>
      <th id="T_57548_level0_col37" class="col_heading level0 col37" >MW_TRANSMISSION_I</th>
      <th id="T_57548_level0_col38" class="col_heading level0 col38" >MW_TRANSMISSION_Z</th>
      <th id="T_57548_level0_col39" class="col_heading level0 col39" >MW_TRANSMISSION_W1</th>
      <th id="T_57548_level0_col40" class="col_heading level0 col40" >MW_TRANSMISSION_W2</th>
      <th id="T_57548_level0_col41" class="col_heading level0 col41" >MW_TRANSMISSION_W3</th>
      <th id="T_57548_level0_col42" class="col_heading level0 col42" >MW_TRANSMISSION_W4</th>
      <th id="T_57548_level0_col43" class="col_heading level0 col43" >NOBS_G</th>
      <th id="T_57548_level0_col44" class="col_heading level0 col44" >NOBS_R</th>
      <th id="T_57548_level0_col45" class="col_heading level0 col45" >NOBS_I</th>
      <th id="T_57548_level0_col46" class="col_heading level0 col46" >NOBS_Z</th>
      <th id="T_57548_level0_col47" class="col_heading level0 col47" >NOBS_W1</th>
      <th id="T_57548_level0_col48" class="col_heading level0 col48" >NOBS_W2</th>
      <th id="T_57548_level0_col49" class="col_heading level0 col49" >NOBS_W3</th>
      <th id="T_57548_level0_col50" class="col_heading level0 col50" >NOBS_W4</th>
      <th id="T_57548_level0_col51" class="col_heading level0 col51" >RCHISQ_G</th>
      <th id="T_57548_level0_col52" class="col_heading level0 col52" >RCHISQ_R</th>
      <th id="T_57548_level0_col53" class="col_heading level0 col53" >RCHISQ_I</th>
      <th id="T_57548_level0_col54" class="col_heading level0 col54" >RCHISQ_Z</th>
      <th id="T_57548_level0_col55" class="col_heading level0 col55" >RCHISQ_W1</th>
      <th id="T_57548_level0_col56" class="col_heading level0 col56" >RCHISQ_W2</th>
      <th id="T_57548_level0_col57" class="col_heading level0 col57" >RCHISQ_W3</th>
      <th id="T_57548_level0_col58" class="col_heading level0 col58" >RCHISQ_W4</th>
      <th id="T_57548_level0_col59" class="col_heading level0 col59" >FRACFLUX_G</th>
      <th id="T_57548_level0_col60" class="col_heading level0 col60" >FRACFLUX_R</th>
      <th id="T_57548_level0_col61" class="col_heading level0 col61" >FRACFLUX_I</th>
      <th id="T_57548_level0_col62" class="col_heading level0 col62" >FRACFLUX_Z</th>
      <th id="T_57548_level0_col63" class="col_heading level0 col63" >FRACFLUX_W1</th>
      <th id="T_57548_level0_col64" class="col_heading level0 col64" >FRACFLUX_W2</th>
      <th id="T_57548_level0_col65" class="col_heading level0 col65" >FRACFLUX_W3</th>
      <th id="T_57548_level0_col66" class="col_heading level0 col66" >FRACFLUX_W4</th>
      <th id="T_57548_level0_col67" class="col_heading level0 col67" >FRACMASKED_G</th>
      <th id="T_57548_level0_col68" class="col_heading level0 col68" >FRACMASKED_R</th>
      <th id="T_57548_level0_col69" class="col_heading level0 col69" >FRACMASKED_I</th>
      <th id="T_57548_level0_col70" class="col_heading level0 col70" >FRACMASKED_Z</th>
      <th id="T_57548_level0_col71" class="col_heading level0 col71" >FRACIN_G</th>
      <th id="T_57548_level0_col72" class="col_heading level0 col72" >FRACIN_R</th>
      <th id="T_57548_level0_col73" class="col_heading level0 col73" >FRACIN_I</th>
      <th id="T_57548_level0_col74" class="col_heading level0 col74" >FRACIN_Z</th>
      <th id="T_57548_level0_col75" class="col_heading level0 col75" >ANYMASK_G</th>
      <th id="T_57548_level0_col76" class="col_heading level0 col76" >ANYMASK_R</th>
      <th id="T_57548_level0_col77" class="col_heading level0 col77" >ANYMASK_I</th>
      <th id="T_57548_level0_col78" class="col_heading level0 col78" >ANYMASK_Z</th>
      <th id="T_57548_level0_col79" class="col_heading level0 col79" >ALLMASK_G</th>
      <th id="T_57548_level0_col80" class="col_heading level0 col80" >ALLMASK_R</th>
      <th id="T_57548_level0_col81" class="col_heading level0 col81" >ALLMASK_I</th>
      <th id="T_57548_level0_col82" class="col_heading level0 col82" >ALLMASK_Z</th>
      <th id="T_57548_level0_col83" class="col_heading level0 col83" >WISEMASK_W1</th>
      <th id="T_57548_level0_col84" class="col_heading level0 col84" >WISEMASK_W2</th>
      <th id="T_57548_level0_col85" class="col_heading level0 col85" >PSFSIZE_G</th>
      <th id="T_57548_level0_col86" class="col_heading level0 col86" >PSFSIZE_R</th>
      <th id="T_57548_level0_col87" class="col_heading level0 col87" >PSFSIZE_I</th>
      <th id="T_57548_level0_col88" class="col_heading level0 col88" >PSFSIZE_Z</th>
      <th id="T_57548_level0_col89" class="col_heading level0 col89" >PSFDEPTH_G</th>
      <th id="T_57548_level0_col90" class="col_heading level0 col90" >PSFDEPTH_R</th>
      <th id="T_57548_level0_col91" class="col_heading level0 col91" >PSFDEPTH_I</th>
      <th id="T_57548_level0_col92" class="col_heading level0 col92" >PSFDEPTH_Z</th>
      <th id="T_57548_level0_col93" class="col_heading level0 col93" >GALDEPTH_G</th>
      <th id="T_57548_level0_col94" class="col_heading level0 col94" >GALDEPTH_R</th>
      <th id="T_57548_level0_col95" class="col_heading level0 col95" >GALDEPTH_I</th>
      <th id="T_57548_level0_col96" class="col_heading level0 col96" >GALDEPTH_Z</th>
      <th id="T_57548_level0_col97" class="col_heading level0 col97" >PSFDEPTH_W1</th>
      <th id="T_57548_level0_col98" class="col_heading level0 col98" >PSFDEPTH_W2</th>
      <th id="T_57548_level0_col99" class="col_heading level0 col99" >WISE_COADD_ID</th>
      <th id="T_57548_level0_col100" class="col_heading level0 col100" >SHAPE_R</th>
      <th id="T_57548_level0_col101" class="col_heading level0 col101" >SHAPE_R_IVAR</th>
      <th id="T_57548_level0_col102" class="col_heading level0 col102" >SHAPE_E1</th>
      <th id="T_57548_level0_col103" class="col_heading level0 col103" >SHAPE_E1_IVAR</th>
      <th id="T_57548_level0_col104" class="col_heading level0 col104" >SHAPE_E2</th>
      <th id="T_57548_level0_col105" class="col_heading level0 col105" >SHAPE_E2_IVAR</th>
      <th id="T_57548_level0_col106" class="col_heading level0 col106" >FIBERFLUX_G</th>
      <th id="T_57548_level0_col107" class="col_heading level0 col107" >FIBERFLUX_R</th>
      <th id="T_57548_level0_col108" class="col_heading level0 col108" >FIBERFLUX_I</th>
      <th id="T_57548_level0_col109" class="col_heading level0 col109" >FIBERFLUX_Z</th>
      <th id="T_57548_level0_col110" class="col_heading level0 col110" >FIBERTOTFLUX_G</th>
      <th id="T_57548_level0_col111" class="col_heading level0 col111" >FIBERTOTFLUX_R</th>
      <th id="T_57548_level0_col112" class="col_heading level0 col112" >FIBERTOTFLUX_I</th>
      <th id="T_57548_level0_col113" class="col_heading level0 col113" >FIBERTOTFLUX_Z</th>
      <th id="T_57548_level0_col114" class="col_heading level0 col114" >REF_CAT</th>
      <th id="T_57548_level0_col115" class="col_heading level0 col115" >REF_ID</th>
      <th id="T_57548_level0_col116" class="col_heading level0 col116" >REF_EPOCH</th>
      <th id="T_57548_level0_col117" class="col_heading level0 col117" >GAIA_PHOT_G_MEAN_MAG</th>
      <th id="T_57548_level0_col118" class="col_heading level0 col118" >GAIA_PHOT_G_MEAN_FLUX_OVER_ERROR</th>
      <th id="T_57548_level0_col119" class="col_heading level0 col119" >GAIA_PHOT_BP_MEAN_MAG</th>
      <th id="T_57548_level0_col120" class="col_heading level0 col120" >GAIA_PHOT_BP_MEAN_FLUX_OVER_ERROR</th>
      <th id="T_57548_level0_col121" class="col_heading level0 col121" >GAIA_PHOT_RP_MEAN_MAG</th>
      <th id="T_57548_level0_col122" class="col_heading level0 col122" >GAIA_PHOT_RP_MEAN_FLUX_OVER_ERROR</th>
      <th id="T_57548_level0_col123" class="col_heading level0 col123" >GAIA_ASTROMETRIC_EXCESS_NOISE</th>
      <th id="T_57548_level0_col124" class="col_heading level0 col124" >GAIA_DUPLICATED_SOURCE</th>
      <th id="T_57548_level0_col125" class="col_heading level0 col125" >GAIA_PHOT_BP_RP_EXCESS_FACTOR</th>
      <th id="T_57548_level0_col126" class="col_heading level0 col126" >GAIA_ASTROMETRIC_SIGMA5D_MAX</th>
      <th id="T_57548_level0_col127" class="col_heading level0 col127" >GAIA_ASTROMETRIC_PARAMS_SOLVED</th>
      <th id="T_57548_level0_col128" class="col_heading level0 col128" >PARALLAX</th>
      <th id="T_57548_level0_col129" class="col_heading level0 col129" >PARALLAX_IVAR</th>
      <th id="T_57548_level0_col130" class="col_heading level0 col130" >PMRA</th>
      <th id="T_57548_level0_col131" class="col_heading level0 col131" >PMRA_IVAR</th>
      <th id="T_57548_level0_col132" class="col_heading level0 col132" >PMDEC</th>
      <th id="T_57548_level0_col133" class="col_heading level0 col133" >PMDEC_IVAR</th>
      <th id="T_57548_level0_col134" class="col_heading level0 col134" >MASKBITS</th>
      <th id="T_57548_level0_col135" class="col_heading level0 col135" >FITBITS</th>
      <th id="T_57548_level0_col136" class="col_heading level0 col136" >SERSIC</th>
      <th id="T_57548_level0_col137" class="col_heading level0 col137" >SERSIC_IVAR</th>
      <th id="T_57548_level0_col138" class="col_heading level0 col138" >_dist_arcsec</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_57548_level0_row0" class="row_heading level0 row0" >24531778214</th>
      <td id="T_57548_row0_col0" class="data row0 col0" >39627785483846048</td>
      <td id="T_57548_row0_col1" class="data row0 col1" >45.014136</td>
      <td id="T_57548_row0_col2" class="data row0 col2" >0.019739</td>
      <td id="T_57548_row0_col3" class="data row0 col3" >1.308415</td>
      <td id="T_57548_row0_col4" class="data row0 col4" >0.000399</td>
      <td id="T_57548_row0_col5" class="data row0 col5" ><table border="1" class="dataframe">
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
      <td id="T_57548_row0_col6" class="data row0 col6" ><table border="1" class="dataframe">
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
      <td id="T_57548_row0_col7" class="data row0 col7" ><table border="1" class="dataframe">
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
      <td id="T_57548_row0_col8" class="data row0 col8" >10000</td>
      <td id="T_57548_row0_col9" class="data row0 col9" >330548</td>
      <td id="T_57548_row0_col10" class="data row0 col10" >0451p000</td>
      <td id="T_57548_row0_col11" class="data row0 col11" >442</td>
      <td id="T_57548_row0_col12" class="data row0 col12" >PSF</td>
      <td id="T_57548_row0_col13" class="data row0 col13" >45.014136</td>
      <td id="T_57548_row0_col14" class="data row0 col14" >0.019740</td>
      <td id="T_57548_row0_col15" class="data row0 col15" >1195533664256.000000</td>
      <td id="T_57548_row0_col16" class="data row0 col16" >1238781526016.000000</td>
      <td id="T_57548_row0_col17" class="data row0 col17" >[35061.421875, 35088.99609375, 35092.234375, 35089.9609375, 0.0]</td>
      <td id="T_57548_row0_col18" class="data row0 col18" >0.093339</td>
      <td id="T_57548_row0_col19" class="data row0 col19" >1.970168</td>
      <td id="T_57548_row0_col20" class="data row0 col20" >2.997587</td>
      <td id="T_57548_row0_col21" class="data row0 col21" >3.241786</td>
      <td id="T_57548_row0_col22" class="data row0 col22" >2.933449</td>
      <td id="T_57548_row0_col23" class="data row0 col23" >16.131390</td>
      <td id="T_57548_row0_col24" class="data row0 col24" >27.092386</td>
      <td id="T_57548_row0_col25" class="data row0 col25" >103.206024</td>
      <td id="T_57548_row0_col26" class="data row0 col26" >-1714.965332</td>
      <td id="T_57548_row0_col27" class="data row0 col27" >3019.286133</td>
      <td id="T_57548_row0_col28" class="data row0 col28" >1879.417358</td>
      <td id="T_57548_row0_col29" class="data row0 col29" >339.480347</td>
      <td id="T_57548_row0_col30" class="data row0 col30" >335.586365</td>
      <td id="T_57548_row0_col31" class="data row0 col31" >3.532467</td>
      <td id="T_57548_row0_col32" class="data row0 col32" >0.651176</td>
      <td id="T_57548_row0_col33" class="data row0 col33" >0.001696</td>
      <td id="T_57548_row0_col34" class="data row0 col34" >0.000005</td>
      <td id="T_57548_row0_col35" class="data row0 col35" >0.758583</td>
      <td id="T_57548_row0_col36" class="data row0 col36" >0.830173</td>
      <td id="T_57548_row0_col37" class="data row0 col37" >0.872091</td>
      <td id="T_57548_row0_col38" class="data row0 col38" >0.901128</td>
      <td id="T_57548_row0_col39" class="data row0 col39" >0.984306</td>
      <td id="T_57548_row0_col40" class="data row0 col40" >0.990333</td>
      <td id="T_57548_row0_col41" class="data row0 col41" >0.997930</td>
      <td id="T_57548_row0_col42" class="data row0 col42" >0.999218</td>
      <td id="T_57548_row0_col43" class="data row0 col43" >11</td>
      <td id="T_57548_row0_col44" class="data row0 col44" >8</td>
      <td id="T_57548_row0_col45" class="data row0 col45" >3</td>
      <td id="T_57548_row0_col46" class="data row0 col46" >6</td>
      <td id="T_57548_row0_col47" class="data row0 col47" >217</td>
      <td id="T_57548_row0_col48" class="data row0 col48" >201</td>
      <td id="T_57548_row0_col49" class="data row0 col49" >27</td>
      <td id="T_57548_row0_col50" class="data row0 col50" >22</td>
      <td id="T_57548_row0_col51" class="data row0 col51" >3.344457</td>
      <td id="T_57548_row0_col52" class="data row0 col52" >3.831788</td>
      <td id="T_57548_row0_col53" class="data row0 col53" >2.267399</td>
      <td id="T_57548_row0_col54" class="data row0 col54" >1.662344</td>
      <td id="T_57548_row0_col55" class="data row0 col55" >0.723033</td>
      <td id="T_57548_row0_col56" class="data row0 col56" >0.400181</td>
      <td id="T_57548_row0_col57" class="data row0 col57" >0.576794</td>
      <td id="T_57548_row0_col58" class="data row0 col58" >0.073295</td>
      <td id="T_57548_row0_col59" class="data row0 col59" >0.002265</td>
      <td id="T_57548_row0_col60" class="data row0 col60" >0.000493</td>
      <td id="T_57548_row0_col61" class="data row0 col61" >0.000206</td>
      <td id="T_57548_row0_col62" class="data row0 col62" >0.000645</td>
      <td id="T_57548_row0_col63" class="data row0 col63" >0.175523</td>
      <td id="T_57548_row0_col64" class="data row0 col64" >0.130598</td>
      <td id="T_57548_row0_col65" class="data row0 col65" >0.694431</td>
      <td id="T_57548_row0_col66" class="data row0 col66" >0.993596</td>
      <td id="T_57548_row0_col67" class="data row0 col67" >0.006617</td>
      <td id="T_57548_row0_col68" class="data row0 col68" >0.006682</td>
      <td id="T_57548_row0_col69" class="data row0 col69" >0.008056</td>
      <td id="T_57548_row0_col70" class="data row0 col70" >0.014573</td>
      <td id="T_57548_row0_col71" class="data row0 col71" >0.997640</td>
      <td id="T_57548_row0_col72" class="data row0 col72" >0.997566</td>
      <td id="T_57548_row0_col73" class="data row0 col73" >0.997907</td>
      <td id="T_57548_row0_col74" class="data row0 col74" >0.997863</td>
      <td id="T_57548_row0_col75" class="data row0 col75" >0</td>
      <td id="T_57548_row0_col76" class="data row0 col76" >0</td>
      <td id="T_57548_row0_col77" class="data row0 col77" >0</td>
      <td id="T_57548_row0_col78" class="data row0 col78" >0</td>
      <td id="T_57548_row0_col79" class="data row0 col79" >0</td>
      <td id="T_57548_row0_col80" class="data row0 col80" >0</td>
      <td id="T_57548_row0_col81" class="data row0 col81" >0</td>
      <td id="T_57548_row0_col82" class="data row0 col82" >0</td>
      <td id="T_57548_row0_col83" class="data row0 col83" >0</td>
      <td id="T_57548_row0_col84" class="data row0 col84" >0</td>
      <td id="T_57548_row0_col85" class="data row0 col85" >1.506923</td>
      <td id="T_57548_row0_col86" class="data row0 col86" >1.158032</td>
      <td id="T_57548_row0_col87" class="data row0 col87" >0.999310</td>
      <td id="T_57548_row0_col88" class="data row0 col88" >1.020745</td>
      <td id="T_57548_row0_col89" class="data row0 col89" >4011.326172</td>
      <td id="T_57548_row0_col90" class="data row0 col90" >2604.875977</td>
      <td id="T_57548_row0_col91" class="data row0 col91" >389.356598</td>
      <td id="T_57548_row0_col92" class="data row0 col92" >353.816223</td>
      <td id="T_57548_row0_col93" class="data row0 col93" >2482.891846</td>
      <td id="T_57548_row0_col94" class="data row0 col94" >1350.747559</td>
      <td id="T_57548_row0_col95" class="data row0 col95" >180.096725</td>
      <td id="T_57548_row0_col96" class="data row0 col96" >166.191879</td>
      <td id="T_57548_row0_col97" class="data row0 col97" >4.829860</td>
      <td id="T_57548_row0_col98" class="data row0 col98" >0.860472</td>
      <td id="T_57548_row0_col99" class="data row0 col99" >0453p000</td>
      <td id="T_57548_row0_col100" class="data row0 col100" >0.000000</td>
      <td id="T_57548_row0_col101" class="data row0 col101" >0.000000</td>
      <td id="T_57548_row0_col102" class="data row0 col102" >0.000000</td>
      <td id="T_57548_row0_col103" class="data row0 col103" >0.000000</td>
      <td id="T_57548_row0_col104" class="data row0 col104" >0.000000</td>
      <td id="T_57548_row0_col105" class="data row0 col105" >0.000000</td>
      <td id="T_57548_row0_col106" class="data row0 col106" >1.534228</td>
      <td id="T_57548_row0_col107" class="data row0 col107" >2.334309</td>
      <td id="T_57548_row0_col108" class="data row0 col108" >2.524475</td>
      <td id="T_57548_row0_col109" class="data row0 col109" >2.284363</td>
      <td id="T_57548_row0_col110" class="data row0 col110" >1.534235</td>
      <td id="T_57548_row0_col111" class="data row0 col111" >2.334314</td>
      <td id="T_57548_row0_col112" class="data row0 col112" >2.524479</td>
      <td id="T_57548_row0_col113" class="data row0 col113" >2.284383</td>
      <td id="T_57548_row0_col114" class="data row0 col114" >  </td>
      <td id="T_57548_row0_col115" class="data row0 col115" >0</td>
      <td id="T_57548_row0_col116" class="data row0 col116" >0.000000</td>
      <td id="T_57548_row0_col117" class="data row0 col117" >0.000000</td>
      <td id="T_57548_row0_col118" class="data row0 col118" >0.000000</td>
      <td id="T_57548_row0_col119" class="data row0 col119" >0.000000</td>
      <td id="T_57548_row0_col120" class="data row0 col120" >0.000000</td>
      <td id="T_57548_row0_col121" class="data row0 col121" >0.000000</td>
      <td id="T_57548_row0_col122" class="data row0 col122" >0.000000</td>
      <td id="T_57548_row0_col123" class="data row0 col123" >0.000000</td>
      <td id="T_57548_row0_col124" class="data row0 col124" >False</td>
      <td id="T_57548_row0_col125" class="data row0 col125" >0.000000</td>
      <td id="T_57548_row0_col126" class="data row0 col126" >0.000000</td>
      <td id="T_57548_row0_col127" class="data row0 col127" >0</td>
      <td id="T_57548_row0_col128" class="data row0 col128" >0.000000</td>
      <td id="T_57548_row0_col129" class="data row0 col129" >0.000000</td>
      <td id="T_57548_row0_col130" class="data row0 col130" >0.000000</td>
      <td id="T_57548_row0_col131" class="data row0 col131" >0.000000</td>
      <td id="T_57548_row0_col132" class="data row0 col132" >0.000000</td>
      <td id="T_57548_row0_col133" class="data row0 col133" >0.000000</td>
      <td id="T_57548_row0_col134" class="data row0 col134" >0</td>
      <td id="T_57548_row0_col135" class="data row0 col135" >0</td>
      <td id="T_57548_row0_col136" class="data row0 col136" >0.000000</td>
      <td id="T_57548_row0_col137" class="data row0 col137" >0.000000</td>
      <td id="T_57548_row0_col138" class="data row0 col138" >0.001237</td>
    </tr>
    <tr>
      <th id="T_57548_level0_row1" class="row_heading level0 row1" >76347715933</th>
      <td id="T_57548_row1_col0" class="data row1 col0" >39627785483846390</td>
      <td id="T_57548_row1_col1" class="data row1 col1" >45.027565</td>
      <td id="T_57548_row1_col2" class="data row1 col2" >0.029181</td>
      <td id="T_57548_row1_col3" class="data row1 col3" >0.884491</td>
      <td id="T_57548_row1_col4" class="data row1 col4" >0.000116</td>
      <td id="T_57548_row1_col5" class="data row1 col5" ><table border="1" class="dataframe">
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
      <td id="T_57548_row1_col6" class="data row1 col6" ><table border="1" class="dataframe">
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
      <td id="T_57548_row1_col7" class="data row1 col7" ><table border="1" class="dataframe">
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
      <td id="T_57548_row1_col8" class="data row1 col8" >10000</td>
      <td id="T_57548_row1_col9" class="data row1 col9" >330548</td>
      <td id="T_57548_row1_col10" class="data row1 col10" >0451p000</td>
      <td id="T_57548_row1_col11" class="data row1 col11" >796</td>
      <td id="T_57548_row1_col12" class="data row1 col12" >REX</td>
      <td id="T_57548_row1_col13" class="data row1 col13" >45.027564</td>
      <td id="T_57548_row1_col14" class="data row1 col14" >0.029180</td>
      <td id="T_57548_row1_col15" class="data row1 col15" >107493949440.000000</td>
      <td id="T_57548_row1_col16" class="data row1 col16" >118149496832.000000</td>
      <td id="T_57548_row1_col17" class="data row1 col17" >[3543.986328125, 3635.03466796875, 3645.25732421875, 3635.730712890625, 0.0]</td>
      <td id="T_57548_row1_col18" class="data row1 col18" >0.094413</td>
      <td id="T_57548_row1_col19" class="data row1 col19" >0.055561</td>
      <td id="T_57548_row1_col20" class="data row1 col20" >0.515381</td>
      <td id="T_57548_row1_col21" class="data row1 col21" >1.539281</td>
      <td id="T_57548_row1_col22" class="data row1 col22" >3.094245</td>
      <td id="T_57548_row1_col23" class="data row1 col23" >13.725572</td>
      <td id="T_57548_row1_col24" class="data row1 col24" >5.308571</td>
      <td id="T_57548_row1_col25" class="data row1 col25" >8.346936</td>
      <td id="T_57548_row1_col26" class="data row1 col26" >113.335503</td>
      <td id="T_57548_row1_col27" class="data row1 col27" >3385.320068</td>
      <td id="T_57548_row1_col28" class="data row1 col28" >1953.585815</td>
      <td id="T_57548_row1_col29" class="data row1 col29" >278.208740</td>
      <td id="T_57548_row1_col30" class="data row1 col30" >255.909348</td>
      <td id="T_57548_row1_col31" class="data row1 col31" >3.577953</td>
      <td id="T_57548_row1_col32" class="data row1 col32" >0.707707</td>
      <td id="T_57548_row1_col33" class="data row1 col33" >0.001630</td>
      <td id="T_57548_row1_col34" class="data row1 col34" >0.000005</td>
      <td id="T_57548_row1_col35" class="data row1 col35" >0.756176</td>
      <td id="T_57548_row1_col36" class="data row1 col36" >0.828397</td>
      <td id="T_57548_row1_col37" class="data row1 col37" >0.870718</td>
      <td id="T_57548_row1_col38" class="data row1 col38" >0.900049</td>
      <td id="T_57548_row1_col39" class="data row1 col39" >0.984127</td>
      <td id="T_57548_row1_col40" class="data row1 col40" >0.990222</td>
      <td id="T_57548_row1_col41" class="data row1 col41" >0.997907</td>
      <td id="T_57548_row1_col42" class="data row1 col42" >0.999209</td>
      <td id="T_57548_row1_col43" class="data row1 col43" >11</td>
      <td id="T_57548_row1_col44" class="data row1 col44" >8</td>
      <td id="T_57548_row1_col45" class="data row1 col45" >3</td>
      <td id="T_57548_row1_col46" class="data row1 col46" >6</td>
      <td id="T_57548_row1_col47" class="data row1 col47" >215</td>
      <td id="T_57548_row1_col48" class="data row1 col48" >201</td>
      <td id="T_57548_row1_col49" class="data row1 col49" >26</td>
      <td id="T_57548_row1_col50" class="data row1 col50" >21</td>
      <td id="T_57548_row1_col51" class="data row1 col51" >0.998930</td>
      <td id="T_57548_row1_col52" class="data row1 col52" >0.963671</td>
      <td id="T_57548_row1_col53" class="data row1 col53" >1.272641</td>
      <td id="T_57548_row1_col54" class="data row1 col54" >1.131160</td>
      <td id="T_57548_row1_col55" class="data row1 col55" >0.410013</td>
      <td id="T_57548_row1_col56" class="data row1 col56" >0.758314</td>
      <td id="T_57548_row1_col57" class="data row1 col57" >0.612041</td>
      <td id="T_57548_row1_col58" class="data row1 col58" >0.193661</td>
      <td id="T_57548_row1_col59" class="data row1 col59" >0.000000</td>
      <td id="T_57548_row1_col60" class="data row1 col60" >0.000000</td>
      <td id="T_57548_row1_col61" class="data row1 col61" >0.000000</td>
      <td id="T_57548_row1_col62" class="data row1 col62" >0.000000</td>
      <td id="T_57548_row1_col63" class="data row1 col63" >0.033763</td>
      <td id="T_57548_row1_col64" class="data row1 col64" >0.149314</td>
      <td id="T_57548_row1_col65" class="data row1 col65" >5.182777</td>
      <td id="T_57548_row1_col66" class="data row1 col66" >4.711756</td>
      <td id="T_57548_row1_col67" class="data row1 col67" >0.015477</td>
      <td id="T_57548_row1_col68" class="data row1 col68" >0.010884</td>
      <td id="T_57548_row1_col69" class="data row1 col69" >0.008725</td>
      <td id="T_57548_row1_col70" class="data row1 col70" >0.011053</td>
      <td id="T_57548_row1_col71" class="data row1 col71" >0.988054</td>
      <td id="T_57548_row1_col72" class="data row1 col72" >0.989599</td>
      <td id="T_57548_row1_col73" class="data row1 col73" >0.991283</td>
      <td id="T_57548_row1_col74" class="data row1 col74" >0.991469</td>
      <td id="T_57548_row1_col75" class="data row1 col75" >0</td>
      <td id="T_57548_row1_col76" class="data row1 col76" >0</td>
      <td id="T_57548_row1_col77" class="data row1 col77" >0</td>
      <td id="T_57548_row1_col78" class="data row1 col78" >0</td>
      <td id="T_57548_row1_col79" class="data row1 col79" >0</td>
      <td id="T_57548_row1_col80" class="data row1 col80" >0</td>
      <td id="T_57548_row1_col81" class="data row1 col81" >0</td>
      <td id="T_57548_row1_col82" class="data row1 col82" >0</td>
      <td id="T_57548_row1_col83" class="data row1 col83" >0</td>
      <td id="T_57548_row1_col84" class="data row1 col84" >0</td>
      <td id="T_57548_row1_col85" class="data row1 col85" >1.506923</td>
      <td id="T_57548_row1_col86" class="data row1 col86" >1.158032</td>
      <td id="T_57548_row1_col87" class="data row1 col87" >0.999310</td>
      <td id="T_57548_row1_col88" class="data row1 col88" >1.020745</td>
      <td id="T_57548_row1_col89" class="data row1 col89" >4011.326172</td>
      <td id="T_57548_row1_col90" class="data row1 col90" >2604.875977</td>
      <td id="T_57548_row1_col91" class="data row1 col91" >389.356598</td>
      <td id="T_57548_row1_col92" class="data row1 col92" >353.816223</td>
      <td id="T_57548_row1_col93" class="data row1 col93" >2482.891846</td>
      <td id="T_57548_row1_col94" class="data row1 col94" >1350.747559</td>
      <td id="T_57548_row1_col95" class="data row1 col95" >180.096725</td>
      <td id="T_57548_row1_col96" class="data row1 col96" >166.191879</td>
      <td id="T_57548_row1_col97" class="data row1 col97" >4.829860</td>
      <td id="T_57548_row1_col98" class="data row1 col98" >0.860472</td>
      <td id="T_57548_row1_col99" class="data row1 col99" >0453p000</td>
      <td id="T_57548_row1_col100" class="data row1 col100" >0.224949</td>
      <td id="T_57548_row1_col101" class="data row1 col101" >7208.357422</td>
      <td id="T_57548_row1_col102" class="data row1 col102" >0.000000</td>
      <td id="T_57548_row1_col103" class="data row1 col103" >0.000000</td>
      <td id="T_57548_row1_col104" class="data row1 col104" >0.000000</td>
      <td id="T_57548_row1_col105" class="data row1 col105" >0.000000</td>
      <td id="T_57548_row1_col106" class="data row1 col106" >0.038878</td>
      <td id="T_57548_row1_col107" class="data row1 col107" >0.360631</td>
      <td id="T_57548_row1_col108" class="data row1 col108" >1.077091</td>
      <td id="T_57548_row1_col109" class="data row1 col109" >2.165156</td>
      <td id="T_57548_row1_col110" class="data row1 col110" >0.038878</td>
      <td id="T_57548_row1_col111" class="data row1 col111" >0.360631</td>
      <td id="T_57548_row1_col112" class="data row1 col112" >1.077091</td>
      <td id="T_57548_row1_col113" class="data row1 col113" >2.165156</td>
      <td id="T_57548_row1_col114" class="data row1 col114" >  </td>
      <td id="T_57548_row1_col115" class="data row1 col115" >0</td>
      <td id="T_57548_row1_col116" class="data row1 col116" >0.000000</td>
      <td id="T_57548_row1_col117" class="data row1 col117" >0.000000</td>
      <td id="T_57548_row1_col118" class="data row1 col118" >0.000000</td>
      <td id="T_57548_row1_col119" class="data row1 col119" >0.000000</td>
      <td id="T_57548_row1_col120" class="data row1 col120" >0.000000</td>
      <td id="T_57548_row1_col121" class="data row1 col121" >0.000000</td>
      <td id="T_57548_row1_col122" class="data row1 col122" >0.000000</td>
      <td id="T_57548_row1_col123" class="data row1 col123" >0.000000</td>
      <td id="T_57548_row1_col124" class="data row1 col124" >False</td>
      <td id="T_57548_row1_col125" class="data row1 col125" >0.000000</td>
      <td id="T_57548_row1_col126" class="data row1 col126" >0.000000</td>
      <td id="T_57548_row1_col127" class="data row1 col127" >0</td>
      <td id="T_57548_row1_col128" class="data row1 col128" >0.000000</td>
      <td id="T_57548_row1_col129" class="data row1 col129" >0.000000</td>
      <td id="T_57548_row1_col130" class="data row1 col130" >0.000000</td>
      <td id="T_57548_row1_col131" class="data row1 col131" >0.000000</td>
      <td id="T_57548_row1_col132" class="data row1 col132" >0.000000</td>
      <td id="T_57548_row1_col133" class="data row1 col133" >0.000000</td>
      <td id="T_57548_row1_col134" class="data row1 col134" >0</td>
      <td id="T_57548_row1_col135" class="data row1 col135" >0</td>
      <td id="T_57548_row1_col136" class="data row1 col136" >1.000000</td>
      <td id="T_57548_row1_col137" class="data row1 col137" >0.000000</td>
      <td id="T_57548_row1_col138" class="data row1 col138" >0.004593</td>
    </tr>
  </tbody>
</table>
2 rows x 139 columns

## 05a - DESI x LSST DP2 dia_object
- A 7.3 GiB catalog called `desi_x_lsst_dp2_dia_obj` at ` /sdf/home/o/olynn/catalogs/` → NOTE: Looking to move this to the shared space at `/sdf/data/rubin/cosmicdata/lsdb` once I'm added to the sdf-rubin-cosmic` group
  - a crossmatch of DESI Main Survey (dark program) DR1 with LSST DP2 dia_object (DP2 v30_0_6 dia_object_collection; accessed May 29)
- A call to `is_valid_catalog` returns True,
  - with `2125` partitions found
  - and `Approximate coverage is 3.85% of the sky.`
- An interactive Dask Performance Report is available [here](https://olivialynn.github.io/DESI-Crossmatch-Project/05%20-%20DESI%20x%20LSST%20DP2/crossmatch_report_dia_obj.html)
  - and key metrics are described and analyzed at the bottom of the [section notebook](https://github.com/olivialynn/DESI-Crossmatch-Project/blob/main/05%20-%20DESI%20x%20LSST%20DP2/5.0%20-%20DESI%20x%20LSST%20DP2.ipynb)



### MOC
<img width="791" height="444" alt="Image" src="https://github.com/user-attachments/assets/aa798ab4-52ab-485a-a1a1-e9e76e1af332" />


### First 2 rows
<table id="T_9c0d7">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_9c0d7_level0_col0" class="col_heading level0 col0" >TARGETID</th>
      <th id="T_9c0d7_level0_col1" class="col_heading level0 col1" >TARGET_RA</th>
      <th id="T_9c0d7_level0_col2" class="col_heading level0 col2" >TARGET_DEC</th>
      <th id="T_9c0d7_level0_col3" class="col_heading level0 col3" >Z</th>
      <th id="T_9c0d7_level0_col4" class="col_heading level0 col4" >ZERR</th>
      <th id="T_9c0d7_level0_col5" class="col_heading level0 col5" >spectra_b</th>
      <th id="T_9c0d7_level0_col6" class="col_heading level0 col6" >spectra_r</th>
      <th id="T_9c0d7_level0_col7" class="col_heading level0 col7" >spectra_z</th>
      <th id="T_9c0d7_level0_col8" class="col_heading level0 col8" >dec</th>
      <th id="T_9c0d7_level0_col9" class="col_heading level0 col9" >diaObjectId</th>
      <th id="T_9c0d7_level0_col10" class="col_heading level0 col10" >nDiaSources</th>
      <th id="T_9c0d7_level0_col11" class="col_heading level0 col11" >ra</th>
      <th id="T_9c0d7_level0_col12" class="col_heading level0 col12" >tract</th>
      <th id="T_9c0d7_level0_col13" class="col_heading level0 col13" >diaObjectForcedSource</th>
      <th id="T_9c0d7_level0_col14" class="col_heading level0 col14" >diaSource</th>
      <th id="T_9c0d7_level0_col15" class="col_heading level0 col15" >_dist_arcsec</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_9c0d7_level0_row0" class="row_heading level0 row0" >1203863513569649040</th>
      <td id="T_9c0d7_row0_col0" class="data row0 col0" >39627437792825537</td>
      <td id="T_9c0d7_row0_col1" class="data row0 col1" >351.428181</td>
      <td id="T_9c0d7_row0_col2" class="data row0 col2" >-14.683122</td>
      <td id="T_9c0d7_row0_col3" class="data row0 col3" >1.368533</td>
      <td id="T_9c0d7_row0_col4" class="data row0 col4" >0.000138</td>
      <td id="T_9c0d7_row0_col5" class="data row0 col5" ><table border="1" class="dataframe">
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
      <td>5.040675</td>
      <td>0.103488</td>
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
      <td id="T_9c0d7_row0_col6" class="data row0 col6" ><table border="1" class="dataframe">
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
      <td>4.024427</td>
      <td>0.179777</td>
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
      <td id="T_9c0d7_row0_col7" class="data row0 col7" ><table border="1" class="dataframe">
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
      <td>0.567026</td>
      <td>2.449597</td>
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
      <td id="T_9c0d7_row0_col8" class="data row0 col8" >-14.683135</td>
      <td id="T_9c0d7_row0_col9" class="data row0 col9" >770721298467782915</td>
      <td id="T_9c0d7_row0_col10" class="data row0 col10" >1</td>
      <td id="T_9c0d7_row0_col11" class="data row0 col11" >351.428182</td>
      <td id="T_9c0d7_row0_col12" class="data row0 col12" >7297</td>
      <td id="T_9c0d7_row0_col13" class="data row0 col13" ><table border="1" class="dataframe">
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
      <td>i</td>
      <td>-14.683135</td>
      <td>...</td>
      <td>0.158163</td>
      <td>2025070100656</td>
    </tr>
    <tr>
      <td><i>+35 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_9c0d7_row0_col14" class="data row0 col14" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>band</th>
      <th>centroid_flag</th>
      <th>...</th>
      <th>y</th>
      <th>yErr</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>g</td>
      <td>False</td>
      <td>...</td>
      <td>923.079074</td>
      <td>0.253312</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_9c0d7_row0_col15" class="data row0 col15" >0.045792</td>
    </tr>
    <tr>
      <th id="T_9c0d7_level0_row1" class="row_heading level0 row1" >1203863976572888979</th>
      <td id="T_9c0d7_row1_col0" class="data row1 col0" >39627437792823928</td>
      <td id="T_9c0d7_row1_col1" class="data row1 col1" >351.350538</td>
      <td id="T_9c0d7_row1_col2" class="data row1 col2" >-14.676350</td>
      <td id="T_9c0d7_row1_col3" class="data row1 col3" >0.146449</td>
      <td id="T_9c0d7_row1_col4" class="data row1 col4" >0.000004</td>
      <td id="T_9c0d7_row1_col5" class="data row1 col5" ><table border="1" class="dataframe">
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
      <td>64.870834</td>
      <td>0.039033</td>
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
      <td id="T_9c0d7_row1_col6" class="data row1 col6" ><table border="1" class="dataframe">
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
      <td>36.507702</td>
      <td>0.079193</td>
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
      <td id="T_9c0d7_row1_col7" class="data row1 col7" ><table border="1" class="dataframe">
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
      <td>187.865128</td>
      <td>0.029783</td>
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
      <td id="T_9c0d7_row1_col8" class="data row1 col8" >-14.676350</td>
      <td id="T_9c0d7_row1_col9" class="data row1 col9" >770721367187259405</td>
      <td id="T_9c0d7_row1_col10" class="data row1 col10" >28</td>
      <td id="T_9c0d7_row1_col11" class="data row1 col11" >351.350518</td>
      <td id="T_9c0d7_row1_col12" class="data row1 col12" >7297</td>
      <td id="T_9c0d7_row1_col13" class="data row1 col13" ><table border="1" class="dataframe">
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
      <td>i</td>
      <td>-14.67635</td>
      <td>...</td>
      <td>0.002871</td>
      <td>2025070100656</td>
    </tr>
    <tr>
      <td><i>+34 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_9c0d7_row1_col14" class="data row1 col14" ><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>band</th>
      <th>centroid_flag</th>
      <th>...</th>
      <th>y</th>
      <th>yErr</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>i</td>
      <td>False</td>
      <td>...</td>
      <td>2971.985481</td>
      <td>0.22065</td>
    </tr>
    <tr>
      <td><i>+27 rows</i></td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table></td>
      <td id="T_9c0d7_row1_col15" class="data row1 col15" >0.071685</td>
    </tr>
  </tbody>
</table>
2 rows x 16 columns


## 05b - DESI x LSST DP2 object
- A 94 GiB catalog called `desi_x_lsst_dp2_object` at `/sdf/data/rubin/user/olynn/`
  - a crossmatch of DESI Main Survey (dark program) DR1 with LSST DP2 object (DP2 v30_0_6 object_collection; accessed June 1)
- A call to `is_valid_catalog` returns True,
  - with `24553` partitions found
  - and `Approximate coverage is 3.57 % of the sky.`
- An interactive Dask Performance Report is available [here](https://olivialynn.github.io/DESI-Crossmatch-Project/05%20-%20DESI%20x%20LSST%20DP2/crossmatch_report_object.html)
  - and key metrics are described and analyzed at the bottom of the [section notebook](https://github.com/olivialynn/DESI-Crossmatch-Project/blob/main/05%20-%20DESI%20x%20LSST%20DP2/5.0%20-%20DESI%20x%20LSST%20DP2.ipynb)

### MOC
<img width="945" height="510" alt="Image" src="https://github.com/user-attachments/assets/06c0c298-babc-405d-b572-89bfeb98011b" />

### First 2 rows
<table id="T_ff59c">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_ff59c_level0_col0" class="col_heading level0 col0" >TARGETID</th>
      <th id="T_ff59c_level0_col1" class="col_heading level0 col1" >TARGET_RA</th>
      <th id="T_ff59c_level0_col2" class="col_heading level0 col2" >TARGET_DEC</th>
      <th id="T_ff59c_level0_col3" class="col_heading level0 col3" >Z</th>
      <th id="T_ff59c_level0_col4" class="col_heading level0 col4" >ZERR</th>
      <th id="T_ff59c_level0_col5" class="col_heading level0 col5" >spectra_b</th>
      <th id="T_ff59c_level0_col6" class="col_heading level0 col6" >spectra_r</th>
      <th id="T_ff59c_level0_col7" class="col_heading level0 col7" >spectra_z</th>
      <th id="T_ff59c_level0_col8" class="col_heading level0 col8" >objectId</th>
      <th id="T_ff59c_level0_col9" class="col_heading level0 col9" >coord_ra</th>
      <th id="T_ff59c_level0_col10" class="col_heading level0 col10" >coord_dec</th>
      <th id="T_ff59c_level0_col11" class="col_heading level0 col11" >r_psfMag</th>
      <th id="T_ff59c_level0_col12" class="col_heading level0 col12" >r_psfMagErr</th>
      <th id="T_ff59c_level0_col13" class="col_heading level0 col13" >_dist_arcsec</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_ff59c_level0_row0" class="row_heading level0 row0" >47991521810220274</th>
      <td id="T_ff59c_row0_col0" class="data row0 col0" >39628230637916670</td>
      <td id="T_ff59c_row0_col1" class="data row0 col1" >23.190178</td>
      <td id="T_ff59c_row0_col2" class="data row0 col2" >18.856721</td>
      <td id="T_ff59c_row0_col3" class="data row0 col3" >1.489172</td>
      <td id="T_ff59c_row0_col4" class="data row0 col4" >0.000865</td>
      <td id="T_ff59c_row0_col5" class="data row0 col5" ><table border="1" class="dataframe">
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
      <td>0.002376</td>
      <td>0.045902</td>
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
      <td id="T_ff59c_row0_col6" class="data row0 col6" ><table border="1" class="dataframe">
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
      <td>0.180997</td>
      <td>2.603897</td>
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
      <td id="T_ff59c_row0_col7" class="data row0 col7" ><table border="1" class="dataframe">
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
      <td>0.920303</td>
      <td>8.82909</td>
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
      <td id="T_ff59c_row0_col8" class="data row0 col8" >805469645476725267</td>
      <td id="T_ff59c_row0_col9" class="data row0 col9" >23.190189</td>
      <td id="T_ff59c_row0_col10" class="data row0 col10" >18.856733</td>
      <td id="T_ff59c_row0_col11" class="data row0 col11" ><NA></td>
      <td id="T_ff59c_row0_col12" class="data row0 col12" ><NA></td>
      <td id="T_ff59c_row0_col13" class="data row0 col13" >0.058550</td>
    </tr>
    <tr>
      <th id="T_ff59c_level0_row1" class="row_heading level0 row1" >47992039361544743</th>
      <td id="T_ff59c_row1_col0" class="data row1 col0" >39628236367335481</td>
      <td id="T_ff59c_row1_col1" class="data row1 col1" >23.165036</td>
      <td id="T_ff59c_row1_col2" class="data row1 col2" >18.888546</td>
      <td id="T_ff59c_row1_col3" class="data row1 col3" >0.880572</td>
      <td id="T_ff59c_row1_col4" class="data row1 col4" >0.000065</td>
      <td id="T_ff59c_row1_col5" class="data row1 col5" ><table border="1" class="dataframe">
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
      <td>0.322199</td>
      <td>0.234359</td>
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
      <td id="T_ff59c_row1_col6" class="data row1 col6" ><table border="1" class="dataframe">
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
      <td>7.639961</td>
      <td>0.089456</td>
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
      <td id="T_ff59c_row1_col7" class="data row1 col7" ><table border="1" class="dataframe">
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
      <td>-0.006492</td>
      <td>18.115849</td>
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
      <td id="T_ff59c_row1_col8" class="data row1 col8" >805469645476725414</td>
      <td id="T_ff59c_row1_col9" class="data row1 col9" >23.165003</td>
      <td id="T_ff59c_row1_col10" class="data row1 col10" >18.888799</td>
      <td id="T_ff59c_row1_col11" class="data row1 col11" ><NA></td>
      <td id="T_ff59c_row1_col12" class="data row1 col12" ><NA></td>
      <td id="T_ff59c_row1_col13" class="data row1 col13" >0.919738</td>
    </tr>
  </tbody>
</table>
2 rows x 14 columns
