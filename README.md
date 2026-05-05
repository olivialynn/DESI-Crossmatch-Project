# Progress so far:
## 02 - DESI x Gaia
- A 71 GiB catalog called `desi_x_gaia` at `/global/cfs/cdirs/cosmo/users/olynn/`
  - a crossmatch of DESI Main Survey (dark program) DR1 with Gaia DR3
- MOC appears functionally identical to the MOC included in the section below, "01 - DESI Data"
- An interactive Dask Performance Report is available [here](https://olivialynn.github.io/DESI-Crossmatch-Project/02%20-%20DESI%20x%20Gaia/crossmatch_report.html)
- First 5 rows as follows:

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
    <tr>
      <th id="T_0b2e5_level0_row2" class="row_heading level0 row2" >2976627719789</th>
      <td id="T_0b2e5_row2_col0" class="data row2 col0" >39627791519453248</td>
      <td id="T_0b2e5_row2_col1" class="data row2 col1" >44.884761</td>
      <td id="T_0b2e5_row2_col2" class="data row2 col2" >0.164806</td>
      <td id="T_0b2e5_row2_col3" class="data row2 col3" >0.807195</td>
      <td id="T_0b2e5_row2_col4" class="data row2 col4" >0.000015</td>
      <td id="T_0b2e5_row2_col5" class="data row2 col5" ><table border="1" class="dataframe">
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
      <td>6.968853</td>
      <td>0.189194</td>
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
      <td id="T_0b2e5_row2_col6" class="data row2 col6" ><table border="1" class="dataframe">
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
      <td>1.523983</td>
      <td>3.836734</td>
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
      <td id="T_0b2e5_row2_col7" class="data row2 col7" ><table border="1" class="dataframe">
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
      <td>0.590848</td>
      <td>16.481377</td>
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
      <td id="T_0b2e5_row2_col8" class="data row2 col8" >5944234902272</td>
      <td id="T_0b2e5_row2_col9" class="data row2 col9" >44.884761</td>
      <td id="T_0b2e5_row2_col10" class="data row2 col10" >0.164806</td>
      <td id="T_0b2e5_row2_col11" class="data row2 col11" >0.000834</td>
    </tr>
    <tr>
      <th id="T_0b2e5_level0_row3" class="row_heading level0 row3" >3287693392179</th>
      <td id="T_0b2e5_row3_col0" class="data row3 col0" >39627791519454413</td>
      <td id="T_0b2e5_row3_col1" class="data row3 col1" >44.919962</td>
      <td id="T_0b2e5_row3_col2" class="data row3 col2" >0.215757</td>
      <td id="T_0b2e5_row3_col3" class="data row3 col3" >0.808562</td>
      <td id="T_0b2e5_row3_col4" class="data row3 col4" >0.000070</td>
      <td id="T_0b2e5_row3_col5" class="data row3 col5" ><table border="1" class="dataframe">
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
      <td>2.379487</td>
      <td>0.144059</td>
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
      <td id="T_0b2e5_row3_col6" class="data row3 col6" ><table border="1" class="dataframe">
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
      <td>2.873809</td>
      <td>0.378829</td>
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
      <td id="T_0b2e5_row3_col7" class="data row3 col7" ><table border="1" class="dataframe">
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
      <td>0.994231</td>
      <td>6.393195</td>
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
      <td id="T_0b2e5_row3_col8" class="data row3 col8" >6567005330944</td>
      <td id="T_0b2e5_row3_col9" class="data row3 col9" >44.919961</td>
      <td id="T_0b2e5_row3_col10" class="data row3 col10" >0.215756</td>
      <td id="T_0b2e5_row3_col11" class="data row3 col11" >0.005419</td>
    </tr>
    <tr>
      <th id="T_0b2e5_level0_row4" class="row_heading level0 row4" >3679366411269</th>
      <td id="T_0b2e5_row4_col0" class="data row4 col0" >39627791523644892</td>
      <td id="T_0b2e5_row4_col1" class="data row4 col1" >45.050386</td>
      <td id="T_0b2e5_row4_col2" class="data row4 col2" >0.219434</td>
      <td id="T_0b2e5_row4_col3" class="data row4 col3" >-0.000279</td>
      <td id="T_0b2e5_row4_col4" class="data row4 col4" >0.000009</td>
      <td id="T_0b2e5_row4_col5" class="data row4 col5" ><table border="1" class="dataframe">
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
      <td>5.181625</td>
      <td>0.132983</td>
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
      <td id="T_0b2e5_row4_col6" class="data row4 col6" ><table border="1" class="dataframe">
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
      <td>8.459776</td>
      <td>1.575747</td>
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
      <td id="T_0b2e5_row4_col7" class="data row4 col7" ><table border="1" class="dataframe">
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
      <td>5.367475</td>
      <td>4.564589</td>
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
      <td id="T_0b2e5_row4_col8" class="data row4 col8" >7352984181120</td>
      <td id="T_0b2e5_row4_col9" class="data row4 col9" >45.050386</td>
      <td id="T_0b2e5_row4_col10" class="data row4 col10" >0.219434</td>
      <td id="T_0b2e5_row4_col11" class="data row4 col11" >0.002946</td>
    </tr>
  </tbody>
</table>
5 rows x 12 columns

## 01 - DESI Data
- A 700GiB  catalog called `desi-dr1-main-dark` at `/global/cfs/cdirs/cosmo/users/olynn/`
  - covers DESI's **main** survey, **dark** program
- A call to `is_valid_catalog` returns True, 
  - with `5769 partitions` found 
  - and `Approximate coverage is 33.39 % of the sky.`
- Notably we are missing coverage of the galactic plane, 
  - but since our decision (co-working meeting 4/29) to skip the main/bright program and only use main/dark, this is unsurprising

<img width="805" height="440" alt="Image" src="https://github.com/user-attachments/assets/6de43034-c34c-49fa-b308-377538f50d3c" />

- First 5 rows as follows:

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
    <tr>
      <th id="T_ebded_level0_row2" class="row_heading level0 row2" >79430617729</th>
      <td id="T_ebded_row2_col0" class="data row2 col0" >2714981116149760</td>
      <td id="T_ebded_row2_col1" class="data row2 col1" >45.018964</td>
      <td id="T_ebded_row2_col2" class="data row2 col2" >0.029766</td>
      <td id="T_ebded_row2_col3" class="data row2 col3" >0.129609</td>
      <td id="T_ebded_row2_col4" class="data row2 col4" >0.000009</td>
      <td id="T_ebded_row2_col5" class="data row2 col5" ><table border="1" class="dataframe">
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
      <td>-5.12881</td>
      <td>0.024819</td>
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
      <td id="T_ebded_row2_col6" class="data row2 col6" ><table border="1" class="dataframe">
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
      <td>0.757192</td>
      <td>0.056087</td>
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
      <td id="T_ebded_row2_col7" class="data row2 col7" ><table border="1" class="dataframe">
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
      <td>0.227893</td>
      <td>10.47636</td>
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
      <th id="T_ebded_level0_row3" class="row_heading level0 row3" >88592216842</th>
      <td id="T_ebded_row3_col0" class="data row3 col0" >-110547443</td>
      <td id="T_ebded_row3_col1" class="data row3 col1" >45.028689</td>
      <td id="T_ebded_row3_col2" class="data row3 col2" >0.031667</td>
      <td id="T_ebded_row3_col3" class="data row3 col3" >1.499465</td>
      <td id="T_ebded_row3_col4" class="data row3 col4" >0.000098</td>
      <td id="T_ebded_row3_col5" class="data row3 col5" ><table border="1" class="dataframe">
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
      <td>1.824267</td>
      <td>0.085791</td>
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
      <td id="T_ebded_row3_col6" class="data row3 col6" ><table border="1" class="dataframe">
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
      <td>-0.888818</td>
      <td>1.860335</td>
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
      <td id="T_ebded_row3_col7" class="data row3 col7" ><table border="1" class="dataframe">
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
      <td>-0.377297</td>
      <td>4.615465</td>
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
      <th id="T_ebded_level0_row4" class="row_heading level0 row4" >101138674798</th>
      <td id="T_ebded_row4_col0" class="data row4 col0" >39627785483846478</td>
      <td id="T_ebded_row4_col1" class="data row4 col1" >45.030526</td>
      <td id="T_ebded_row4_col2" class="data row4 col2" >0.041094</td>
      <td id="T_ebded_row4_col3" class="data row4 col3" >1.263249</td>
      <td id="T_ebded_row4_col4" class="data row4 col4" >0.000090</td>
      <td id="T_ebded_row4_col5" class="data row4 col5" ><table border="1" class="dataframe">
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
      <td>0.314766</td>
      <td>0.135213</td>
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
      <td id="T_ebded_row4_col6" class="data row4 col6" ><table border="1" class="dataframe">
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
      <td>0.615158</td>
      <td>3.966969</td>
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
      <td id="T_ebded_row4_col7" class="data row4 col7" ><table border="1" class="dataframe">
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
      <td>1.088948</td>
      <td>11.775853</td>
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
5 rows x 8 columns
