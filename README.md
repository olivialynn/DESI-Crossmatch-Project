*Interactive Dask performance report quick links:*
- [02 - DESI x Gaia](https://olivialynn.github.io/DESI-Crossmatch-Project/02%20-%20DESI%20x%20Gaia/crossmatch_report.html)
- 03 (in progress)

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
